---
title: "Position: Membership inference attacks cannot prove that a model was trained on your data"
authors: [Jie Zhang, Debeshee Das, Gautam Kamath, et al.]
year: 2025
venue: IEEE Conference on Secure and Trustworthy Machine Learning (SaTML) 2025, pp. 333–345
citekey: Zhang 25a
tags: [membership-inference, critique, legal, position]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Membership inference attacks cannot prove that a model was trained on your data

## TL;DR

メンバーシップ推論は「モデルがあなたのデータで訓練された」ことを**証明できない**、
という立場表明（position paper）。訓練セットの正確な内容が分からない状況では
**特殊なコーパスを用いた検証**が選択肢に入ると述べる。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の**法的・実務的な限界**を明確にした論文。
サーベイ 7·1 節（現実の問題に即した評価の枠組み）で引用される。

## 手法・実験

立場表明論文。サーベイからは詳細は判明しない（原論文未読）。

## 主要な知見

- メンバーシップ推論の結果は、統計的な示唆にとどまり、
  個別データの訓練セットへの帰属を**証明する**ものではない
- 訓練セットの正確な内容が分からない状況を踏まえると、
  特殊なコーパスを用いた検証も選択肢に入る（サーベイ 7·1 が引用）

## 限界・批判

- 「証明できない」ことは示すが、**では何が証明になるのか**は開かれたままである。
  この Wiki では [著作権](../concepts/copyright.md) の未解決の問いとして残っている

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [著作権](../concepts/copyright.md) / [評価の枠組み](../concepts/evaluation-framework.md)
- 同方向の実証的批判: [Das 25](das-2025-blind-baselines.md)（共著者が重なる）
- [データセット汚染](../concepts/data-contamination.md)（塊の単位なら信頼できる、という対照）
- 本論文を引用している概念: [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)
