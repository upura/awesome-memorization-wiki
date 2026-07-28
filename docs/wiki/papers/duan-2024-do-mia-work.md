---
title: Do membership inference attacks work on large language models?
authors: [Michael Duan, Anshuman Suri, Niloofar Mireshghallah, et al.]
year: 2024
venue: Conference on Language Modeling (COLM) 2024
citekey: Duan 24
tags: [membership-inference, critique, benchmark, dynamics]
axis: [出力, 訓練セット]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Do membership inference attacks work on large language models?

## TL;DR

大規模言語モデルに対してメンバーシップ推論が本当に機能するのかを正面から問い、
評価セット **MIMIR**（よりランダムな分割）を提供した。
あわせて**暗記と忘却が並行して発生している**ことを指摘。

## 位置づけ

出力軸（メンバーシップ推論の批判的再検討）と訓練セット軸（学習ダイナミクス）にまたがる。
[Shi 24](shi-2024-min-k-prob.md) の WikiMIA が抱える分布差問題への応答の一つ。

## 手法・実験

**MIMIR**: よりランダムな設定でデータセットを分割した評価セット。
メンバーシップ推論の手法を整備したライブラリとしても公開されている。

## 主要な知見

- メンバーシップ推論の有効性は、評価セットの構成に強く依存する
- **学習の後半に用いられたテキストの方が暗記されやすい**（学習順の影響）。
  これは訓練セット内の訓練データで学習していく上で、
  **暗記と忘却が並行して発生している**ことを示唆する → [学習順と忘却](../concepts/training-order-and-forgetting.md)
- 大規模言語モデルの事前学習では大きな**バッチサイズ**が一般的だが、
  これも暗記の保持に寄与していると見なせる。
  バッチサイズが大きいほど学習ステップ数は小さく、
  学習ステップ単位で見ると忘却の機会が減少していると解釈できる可能性がある

## 限界・批判

- バッチサイズと暗記保持の関係は解釈であり、直接検証されていない
  （サーベイも「解釈できる可能性がある」と留保している）
- MIMIR がランダム分割を採用しても、正例・負例を得る根本的な制約
  （訓練セット外のテキストをどう大量に集めるか）は残る → [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)
- [学習順と忘却](../concepts/training-order-and-forgetting.md) / [文字列の重複](../concepts/string-duplication.md)
- 批判対象: [Shi 24](shi-2024-min-k-prob.md)
- 同方向の批判: [Das 25](das-2025-blind-baselines.md) / [Chen 25](chen-2025-revisiting-mia.md)
