# awesome-memorization-wiki — スキーマ定義

LLM の **Memorization（訓練データの暗記）** に関する知識を蓄積する LLM Wiki。
GitHub Pages で <https://upura.github.io/awesome-memorization-wiki> として公開している。
「質問のたびにゼロから再発見する」RAG ではなく、**繋がりが永続的に蓄積される知識ベース**を目指す。

軸となる一次資料は次のサーベイ論文である。

> 石原祥太郎, 高橋寛武「大規模言語モデルの訓練データ暗記の研究動向」
> 人工知能学会論文誌 41巻4号 AN40-F (2026). DOI: 10.1527/tjsai.41-4_AN40-F

このサーベイの **訓練セット / モデル / 出力** という 3 軸（図1）を、本 Wiki の
概念ページを組織する骨格として採用する。新しいソースは必ずこの 3 軸のどこに
位置づくかを明示すること。

---

## 1. 三層構造

| 層 | 管理者 | 内容 |
|---|---|---|
| **Raw sources** | 人間 | `docs/raw/` 配下。論文 PDF や記事クリッピング。**不変**。LLM は書き換えない |
| **Wiki** | LLM | `docs/wiki/` 配下。要約・概念ページ・相互参照を含む markdown 群 |
| **Schema** | 人間 | 本ファイル（`CLAUDE.md`）と `.claude/skills/`。ワークフローと命名規約 |

## 2. ディレクトリ構成

```
awesome-memorization-wiki/
├── CLAUDE.md                  # このファイル（スキーマ定義）
├── README.md                  # サイトのトップページ 兼 目次。index の役割を兼ねる
├── _config.yml                # Jekyll 設定（GitHub Pages）
├── _layouts/default.html      # サイト共通レイアウト
├── .github/workflows/
│   ├── jekyll-gh-pages.yml    # main への push で GitHub Pages にデプロイ
│   └── lint.yml               # verify_wiki.py を CI で実行
├── tools/verify_wiki.py       # 整合性チェック（lint スキルの内部検査）
├── .claude/skills/
│   ├── ingest-paper/SKILL.md
│   ├── ingest-article/SKILL.md
│   ├── query/SKILL.md
│   └── lint/SKILL.md
└── docs/
    ├── raw/                   # 一次資料。PDF は .gitignore 済み（出版社の権利のため）
    │   ├── papers/
    │   └── articles/
    └── wiki/                  # Obsidian Vault としても開ける
        ├── log.md             # 操作履歴を時系列で追記
        ├── papers/            # 論文サマリー
        ├── articles/          # 記事サマリー
        ├── concepts/          # 横断的な概念
        └── queries/           # query 結果
```

**`docs/wiki/index.md` は無い。** カタログの役割は `README.md` が兼ねる
（GitHub Pages が README.md をサイトのトップページとして描画するため）。
新規ページを作ったら **README.md の目次に 1 行足す**こと。`verify_wiki.py` が
掲載漏れを検出する。

## 3. 命名規約

| 種別 | 規約 | 例 |
|---|---|---|
| 論文サマリー | `{筆頭著者姓小文字}-{発行年}-{内容スラッグ}.md` | `carlini-2023-quantifying-memorization.md` |
| 記事サマリー | `{発行年}-{媒体}-{スラッグ}.md` | `2025-zenn-llm-wiki.md` |
| 概念ページ | `{英語スラッグ}.md`（ケバブケース） | `membership-inference.md` |
| Query ページ | `{YYYY-MM-DD}-{質問スラッグ}.md` | `2026-07-29-mia-is-broken.md` |

サーベイ本文が使う **引用キー**（`[Carlini 23b]` 等）は論文ページの
frontmatter `citekey` に必ず保持する。サーベイ本文との往復に使うため。

## 4. Frontmatter

論文ページ:

```yaml
---
title: 論文タイトル（原題）
authors: [著者1, 著者2]
year: 2023
venue: ICLR 2023
citekey: Carlini 23b        # サーベイ本文中の引用キー（あれば）
url: https://...
tags: [memorization, quantification, scaling]
axis: [訓練セット, モデル, 出力]   # サーベイ図1 の 3 軸のどこに属するか
type: paper
stub: true                  # 原論文未読の場合のみ
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---
```

概念ページ:

