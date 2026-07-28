---
title: Deduplicating training data makes language models better
authors: [Katherine Lee, Daphne Ippolito, Andrew Nystrom, et al.]
year: 2022
venue: "ACL 2022 (Volume 1: Long Papers), pp. 8424–8445"
citekey: Lee 22
tags: [mitigation, deduplication, training-set]
axis: [訓練セット]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Deduplicating training data makes language models better

## TL;DR

訓練セットの**重複排除**が言語モデルを良くする。暗記の抑制と性能向上を両立させうる、
最も実用的な緩和策。

## 位置づけ

訓練セット軸の前処理（[Ishihara 26](ishihara-2026-memorization-survey.md) 5·1）。
実証的知見の[文字列の重複](../concepts/string-duplication.md)（4·1）に対応する抑制手法。

## 手法・実験

暗記の測定に**トークン一致率**を用いた（[文字列の類似度](../concepts/string-similarity-memorization.md)）。
サーベイからは重複排除アルゴリズムの詳細は判明しない（原論文未読）。

## 主要な知見

- 重複排除は暗記の緩和に有効である [Allamanis 19, Kandpal 22, Lee 22]
- モデル学習に比べ効率的であり、実用的な解決策として期待されている

## 限界・批判

- **重複以外の要因でも暗記は発生し得るため、重複排除のみで完全に防ぐことはできない**
  （サーベイ 5·1 の明示的な留保）
- 前処理は 4 章の 3 因子のうち[重複](../concepts/string-duplication.md)しか動かせない。
  [モデルサイズ](../concepts/model-size.md) と [文脈長](../concepts/context-length.md) には触れない → [重複排除](../concepts/deduplication.md)
- [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) で整理したとおり、
  守るべき機密情報は**重複が少ない外れ値**の側にあることが多く、
  重複排除は最も守るべきデータには効きにくい

## Wiki 内の接点

- [重複排除](../concepts/deduplication.md) / [文字列の重複](../concepts/string-duplication.md)
- プライバシ観点での姉妹研究: [Kandpal 22](kandpal-2022-deduplicating-privacy.md)
- 日本語での再現: [Ishihara 24](ishihara-2024-japanese-newspaper.md) / [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md)
