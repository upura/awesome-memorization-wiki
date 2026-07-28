#!/usr/bin/env python3
"""LLM Wiki の整合性チェック(lint スキルの内部検査項目)。

検査:
  1. 相対リンク切れ
  2. 孤立ページ(どこからもリンクされていない)
  3. 必須セクションの欠落(CLAUDE.md 6 節)
  4. frontmatter の YAML 妥当性・必須キー・axis の値
  5. 概念ページから論文ページへのリンクが 2 本未満(根拠 1 本の概念)
  6. 論文ページから概念ページへのリンクが 0 本
  7. 片方向リンク(概念 -> 論文 に対する返リンクが無い)
  8. README.md の目次と実ファイルの同期
  9. Obsidian の [[wikilink]] の残存(Jekyll で解決できない)
 10. リスト項目内の未エスケープパイプ(kramdown が表として誤解釈する)

問題があれば終了コード 1。
"""
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
WIKI = os.path.join(ROOT, "docs", "wiki")
README = os.path.join(ROOT, "README.md")

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")
VALID_AXIS = {"訓練セット", "モデル", "出力", "横断"}

REQUIRED_CONCEPT = ["## 定義", "## 主要な論文", "## 横断的知見", "## 未解決の問い"]
REQUIRED_PAPER = ["## TL;DR", "## 位置づけ", "## 手法・実験",
                  "## 主要な知見", "## 限界・批判", "## Wiki 内の接点"]

problems: list[str] = []


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


# ---- 収集 -------------------------------------------------------------
md_files = [README]
for dirpath, _, files in os.walk(os.path.join(ROOT, "docs")):
    md_files += [os.path.join(dirpath, f) for f in sorted(files) if f.endswith(".md")]

text = {p: open(p, encoding="utf-8").read() for p in md_files}


def frontmatter(t: str) -> dict:
    if not t.startswith("---\n"):
        return {}
    body = t.split("---\n", 2)[1]
    fm = {}
    for line in body.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def check_frontmatter_yaml(path: str, t: str) -> None:
    """frontmatter が正しい YAML か検査する。

    ここが壊れると Jekyll のビルドがサイト全体で落ちるため、最優先の検査項目。
    典型的な事故は `title: Foo: Bar` のようにコロンを含む値を引用符で囲み忘れること。
    """
    if not t.startswith("---\n") or "---\n" not in t[4:]:
        problems.append(f"[frontmatter 無し] {rel(path)}")
        return
    fm = t.split("---\n", 2)[1]
    for i, line in enumerate(fm.splitlines(), 2):
        m = re.match(r"^([a-z_]+):\s+(.+)$", line)
        if not m:
            continue
        value = m.group(2)
        if value.startswith(('"', "'", "[", "{")):
            continue
        if ": " in value or value.endswith(":"):
            problems.append(
                f"[frontmatter YAML] {rel(path)}:{i}: "
                f"`{m.group(1)}` の値にコロンがある。\"...\" で囲むこと")


def pages_in(sub: str) -> list[str]:
    d = os.path.join(WIKI, sub)
    if not os.path.isdir(d):
        return []
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]


concepts = pages_in("concepts")
papers = pages_in("papers")
queries = pages_in("queries")

# path -> リンク先の絶対パス集合
outgoing: dict[str, set[str]] = {}
for path, t in text.items():
    targets = set()
    for m in LINK_RE.finditer(t):
        target = m.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = target.split("#")[0]
        if not target_path:
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target_path))
        # 1. 相対リンク切れ
        if not os.path.exists(resolved):
            problems.append(f"[相対リンク切れ] {rel(path)}: {target}")
        else:
            targets.add(resolved)
    outgoing[path] = targets

incoming: dict[str, set[str]] = {p: set() for p in md_files}
for src, targets in outgoing.items():
    for t in targets:
        incoming.setdefault(t, set()).add(src)

# ---- 2. 孤立ページ ----------------------------------------------------
for p in concepts + papers + queries:
    if not incoming.get(p):
        problems.append(f"[孤立ページ] {rel(p)}: どこからもリンクされていない")

# ---- 3-6. ページ単位の検査 -------------------------------------------
for p in concepts + papers + queries:
    check_frontmatter_yaml(p, text[p])

for p in concepts + papers:
    t = text[p]
    fm = frontmatter(t)
    is_concept = p in concepts

    for section in (REQUIRED_CONCEPT if is_concept else REQUIRED_PAPER):
        if section not in t:
            problems.append(f"[必須セクション欠落] {rel(p)}: {section}")

    for key in ("title", "type"):
        if key not in fm:
            problems.append(f"[frontmatter 欠落] {rel(p)}: {key}")

    axis = fm.get("axis", "")
    for value in re.findall(r"[^\[\],\s]+", axis):
        if value not in VALID_AXIS:
            problems.append(f"[axis 不正] {rel(p)}: {value}")

    if is_concept:
        n = len(outgoing[p] & set(papers))
        if n < 2:
            problems.append(
                f"[根拠不足] {rel(p)}: 論文ページへのリンクが {n} 本"
                "(概念には 2 本以上必要)")
    else:
        if not outgoing[p] & set(concepts):
            problems.append(f"[接点なし] {rel(p)}: 概念ページへのリンクが 0 本")

# ---- 7. 片方向リンク --------------------------------------------------
for c in concepts:
    for pa in sorted(outgoing[c] & set(papers)):
        if c not in outgoing[pa]:
            problems.append(
                f"[片方向リンク] {rel(c)} -> {rel(pa)}: 返リンクが無い")

# ---- 8. README 目次の同期 --------------------------------------------
readme_targets = outgoing[README]
for p in concepts + papers + queries:
    if p not in readme_targets:
        problems.append(f"[目次未掲載] {rel(p)}: README.md から辿れない")

# ---- 9-10. 記法 -------------------------------------------------------
for path, t in text.items():
    for i, line in enumerate(t.splitlines(), 1):
        # インラインコード（記法そのものの説明）は検査対象外
        bare = re.sub(r"`[^`]*`", "", line)
        if WIKILINK_RE.search(bare):
            problems.append(
                f"[wikilink 残存] {rel(path)}:{i}: Jekyll で解決できない")
        if re.match(r"^\s*[-*]\s", bare) and re.search(r"(?<!\\)\|", bare):
            problems.append(
                f"[未エスケープパイプ] {rel(path)}:{i}: "
                "リスト項目内の | は \\| にする")

# ---- 出力 -------------------------------------------------------------
print(f"検査対象: {len(md_files)} ファイル "
      f"(概念 {len(concepts)} / 論文 {len(papers)} / Query {len(queries)})")
if problems:
    print(f"\n{len(problems)} 件の問題:")
    for p in problems:
        print("  " + p)
    sys.exit(1)
print("問題なし")
