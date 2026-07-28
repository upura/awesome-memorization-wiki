---
title: "Memorization without overfitting: Analyzing the training dynamics of large language models"
authors: [Kushal Tirumala, Aram H. Markosyan, Luke Zettlemoyer, et al.]
year: 2022
venue: NeurIPS 2022
citekey: Tirumala 22
tags: [dynamics, overfitting, landmark]
axis: [訓練セット, モデル]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Memorization without overfitting

## TL;DR

大規模言語モデルは**過学習に至る前に**大半のデータを暗記し、その後も情報を忘れにくい。
「暗記 ＝ 過学習」という素朴な等式を訓練ダイナミクスの観測から否定した。

## 位置づけ

訓練セット軸・モデル軸。[暗記](../concepts/memorization.md) の中心命題
「暗記は単なる過学習の副産物ではない」を最も直接的に支える証拠。
サーベイでは 2 章（自己回帰型モデルの参照）と 5·2 節（正則化の限界）で言及される。

## 手法・実験

訓練ダイナミクスの追跡。暗記をトークン単位で議論している点が特徴
（[文字列の類似度](../concepts/string-similarity-memorization.md) の単位の議論）。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- 大規模言語モデルは**過学習前に大半のデータを暗記する**傾向がある
- その後も情報を忘れにくい

## 限界・批判

- サーベイ 5·2 節はこの知見を、正則化による抑制の限界を示す文脈で引く。
  ただし正則化が実際には暗記の抑制に有効とされる報告 [Yeom 18, Zhang 21] とは
  緊張関係にあり、**なぜ効くのかの説明はこの Wiki には無い**
  → [学習過程における抑制](../concepts/mitigation-in-training.md)

## Wiki 内の接点

- [暗記](../concepts/memorization.md) / [学習順と忘却](../concepts/training-order-and-forgetting.md) / [暗記と汎化](../concepts/memorization-vs-generalization.md)
- [学習過程における抑制](../concepts/mitigation-in-training.md)（正則化の限界）
- 学習中の低損失の観測: [Carlini 21](carlini-2021-extracting-training-data.md)
