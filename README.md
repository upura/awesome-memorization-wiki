# Awesome Memorization Wiki

大規模言語モデル（LLM）の **Memorization（訓練データの暗記）** に関する日本語の非公式リンク集です。
定義・定量化手法・実証的知見・抑制手法・社会的課題を、話題ごとにまとめています。

本サイトの特徴は、**LLM Wiki** として運用している点です。
次のサーベイ論文を軸とし、LLM が話題ごとの知見の統合と相互リンクを維持しています。

> 石原祥太郎, 高橋寛武「[大規模言語モデルの訓練データ暗記の研究動向](https://www.jstage.jst.go.jp/article/tjsai/41/4/41_41-4_AN40-F/_article/-char/ja)」
> 人工知能学会論文誌 41巻4号 AN40-F (2026). DOI: [10.1527/tjsai.41-4_AN40-F](https://doi.org/10.1527/tjsai.41-4_AN40-F)

サーベイが提示する **訓練セット・モデル・出力**という 3 軸（同論文 図1）を、
そのままページの組織原理として採用しています。
新しい資料を取り込むときは、必ずこの 3 軸のどこに位置づくかを明示します。

構築の方針は [tsurubee さんの「LLM Wiki：知識を繋げる」](https://zenn.dev/tsurubee/articles/llm-wiki-connecting-knowledge)を参考にしています。
「質問のたびに知識をゼロから再発見する」RAG ではなく、繋がりが永続的に蓄積される知識ベースを目指しています。

## 最近の更新

直近の更新の抜粋です（全履歴は[操作ログ](./docs/wiki/log.md)）。

- 2026-07-31: [Morris+ (ICML 2026)](./docs/wiki/papers/morris-2026-how-much-memorize.md) を ingest（サーベイのカットオフ以降の研究）。[対立の台帳](./docs/wiki/conflicts.md) 4 番が「両立する」に決着
- 2026-07-31: 被参照数トップの 5 本（[Carlini 23b](./docs/wiki/papers/carlini-2023-quantifying-memorization.md)・[Ippolito 23](./docs/wiki/papers/ippolito-2023-false-sense-of-privacy.md)・[Das 25](./docs/wiki/papers/das-2025-blind-baselines.md)・[Brown 22](./docs/wiki/papers/brown-2022-what-does-it-mean-privacy.md)・[Carlini 21](./docs/wiki/papers/carlini-2021-extracting-training-data.md)）を原典から読み直し、stub を解消。[対立の台帳](./docs/wiki/conflicts.md)が 1 件解消・1 件追加
- 2026-07-30: [未解決の問い（研究アジェンダ）](./docs/wiki/questions.md)と[対立の台帳](./docs/wiki/conflicts.md)を新設
- 2026-07-29: サーベイ論文を軸に Wiki を初期構築。概念ページ 23 件・論文ページ 25 件・Query 2 件

## 目次

話題ごとに、概念ページ（定義・主要な論文・横断的知見・未解決の問い）を案内します。

> **はじめて読む方へ**: [暗記とは何か](./docs/wiki/concepts/memorization.md) →
> [軸となるサーベイ](./docs/wiki/papers/ishihara-2026-memorization-survey.md) →
> 関心のある軸の概念ページ、の順に読むと全体像が掴めます。

### 横断ページ

- [**未解決の問い（研究アジェンダ）**](./docs/wiki/questions.md): 概念ページに散在する 105 件の問いを「何が来れば決着するか」で分類。会議 sweep の検索クエリを兼ねる
- [**対立の台帳**](./docs/wiki/conflicts.md): 結論が食い違う 8 件を、どちらも消さずに整理。各項目に決着させる実験を併記（うち 1 件は原典を読んで解消済み）
- [操作ログ](./docs/wiki/log.md): 全更新履歴

### 軸：訓練セット・モデル・出力

| 軸 | 定量化（3章） | 実証的知見（4章） | 抑制（5章） |
|---|---|---|---|
| **訓練セット** | — | [文字列の重複](./docs/wiki/concepts/string-duplication.md)<br>[学習順と忘却](./docs/wiki/concepts/training-order-and-forgetting.md) | [重複排除](./docs/wiki/concepts/deduplication.md) |
| **モデル** | [反実仮想](./docs/wiki/concepts/counterfactual-memorization.md)<br>[差分プライバシ](./docs/wiki/concepts/differential-privacy.md) | [モデルサイズ](./docs/wiki/concepts/model-size.md) | [学習過程での抑制](./docs/wiki/concepts/mitigation-in-training.md)<br>[逆学習](./docs/wiki/concepts/machine-unlearning.md)<br>[知識編集](./docs/wiki/concepts/knowledge-editing.md) |
| **出力** | [文字列の類似度](./docs/wiki/concepts/string-similarity-memorization.md)<br>[メンバーシップ推論](./docs/wiki/concepts/membership-inference.md)<br>[知識を問うタスク](./docs/wiki/concepts/knowledge-probing.md) | [文脈長](./docs/wiki/concepts/context-length.md) | [出力の制御・電子透かし](./docs/wiki/concepts/output-control-and-watermarking.md) |

課題（6章）: [セキュリティ](./docs/wiki/concepts/security-and-privacy-leakage.md)・[著作権](./docs/wiki/concepts/copyright.md)・[評価の正当性](./docs/wiki/concepts/data-contamination.md)
展望（7章）: [評価の枠組み](./docs/wiki/concepts/evaluation-framework.md)・[ドメインや言語横断](./docs/wiki/concepts/multilingual-and-domain.md)・[研究領域の拡張](./docs/wiki/concepts/multimodal-memorization.md)

### 核となる概念

- [暗記（Memorization）](./docs/wiki/concepts/memorization.md): 暗記とは何か。定義が一枚岩でないことと、目的による使い分け
- [暗記と汎化の境界](./docs/wiki/concepts/memorization-vs-generalization.md): この分野で最も未解決な問い
- [現実の問題に即した評価の枠組み](./docs/wiki/concepts/evaluation-framework.md): 「何を測っているか」の宣言が要る理由。方法論のハブ

### 定義と定量化手法（3章）

- [反実仮想に基づく定義](./docs/wiki/concepts/counterfactual-memorization.md): 損失差分による定義。理論的に素直だが計算コストが高い
- [差分プライバシ](./docs/wiki/concepts/differential-privacy.md): 学習アルゴリズムに着目。定義でもあり抑制手法でもある
- [文字列の類似度（逐語暗記・近似暗記）](./docs/wiki/concepts/string-similarity-memorization.md): 事実上の標準となっている定義
- [メンバーシップ推論](./docs/wiki/concepts/membership-inference.md): 訓練セットが未知のときの主力。方法論的批判が集中している
- [知識を問うタスク](./docs/wiki/concepts/knowledge-probing.md): 閉じた実用モデルを調べる唯一の窓
- [評価セットとライブラリ](./docs/wiki/concepts/benchmarks-and-tools.md): WikiMIA・MIMIR・Fast-MIA と、評価セットの壊れ方

### 実証的知見（4章）

- [文字列の重複](./docs/wiki/concepts/string-duplication.md): 重複が多いほど暗記されやすい。最も頑健な因子
- [モデルサイズ](./docs/wiki/concepts/model-size.md): ほぼ完全な対数線形関係。性能の副産物かもしれない
- [文脈長](./docs/wiki/concepts/context-length.md): 発見可能性の現象。日本語での「逆転」は**設定依存だと判明**（2026-07-31 訂正）
- [学習順と忘却](./docs/wiki/concepts/training-order-and-forgetting.md): 重複の効果を説明する機構

### 暗記の抑制（5章）

- [重複排除・データの削除](./docs/wiki/concepts/deduplication.md): 前処理。最も実用的だが 3 因子のうち 1 つしか動かせない
- [学習過程における抑制](./docs/wiki/concepts/mitigation-in-training.md): 正則化・知識蒸留・PEFT・連合学習
- [逆学習](./docs/wiki/concepts/machine-unlearning.md): 事後に発生した削除要求に応えられる唯一の層
- [知識編集](./docs/wiki/concepts/knowledge-editing.md): 「暗記はモデルのどこに宿るか」を問う系統
- [出力の制御と電子透かし](./docs/wiki/concepts/output-control-and-watermarking.md): 後処理。本 Wiki で最も懐疑的に扱われる層

### 暗記にまつわる課題（6章）

- [セキュリティと情報漏洩](./docs/wiki/concepts/security-and-privacy-leakage.md): 訓練データ抽出・データポイズニング・忘れられる権利
- [著作権の侵害](./docs/wiki/concepts/copyright.md): 依拠性と類似性。立証経路が両側から塞がれている
- [データセット汚染と評価の正当性](./docs/wiki/concepts/data-contamination.md): 塊で測れば信頼できるという逆説

### 今後の展望（7章）

- [ドメインや言語横断での分析](./docs/wiki/concepts/multilingual-and-domain.md): 日本語・低資源言語・ドメイン特化。本 Wiki 最大の知識ギャップ
- [研究領域の拡張](./docs/wiki/concepts/multimodal-memorization.md): 画像・音声・剽窃検出・モデル反転攻撃への接続

## 論文ページ

各論文の要約と、Wiki 内のどの概念と繋がるかをまとめています。

### 軸・サーベイ

- [大規模言語モデルの訓練データ暗記の研究動向](./docs/wiki/papers/ishihara-2026-memorization-survey.md) (石原・高橋, 2026): **本 Wiki の軸**。約 180 件を 3 軸で体系化
- [Training data extraction from pre-trained language models: A survey](./docs/wiki/papers/ishihara-2023-training-data-extraction-survey.md) (Ishihara, 2023): 上記の前身
- [Undesirable memorization in large language models: A survey](./docs/wiki/papers/satvaty-2024-undesirable-memorization.md) (Satvaty+, 2024): 意図せぬ暗記のサーベイ

### 定量化の原典

- [Extracting training data from large language models](./docs/wiki/papers/carlini-2021-extracting-training-data.md) (Carlini+, 2021): GPT-2 から個人情報が抽出できる。分野の起点
- [Quantifying memorization across neural language models](./docs/wiki/papers/carlini-2023-quantifying-memorization.md) (Carlini+, 2023): 3 因子を実証。サーベイ 4 章の骨格
- [What neural networks memorize and why](./docs/wiki/papers/feldman-2020-influence-long-tail.md) (Feldman+, 2020): 反実仮想に基づく定義の原典
- [Counterfactual memorization in neural language models](./docs/wiki/papers/zhang-2023-counterfactual-memorization.md) (Zhang+, 2023): 反実仮想を言語モデルへ
- [Membership inference attacks against machine learning models](./docs/wiki/papers/shokri-2017-membership-inference.md) (Shokri+, 2017): メンバーシップ推論の原典
- [Detecting pretraining data from large language models](./docs/wiki/papers/shi-2024-min-k-prob.md) (Shi+, 2024): Min-K% Prob と WikiMIA。標準であり批判の的
- [Speak, memory: An archaeology of books known to ChatGPT/GPT-4](./docs/wiki/papers/chang-2023-speak-memory.md) (Chang+, 2023): 事後学習済みモデルを扱う数少ない例
- [How much do language models memorize?](./docs/wiki/papers/morris-2026-how-much-memorize.md) (Morris+, 2026): 容量 3.6 bits/param。暗記と汎化を情報理論的に分離

### 方法論への批判

- [Membership inference attacks from first principles](./docs/wiki/papers/carlini-2022-first-principles.md) (Carlini+, 2022): AUC では不十分。低偽陽性率での真陽性率を
- [Blind baselines beat membership inference attacks](./docs/wiki/papers/das-2025-blind-baselines.md) (Das+, 2025): 盲目的ベースラインが既存手法を上回る
- [A statistical and multi-perspective revisiting of the MIA](./docs/wiki/papers/chen-2025-revisiting-mia.md) (Chen+, 2025): 包括的な実証再検討
- [Do membership inference attacks work on large language models?](./docs/wiki/papers/duan-2024-do-mia-work.md) (Duan+, 2024): MIMIR を提供。暗記と忘却の並行
- [MIAs cannot prove that a model was trained on your data](./docs/wiki/papers/zhang-2025-mia-cannot-prove.md) (Zhang+, 2025): 「証明できない」という立場表明
- [What does it mean for a language model to preserve privacy?](./docs/wiki/papers/brown-2022-what-does-it-mean-privacy.md) (Brown+, 2022): プライバシは文脈依存。形式的定義の限界
- [Preventing verbatim memorization gives a false sense of privacy](./docs/wiki/papers/ippolito-2023-false-sense-of-privacy.md) (Ippolito+, 2023): 逐語フィルタは偽りの安心感

### 実証・抑制

- [Memorization without overfitting](./docs/wiki/papers/tirumala-2022-memorization-without-overfitting.md) (Tirumala+, 2022): 過学習前に暗記が起きる
- [Deduplicating training data makes language models better](./docs/wiki/papers/lee-2022-deduplicating.md) (Lee+, 2022): 重複排除は言語モデルを良くする
- [Deduplicating training data mitigates privacy risks](./docs/wiki/papers/kandpal-2022-deduplicating-privacy.md) (Kandpal+, 2022): 重複排除はプライバシリスクを緩和する
- [How much do language models copy from their training data?](./docs/wiki/papers/mccoy-2023-raven.md) (McCoy+, 2023): 生成文の新規性。大規模な複製の報告

### 日本語・多言語

- [A comprehensive analysis of memorization in LLMs](./docs/wiki/papers/kiyomaru-2024-comprehensive-analysis.md) (Kiyomaru+, 2024): 日本語で英語の知見が再現される
- [Quantifying memorization ... using Japanese newspaper](./docs/wiki/papers/ishihara-2024-japanese-newspaper.md) (Ishihara+, 2024): 日本語新聞記事での定量化。**3 因子すべてを日本語で再現**
- [Fast-MIA: Efficient and scalable membership inference for LLMs](./docs/wiki/papers/takahashi-2025-fast-mia.md) (Ishihara+, 2025): 評価を効率化するライブラリ
- [Quantifying memorization in continual pre-training with Japanese corpora](./docs/wiki/papers/takahashi-2025-continual-pretraining-japanese.md) (Takahashi+, 2025): 継続事前学習。文脈長で反例
- [Memorization is language-sensitive](./docs/wiki/papers/satvaty-2025-language-sensitive.md) (Satvaty+, 2025): 低資源言語ほど推論されやすい

## Query

複数のページを突き合わせて初めて見えた繋がりを、質問の形でファイリングしています。

- [暗記の 3 因子のうち、日本語で崩れるのはどれか](./docs/wiki/queries/2026-07-29-3-factors-robustness-across-languages.md)
- [「メンバーシップ推論が効かなくなった」を抑制手法の成功指標にしてよいか](./docs/wiki/queries/2026-07-29-attack-failure-is-not-success.md)

## この Wiki の設計方針

- **概念ページに「横断的知見」と「未解決の問い」を必須にしています。**
  1 本の論文だけから言えることは横断的知見に書きません。ここが Wiki の心臓部であり、
  空になっているページは「繋げ損ねている」サインとして lint が検出します。
- **矛盾を消しません。** [文脈長](./docs/wiki/concepts/context-length.md)は英語と日本語で結論が逆転していますが、
  どちらかを採用せず両論を残し、[対立の台帳](./docs/wiki/conflicts.md)に「どの条件差が効いているか」と
  「何をすれば決着するか」を記録しています。
- **未解決の問いを研究アジェンダとして公開しています。**
  [105 件の問い](./docs/wiki/questions.md)を、文献調査で閉じうるもの / 実験が要るもの /
  枠組みの問題、に分類しています。
- **原論文を読んでいない論文ページは frontmatter に `stub: true` と明記しています。**
  現在 19 本が stub（サーベイ経由の記述）です。被参照数の多い順に解消しています。

## 現時点で最大の知識ギャップ

1. **日本語での抑制手法の有効性** — 定量化の日本語検証は複数あるが、
   [重複排除](./docs/wiki/concepts/deduplication.md)・[学習過程での抑制](./docs/wiki/concepts/mitigation-in-training.md)・[出力の制御](./docs/wiki/concepts/output-control-and-watermarking.md)の
   有効性を日本語で確認した研究が本 Wiki には無い
2. **信号が弱い設定（AUC ≒ 0.5）での[文脈長](./docs/wiki/concepts/context-length.md)の減少はノイズか実効果か** — 原論文の数値に当たって初めて立った問い
3. **日本語の標準ベンチマーク** — WikiMIA・MIMIR に相当するものが無い
4. **抑制手法を測定手法と独立に検証する方法論** — [評価の枠組み](./docs/wiki/concepts/evaluation-framework.md)を参照
5. **原論文未読の stub が 24 本** — 特に [Zhang 23](./docs/wiki/papers/zhang-2023-counterfactual-memorization.md) と
   [Ishihara 23](./docs/wiki/papers/ishihara-2023-training-data-extraction-survey.md) は主要な知見が空欄

## 開発

```
CLAUDE.md                 # スキーマ定義（命名規約・frontmatter・必須セクション・運用ルール）
.claude/skills/           # ingest-paper / ingest-article / query / lint
tools/verify_wiki.py      # リンク・必須セクション・双方向リンクの検査
docs/raw/                 # 一次資料（PDF は Git 管理外）
docs/wiki/                # Wiki 本体。Obsidian Vault としても開ける
```

Claude Code をこのディレクトリで起動してスキルを呼びます。

```
> /ingest-paper https://arxiv.org/abs/XXXX.XXXXX
> /query 日本語で重複排除は有効か？
> /lint
```

検査は手元でも実行できます（CI でも走ります）。

```sh
python3 tools/verify_wiki.py
```

日本語 PDF の本文抽出には poppler の `pdftotext -enc UTF-8` を使ってください
（pypdf は CID フォントで文字化けします）。

```sh
brew install poppler
```

## ライセンス

本リポジトリのコンテンツは [MIT License](./LICENSE) で提供します。
`docs/raw/` に置く一次資料（論文 PDF 等）は各出版社の権利に従うため、Git 管理外としています。
