---
title: Membership inference attacks from first principles
authors: [Nicholas Carlini, Steve Chien, Milad Nasr, et al.]
year: 2022
venue: IEEE Symposium on Security and Privacy (SP) 2022, pp. 1897–1914
citekey: Carlini 22
tags: [membership-inference, evaluation, metrics]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Membership inference attacks from first principles

## TL;DR

メンバーシップ推論の**評価指標は現実的な攻撃シナリオを反映すべき**だと主張し、
AUC などの正確性に関する直接的な指標だけでは不十分で、
**低い偽陽性率における真陽性率**を評価すべきだと提案した。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の手法そのものではなく、
**手法の評価のしかた**を問い直した論文。[評価の枠組み](../concepts/evaluation-framework.md) の指標水準での実践例。

## 手法・実験

サーベイからは実験の詳細は判明しない（原論文未読）。
主張の構造は、現実の攻撃者のインセンティブから逆算して指標を選ぶ、というもの。

## 主要な知見

- 平均的な精度（AUC）は、現実の攻撃者が求めるもの——**少数のデータについて確実に当てる**——を
  反映していない
- したがって低い偽陽性率における真陽性率（TPR@low FPR）で評価すべきである

サーベイは関連して、訓練データ抽出のコンペティション
（lm-extraction-benchmark）が適合率・再現率だけでなく
**攻撃速度**を測定した例も挙げている。

## 限界・批判

- 指標を変えると手法のランキングがどう変わるかを、その後の言語モデル研究が
  体系的に再評価したかは、この Wiki では未確認
- 評価**セット**の分布差問題（[Das 25](das-2025-blind-baselines.md)）は別の軸の問題であり、
  指標を直しても解決しない。両方を直す必要がある → [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [評価の枠組み](../concepts/evaluation-framework.md)
- 同著者の実証研究: [Carlini 21](carlini-2021-extracting-training-data.md) / [Carlini 23b](carlini-2023-quantifying-memorization.md)
