---
title: Quantifying memorization across neural language models
authors: [Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, et al.]
year: 2023
venue: ICLR 2023
citekey: Carlini 23b
tags: [quantification, scaling, duplication, context-length, landmark]
axis: [訓練セット, モデル, 出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Quantifying memorization across neural language models

## TL;DR

暗記を初めて包括的に定量化し、**文字列の重複・モデルサイズ・文脈長**という
3 因子との強い関連を実証した。**暗記が単なる過学習の副産物ではない**ことを明らかにした論文。

## 位置づけ

3 軸すべてにまたがる。[Ishihara 26](ishihara-2026-memorization-survey.md) 4 章の骨格そのものを提供しており、
本 Wiki では[軸論文](ishihara-2026-memorization-survey.md)に次いで参照が多い。

## 手法・実験

- 対象: 大規模英語コーパス **Pile** [Gao 20] で事前学習された **GPT-Neo 系モデル** [Black 22]
  （125M / 1.3B / 2.7B / 6B の 4 種類）
- 評価: Pile から **50,000 文**を抽出し、重複を解析したうえで、
  文頭を一定トークン長に切り出してプロンプトとした
- 定義: [逐語暗記](../concepts/string-similarity-memorization.md)（続きの生成）

## 主要な知見

1. **[文字列の重複](../concepts/string-duplication.md)** — 重複回数を 2 から 900 までの塊に分けて測定したところ、
   重複が多いほど暗記されやすい
2. **[モデルサイズ](../concepts/model-size.md)** — モデルサイズと暗記量の間に**ほぼ完全な対数線形関係**が存在する
3. **[文脈長](../concepts/context-length.md)** — 文脈長が大きいほど観測される暗記量が増加する

また、デコーディング戦略の違いは実験結果に**大きな影響を与えない**と報告した。

[反実仮想に基づく定義](../concepts/counterfactual-memorization.md)については、
多数のモデルを学習する必要があり**計算コストが高い**ことを課題として指摘している。

## 限界・批判

- 実験は最大 6B パラメータであり、数百 B 規模への外挿は検証されていない
- 英語コーパス（Pile）に限定。日本語では [文脈長](../concepts/context-length.md) の知見が逆転する
  [小柳 24] → [ドメインや言語横断](../concepts/multilingual-and-domain.md)
- デコーディング戦略の影響について [Lee 23] は**逆の結果**（top-k / top-p の方が
  多く抽出する）を報告しており、対立が未解決 → [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md)
- 逐語暗記の定義に基づくが、[Ippolito 23](ippolito-2023-false-sense-of-privacy.md) は
  近似暗記でも同様の結果が得られることを確認した（この点では限界が解消されている）

## Wiki 内の接点

- 3 因子: [文字列の重複](../concepts/string-duplication.md) / [モデルサイズ](../concepts/model-size.md) / [文脈長](../concepts/context-length.md)
- [暗記](../concepts/memorization.md)（暗記 ≠ 過学習の主要な根拠）
- 前身: [Carlini 21](carlini-2021-extracting-training-data.md)
- 定義を緩めた追試: [Ippolito 23](ippolito-2023-false-sense-of-privacy.md)
- 本論文を引用している概念: [逆学習](../concepts/machine-unlearning.md) / [暗記と汎化](../concepts/memorization-vs-generalization.md) / [学習過程における抑制](../concepts/mitigation-in-training.md) / [知識編集](../concepts/knowledge-editing.md)
