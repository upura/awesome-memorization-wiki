---
title: "How much do language models copy from their training data? Evaluating linguistic novelty in text generation using RAVEN"
authors: [R. Thomas McCoy, Paul Smolensky, Tal Linzen, et al.]
year: 2023
venue: Transactions of the Association for Computational Linguistics, Vol. 11, pp. 652–670
citekey: McCoy 23
tags: [novelty, copyright, output]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# How much do language models copy from their training data?（RAVEN）

## TL;DR

生成文の**新規性（novelty）**に着目した分析を実施し、
言語モデルが訓練データからの**大規模な複製**を実施すると報告した。

## 位置づけ

出力軸。[著作権](../concepts/copyright.md)（6·2 節、新規性の欠如による盗用）の主要な証拠。
[文字列の重複](../concepts/string-duplication.md) と [モデルサイズ](../concepts/model-size.md) の知見も支持している。

## 手法・実験

RAVEN という枠組みで、生成テキストの言語的新規性を評価する。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- 言語モデルは訓練データから大規模な複製を実施している
- [文字列の重複](../concepts/string-duplication.md): 重複が多いほど暗記されやすいという知見を支持
- [モデルサイズ](../concepts/model-size.md): モデルサイズが大きいほど暗記されやすいという知見を支持

## 限界・批判

- 「新規性」の指標が、法的な**類似性**の判断とどこまで対応するかは
  この Wiki の未解決の問いである → [著作権](../concepts/copyright.md)
- 剽窃検出の伝統的研究 [Potthast 10, Roy 09] が探究してきた
  多面的な類似性との関係は整理されていない → [研究領域の拡張](../concepts/multimodal-memorization.md)

## Wiki 内の接点

- [著作権](../concepts/copyright.md) / [文字列の類似度](../concepts/string-similarity-memorization.md) / [文字列の重複](../concepts/string-duplication.md) / [モデルサイズ](../concepts/model-size.md)
- [研究領域の拡張](../concepts/multimodal-memorization.md)（剽窃検出との接続）
