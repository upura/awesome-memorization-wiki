---
title: Membership inference attacks against machine learning models
authors: [Reza Shokri, Marco Stronati, Congzheng Song, et al.]
year: 2017
venue: IEEE Symposium on Security and Privacy (SP) 2017, pp. 3–18
citekey: Shokri 17
tags: [membership-inference, security, landmark]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Membership inference attacks against machine learning models

## TL;DR

**特定のデータが機械学習モデルの訓練セットに含まれるか否かを予測する**攻撃を定式化した原典。
分類器の構築（shadow model）によるアプローチ。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の起点。言語モデル以前の機械学習一般を対象とする。
[Ishihara 26](ishihara-2026-memorization-survey.md) 1 章で、暗記の定量化に用いられる考え方として最初に挙げられる。

## 手法・実験

**分類器の構築**による攻撃 [Shokri 17, Song 19]。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- 機械学習モデルの出力から、訓練セットへの帰属を推定できる

## 限界・批判

- **大規模な言語モデルを対象にする場合は分類器の学習が現実的ではない**ことが多く、
  指標の算出に基づく手法 [Bentley 20, Choquette-Choo 21, Song 21] が
  一般的になった（サーベイ 3·2§2）。つまり原典の手法は
  言語モデルにはそのまま使えない
- 評価指標として AUC を用いる慣行は [Carlini 22](carlini-2022-first-principles.md) に批判された

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md)
- 言語モデル向けの後継: [Shi 24](shi-2024-min-k-prob.md) / [Duan 24](duan-2024-do-mia-work.md)
- 評価への批判: [Carlini 22](carlini-2022-first-principles.md) / [Das 25](das-2025-blind-baselines.md)
