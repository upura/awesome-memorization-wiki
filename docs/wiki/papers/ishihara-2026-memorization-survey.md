---
title: "大規模言語モデルの訓練データ暗記の研究動向 (Memorization of Training Data of Large Language Models: A Survey)"
authors: [石原祥太郎, 高橋寛武]
year: 2026
venue: 人工知能学会論文誌 41巻4号 AN40-F（特集論文「人工知能学会設立40周年記念論文」）
citekey: Ishihara 26
doi: 10.1527/tjsai.41-4_AN40-F
url: https://www.jstage.jst.go.jp/article/tjsai/41/4/41_41-4_AN40-F/_article/-char/ja
raw: ../../raw/papers/ishihara-2026-memorization-survey.pdf
tags: [survey, memorization, membership-inference, ai-safety]
axis: [訓練セット, モデル, 出力]
type: paper
role: axis
---

# 大規模言語モデルの訓練データ暗記の研究動向

> **この Wiki の軸となる論文。** 本 Wiki の概念ページはすべて、この論文の
> 訓練セット・モデル・出力という 3 軸（図1）に従って組織されている。
> 新しいソースを ingest するときは、まずこのページの体系に位置づけること。

## TL;DR

約 180 件の既存研究を、**訓練セット・モデル・出力**という 3 軸で整理した日本語サーベイ。
暗記が単なる過学習の副産物ではなく、**文字列の重複・モデルサイズ・文脈長**に依存する
現象であることを軸に、定義と定量化（3章）→ 実証的知見（4章）→ 抑制（5章）→
社会的課題（6章）→ 展望（7章）という一連の流れを体系化する。
2023 年の [Ishihara 23](ishihara-2023-training-data-extraction-survey.md) の発展版。

## 位置づけ

3 軸すべてを扱う唯一のページ。他のサーベイとの差分は本論文自身が明示している。

| 既存サーベイ | 差分 |
|---|---|
| [Satvaty 24](satvaty-2024-undesirable-memorization.md)（意図せぬ暗記）<br>[Meeus 25], [Wu 25]（メンバーシップ推論） | 話題を絞っている。本論文は攻撃やメンバーシップ推論**以外**の定量化手法も含めて幅広く扱う |
| [Cheng 25b], [Kaneko 25a], [Ravaut 25], [Xu 24]（モデル評価の正当性） | 本論文はモデル評価を「暗記がもたらす課題の一つ」と位置づけ、より広い視点で整理する |
| [Wei 25]（機械学習一般の暗記）<br>[Hu 22b]（メンバーシップ推論全般） | 対象が広い。本論文は**言語モデルに絞る**ことで端的かつ横断的な整理を実現した |

対象は Transformer [Vaswani 17] を基盤とした**自己回帰型**の言語モデル。
BERT のようなマスク型モデルの暗記は 7章の議論にとどめている。
また 3〜5 章では原則として**事後学習前のベースモデル**を扱う（派生モデルの共通基盤であり、
事後学習の設定差による変動を切り分けるため）。

## 体系（図1）

3 段階の軸に、定量化・実証的知見・抑制を対応させたのが本論文の骨格である。

| 軸 | 3章 定量化 | 4章 実証的知見 | 5章 抑制 |
|---|---|---|---|
| **訓練セット** | — | [文字列の重複](../concepts/string-duplication.md) (4·1) | [重複排除](../concepts/deduplication.md)・データの削除 (5·1 前処理) |
| **モデル** | [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) (3·1§1)<br>[差分プライバシ](../concepts/differential-privacy.md) (3·1§2) | [モデルサイズ](../concepts/model-size.md) (4·2) | [学習過程における抑制](../concepts/mitigation-in-training.md) (5·2 学習)<br>差分プライバシ、正則化、[逆学習](../concepts/machine-unlearning.md)、[知識編集](../concepts/knowledge-editing.md)、知識蒸留、PEFT、連合学習 |
| **出力** | [文字列の類似度](../concepts/string-similarity-memorization.md) (3·2§1)<br>[メンバーシップ推論](../concepts/membership-inference.md) (3·2§2)<br>[知識を問うタスク](../concepts/knowledge-probing.md) (3·2§3) | [文脈長](../concepts/context-length.md) (4·3) | [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md) (5·3 後処理) |

6章の課題: [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) (6·1)・[著作権](../concepts/copyright.md) (6·2)・[データセット汚染](../concepts/data-contamination.md) (6·3)
7章の展望: [評価の枠組み](../concepts/evaluation-framework.md) (7·1)・[ドメインや言語横断](../concepts/multilingual-and-domain.md) (7·2)・[研究領域の拡張](../concepts/multimodal-memorization.md) (7·3)

## 手法・実験

