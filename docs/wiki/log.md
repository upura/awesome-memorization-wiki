---
title: log
type: log
---

# log

操作履歴。**追記のみ。過去行は書き換えない。**

| 日時 | 操作 | 内容 |
|---|---|---|
| 2026-07-29 06:16 | setup | スキーマ定義（`CLAUDE.md`）と skills 4 種（ingest-paper / ingest-article / query / lint）を作成。ディレクトリ構成を初期化 |
| 2026-07-29 06:20 | ingest-paper | 軸論文を取り込み: [Ishihara 26](papers/ishihara-2026-memorization-survey.md)（人工知能学会論文誌 41(4) AN40-F）。`pdftotext -enc UTF-8` で本文抽出（pypdf は CID フォントで文字化けした） |
| 2026-07-29 06:30 | ingest-paper | 概念ページ 23 件を新規作成。サーベイ図1 の 3 軸（訓練セット・モデル・出力）に沿って組織: [暗記](concepts/memorization.md) [暗記と汎化](concepts/memorization-vs-generalization.md) [評価の枠組み](concepts/evaluation-framework.md) [反実仮想に基づく定義](concepts/counterfactual-memorization.md) [差分プライバシ](concepts/differential-privacy.md) [文字列の類似度](concepts/string-similarity-memorization.md) [メンバーシップ推論](concepts/membership-inference.md) [知識を問うタスク](concepts/knowledge-probing.md) [評価セットとライブラリ](concepts/benchmarks-and-tools.md) [文字列の重複](concepts/string-duplication.md) [モデルサイズ](concepts/model-size.md) [文脈長](concepts/context-length.md) [学習順と忘却](concepts/training-order-and-forgetting.md) [重複排除](concepts/deduplication.md) [学習過程における抑制](concepts/mitigation-in-training.md) [逆学習](concepts/machine-unlearning.md) [知識編集](concepts/knowledge-editing.md) [出力の制御と電子透かし](concepts/output-control-and-watermarking.md) [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md) [著作権](concepts/copyright.md) [データセット汚染](concepts/data-contamination.md) [ドメインや言語横断](concepts/multilingual-and-domain.md) [研究領域の拡張](concepts/multimodal-memorization.md) |
| 2026-07-29 06:45 | ingest-paper | 論文ページ 24 件を stub として作成（サーベイ経由・原論文未読）。主要な引用キーを `citekey` に保持 |
| 2026-07-29 06:55 | query | Filed [3 因子は日本語で再現するか](queries/2026-07-29-3-factors-robustness-across-languages.md)、[ドメインや言語横断](concepts/multilingual-and-domain.md) の横断的知見に還元 |
| 2026-07-29 06:58 | query | Filed [攻撃の失敗を成功指標にできるか](queries/2026-07-29-attack-failure-is-not-success.md)、[評価の枠組み](concepts/evaluation-framework.md) と [著作権](concepts/copyright.md) の横断的知見に還元 |
| 2026-07-29 07:00 | lint | 自動修正: 必須セクション `## 主要な論文` 欠落 5 件を追加（[評価セットとライブラリ](concepts/benchmarks-and-tools.md) [評価の枠組み](concepts/evaluation-framework.md) [学習過程における抑制](concepts/mitigation-in-training.md) [ドメインや言語横断](concepts/multilingual-and-domain.md) [研究領域の拡張](concepts/multimodal-memorization.md)）。片方向リンク 16 件に返リンクを追加。根拠 1 本だった [知識編集](concepts/knowledge-editing.md) に [Carlini 23b](papers/carlini-2023-quantifying-memorization.md) を接続 |
| 2026-07-29 07:02 | lint | 検証結果: 全 52 ページ、壊れたリンク 0 / 孤立ページ 0 / 片方向リンク 0 / 必須セクション欠落 0。stub 24 件と知識ギャップ 5 件を [README](../../README.md) 末尾に記録 |
| 2026-07-29 08:10 | publish | GitHub Pages で公開する構成に移行。`vault/` を `docs/` に移し、Obsidian の `[[wikilink]]` 52 ファイルを相対リンクへ変換。`index.md` は `README.md` に統合（サイトのトップページを兼ねるため）。Jekyll 設定（`_config.yml` / `_layouts/default.html`）、デプロイと lint の GitHub Actions、`tools/verify_wiki.py` を追加。一次資料の PDF は出版社の権利のため `.gitignore` |
| 2026-07-29 10:20 | publish | <https://upura.github.io/awesome-memorization-wiki/> で公開。GitHub Actions（デプロイと lint）を追加し、Pages の build type を workflow に切り替え。frontmatter 4 件の YAML 不正（コロンの引用符漏れ）を修正し、同種の事故を `tools/verify_wiki.py` の検査項目に追加した（1 件でもサイト全体のビルドが落ちるため） |
| 2026-07-30 09:00 | setup | [未解決の問い（研究アジェンダ）](questions.md)と[対立の台帳](conflicts.md)を新設。105 件の問いを A 文献調査 / B 実験 / C 枠組み に分類。`verify_wiki.py` に stub の被参照数レポートを追加 |
| 2026-07-31 11:30 | ingest-paper | [Carlini 23b](papers/carlini-2023-quantifying-memorization.md) を原典から再取り込み（stub 解消、11 概念ページが依存）。追試節の知見を反映し [文字列の重複](concepts/string-duplication.md) の主張を訂正、[対立の台帳](conflicts.md) 2 番を解消・8 番を新設 |
| 2026-07-31 12:10 | ingest-paper | [Ippolito 23](papers/ippolito-2023-false-sense-of-privacy.md) を原典から再取り込み。MemFree の実装と 2 つの失敗経路、近似定義での過小評価を反映 |
| 2026-07-31 12:40 | ingest-paper | [Das 25](papers/das-2025-blind-baselines.md) を原典から再取り込み。8 データセットへの拡大と、[Panaitescu-Liess 25] の名指し批判を反映。[評価の枠組み](concepts/evaluation-framework.md)・[出力の制御と電子透かし](concepts/output-control-and-watermarking.md)・[著作権](concepts/copyright.md)・[Query](queries/2026-07-29-attack-failure-is-not-success.md) に留保を追記 |
| 2026-07-31 13:20 | ingest-paper | [Brown 22](papers/brown-2022-what-does-it-mean-privacy.md)・[Carlini 21](papers/carlini-2021-extracting-training-data.md) を原典から再取り込み。k-eidetic による危険度のスペクトラム化を反映し、[評価の枠組み](concepts/evaluation-framework.md) の [Lee 20] 批判に留保を追加 |
| 2026-07-31 13:30 | lint | 検査通過。stub は 24 → 19 本。片方向リンク 3 件を修正 |