```yaml
---
title: 日本語での概念名（英語名）
aliases: [別名, English Name]
axis: モデル                  # 訓練セット / モデル / 出力 / 横断 のいずれか
survey_section: "3・1"        # 対応するサーベイの節番号（あれば）
tags: [...]
type: concept
---
```

`axis` の値は **訓練セット / モデル / 出力 / 横断** のいずれかでなければならない
（`verify_wiki.py` が検査する）。`type` と `axis` はサイトのページヘッダにも表示される。

## 5. リンク規約

**Obsidian の `[[wikilink]]` は使わない。** Jekyll が解決できず、公開サイトで
リンク切れになるため。標準の markdown 相対リンクを使う。Obsidian でも問題なく辿れる。

```markdown
[文字列の重複](string-duplication.md)                     # 概念 → 概念
[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md)  # 概念 → 論文
[メンバーシップ推論](../concepts/membership-inference.md)   # 論文 → 概念
```

- **論文へのリンクは表示名をサーベイの引用キーに揃える**（`[Carlini 23b]`）。
  未取り込みの論文を素の `[Huang 22a]` と書いたときと見た目が揃い、
  リンクの有無がそのまま「取り込み済みかどうか」を表す。
- リンクは**惜しまず張る**。ただし存在しないファイルを指すとリンク切れになるので、
  未作成ページへの言及は `[Hong 25a]`（リンクなし・要 ingest）の形で残す。
- 論文ページは必ず 1 つ以上の概念ページにリンクする。
- 概念ページは必ず 2 つ以上の論文ページにリンクする（1 本しか根拠がない
  概念は、まだ「概念」ではなく論文サマリーの一部である）。
- 概念 → 論文 のリンクには、論文ページの `## Wiki 内の接点` から**返リンク**を張る。

## 6. 必須セクション

**概念ページ**には以下を必ず置く（本 Wiki の心臓部）:

- `## 定義` — 何を指すか。サーベイの節番号を併記
- `## 主要な論文` — 論文ページへのリンクと 1 行の位置づけ
- `## 横断的知見` — 複数ソースを突き合わせて初めて見える観察。
  **1 本の論文だけから言えることは書かない**
- `## 未解決の問い` — 次に調べるべきこと。ingest のたびに解消・追加される

**論文ページ**には以下を必ず置く:

- `## TL;DR` — 3 行以内
- `## 位置づけ` — サーベイのどの章節に対応するか、3 軸のどこか
- `## 手法・実験`
- `## 主要な知見`
- `## 限界・批判`
- `## Wiki 内の接点` — 既存ページとどう繋がるか

## 7. 運用ルール

- **量より質**。1 回の ingest で 5 本以上を一気に入れない。人間が読んで
  理解することがボトルネックである。
- ingest 1 本で 10〜15 ページに更新が波及するのが正常。更新が 1 ページで
  止まったら、繋げ方を疑うこと。
- `docs/wiki/log.md` は**追記のみ**。過去行を書き換えない。
- 出典のない主張を書かない。推測を書く場合は `（推測）` と明記する。
- **原論文を読んでいない論文ページは `stub: true` と明記する。** 嘘をつかない。
- 日本語で書く。ただし専門用語は初出時に英語を併記する。
- サーベイと矛盾する知見を見つけたら消さずに残し、概念ページの
  `## 横断的知見` に「サーベイ（2026）は X としているが、Y は Z を報告」
  という形で対立を明示する。

## 8. 公開に関する注意

- **一次資料の PDF はコミットしない。** `docs/raw/papers/*.pdf` は `.gitignore`
  済み。出版社が権利を持つ PDF を公開リポジトリで再配布しないため。
  論文ページの frontmatter には `url`（出版社サイトへのリンク）を必ず入れる。
- 日本語 PDF の本文抽出は poppler の `pdftotext -enc UTF-8` を使う。
  Python の pypdf は CID フォントで文字化けする（軸論文で実証済み）。
- **frontmatter の値にコロン（`: `）が含まれるときは必ず `"..."` で囲む。**
  `title: Foo: Bar` のような行は YAML として不正で、**サイト全体のビルドが落ちる**。
  論文の原題や `venue`（`ACL 2025 (Volume 1: Long Papers)` など）で起きやすい。
- 変更を push する前に `python3 tools/verify_wiki.py` を通す。CI でも走る。
- kramdown の制約により、**リスト項目内のパイプ文字は `\|` にエスケープ**する
  （表として誤解釈されるため）。`verify_wiki.py` が検出する。
