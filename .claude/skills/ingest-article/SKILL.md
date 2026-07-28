---
name: ingest-article
description: Web 記事・ブログ・ニュースをクリッピングして Wiki に取り込む。「この記事を入れて」「URL を ingest」と言われたときに使う。
---

# ingest-article

Web 記事を Wiki に取り込む。手順は [ingest-paper](../ingest-paper/SKILL.md) とほぼ同じだが、
**一次資料としての強度が論文より弱い**点を扱いが違う。

## 手順

### 0. クリッピング

WebFetch で本文を取得し、`docs/raw/articles/{年}-{媒体}-{スラッグ}.md` に保存する。
冒頭に取得元 URL と取得日を必ず書く。Raw は不変なので、要約せず本文をそのまま残す。

### 1. サマリーページ

`docs/wiki/articles/{同名}.md` に書く。Frontmatter は論文ページに準じるが `type: article`、
加えて `reliability` を必ず入れる:

| 値 | 意味 |
|---|---|
| `primary` | 著者本人による解説、公式ドキュメント、一次データを含む |
| `secondary` | 論文の解説記事。原論文を確認するまで断定しない |
| `opinion` | 意見・観測。事実としては引用しない |

### 2. 概念ページへの反映

**`reliability: opinion` の内容を概念ページの `## 横断的知見` に書かない。**
書くなら `## 未解決の問い` に「〜という指摘がある（記事ページへのリンク、未検証）」として置く。

`secondary` の記事から論文の知見を得た場合、その論文のページを `stub: true` で作り、
`source_note` に記事経由であることを書く。原論文を読んだ時点で stub を外す。

### 3〜5

`ingest-paper` の手順 4〜7（双方向リンク / README の目次 / log / 検証）と同じ。
`log.md` の操作名は `ingest-article` とする。
