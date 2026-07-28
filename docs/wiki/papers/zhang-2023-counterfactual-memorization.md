---
title: Counterfactual memorization in neural language models
authors: [Chiyuan Zhang, Daphne Ippolito, Katherine Lee, et al.]
year: 2023
venue: NeurIPS 2023
citekey: Zhang 23
tags: [definition, counterfactual, model]
axis: [モデル]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Counterfactual memorization in neural language models

## TL;DR

反実仮想の概念に基づく暗記の考え方を、ニューラル言語モデルに適用した研究。

## 位置づけ

モデル軸。[Ishihara 26](ishihara-2026-memorization-survey.md) 3·1 節で、
差分プライバシと並ぶ「モデルに着目した定義」の代表として挙げられる。
[Feldman 20](feldman-2020-influence-long-tail.md) の枠組みを言語モデルへ展開したもの。

## 手法・実験

サーベイからは詳細が判明しない（原論文未読）。**要 ingest。**

## 主要な知見

サーベイでの言及は概念的な位置づけにとどまる。**要 ingest。**

## 限界・批判

- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) 全般の課題として、多数のモデルを学習する必要があり
  計算コストが高い

## Wiki 内の接点

- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) / [暗記](../concepts/memorization.md)
- 原典: [Feldman 20](feldman-2020-influence-long-tail.md)
- 共著者が重なる出力軸の研究: [Carlini 23b](carlini-2023-quantifying-memorization.md) / [Ippolito 23](ippolito-2023-false-sense-of-privacy.md)