サーベイ論文であり独自実験は無い。ただし 4 章の骨格は
[Carlini 23b](carlini-2023-quantifying-memorization.md) の実験設定に依拠している:
大規模英語コーパス Pile [Gao 20] で事前学習された GPT-Neo 系モデル [Black 22]
（125M / 1.3B / 2.7B / 6B の 4 種類）に対し、Pile から 50,000 文を抽出し、
重複を解析したうえで文頭を一定トークン長に切り出してプロンプトとする。

評価セットの構築手法は 2 種類が図示されている（図2・図3）。両者とも
訓練セットから一部を抽出し、冒頭の数トークンを抜粋する点は共通する。
これは[抽出時のバイアス](../concepts/evaluation-framework.md)という 7·1 節の論点に直結する。

- **図2 続きの生成**: 訓練データを分割し、冒頭をプロンプト、後続を参照用として類似度を測る
- **図3 メンバーシップ推論**: 訓練セットからの抽出を正例、訓練セット外のテキストを負例とする

## 主要な知見

### 定義は一枚岩ではない（3章）

暗記の定義は「着目する対象が**学習時のモデル**か、**推論時の出力**か」で大別される。
多くの研究は素朴に[文字列の類似度](../concepts/string-similarity-memorization.md)に着目するが、
[反実仮想](../concepts/counterfactual-memorization.md)や[差分プライバシ](../concepts/differential-privacy.md)に
基づく定義もあり、[メンバーシップ推論](../concepts/membership-inference.md) や[知識を問うタスク](../concepts/knowledge-probing.md)も使われる。

### 3 つの実証的知見（4章）

[Carlini 23b](carlini-2023-quantifying-memorization.md) が示し、後続研究で広く再現された 3 点。

1. **[文字列の重複](../concepts/string-duplication.md)**: 重複回数を 2〜900 の塊に分けて測定すると、重複が多いほど暗記されやすい
2. **[モデルサイズ](../concepts/model-size.md)**: モデルサイズと暗記量の間にほぼ完全な**対数線形関係**が存在する
3. **[文脈長](../concepts/context-length.md)**: 文脈長が大きいほど観測される暗記量が増加する

加えて**学習順の影響**（学習の後半に用いられたテキストの方が暗記されやすい）が
[Duan 24], [Huang 24], [Satvaty 25], [Jagielski 23] で観測されている。
これは暗記と忘却が**並行して発生している**ことを示唆する
（[学習順と忘却](../concepts/training-order-and-forgetting.md)）。

### 抑制は 3 段階に分類できる（5章）

前処理（訓練セット）/ 学習（モデル）/ 後処理（推論）。この分類は
[Hu 22b], [Huang 22a], [Jagielski 23], [Sakarvadia 25] を参考に再構成されたもの。
**どの段階の手法も単独では完全ではない**——たとえば重複排除は有効だが、
重複以外の要因でも暗記は発生し得るため、それだけでは防げない。

### 暗記は常に排除すべき対象ではない（7·1）

本論文の規範的な主張として最も重要な一文。実用上は一定の知識保持が有用に働く場合があり
（公開事実の想起、特定ドメインの定型表現の再現など）、
**許容可能な暗記と深刻度の高い暗記を区別する必要がある**。
[Lee 20] は既存研究の多くが暗記された文字列の危険性の程度を区別していないと指摘した。

## 限界・批判

- サーベイの性質上、4 章の実証的知見は**英語を中心とする研究**に強く依拠している。
  日本語を含むその他の条件における検証は十分でないと本論文自身が 7·2 節で認めている。
- 3〜5 章は事後学習前のベースモデルを対象とするが、
  近年の実用モデルは事後学習を前提としており、事後学習が出力の傾向に影響を与える点に
  注意が必要だと本論文自身が留保している。ChatGPT / GPT-4 のような事後学習済みモデルの
  暗記は [Chang 23] などに限られる。
- 統一的な分類法とベンチマークの確立は「今後の方向性」として提示された段階であり、
  本論文が提供するものではない。

## Wiki 内の接点

このページはハブである。全概念ページからリンクが返ってくる。

- 暗記の定義全体: [暗記](../concepts/memorization.md)
- 前身: [Ishihara 23](ishihara-2023-training-data-extraction-survey.md)
- 4章の骨格を提供: [Carlini 23b](carlini-2023-quantifying-memorization.md)
- 日本語での検証: [Kiyomaru 24](kiyomaru-2024-comprehensive-analysis.md) / [Ishihara 24](ishihara-2024-japanese-newspaper.md) / [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md)
- 評価の枠組みへの批判: [評価の枠組み](../concepts/evaluation-framework.md)
- 本論文を引用している概念: [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [暗記と汎化](../concepts/memorization-vs-generalization.md)
