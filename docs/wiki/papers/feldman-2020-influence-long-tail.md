---
title: "What neural networks memorize and why: Discovering the long tail via influence estimation"
authors: [Vitaly Feldman, Chiyuan Zhang]
year: 2020
venue: NeurIPS 2020, pp. 2881–2891
citekey: Feldman 20
tags: [definition, counterfactual, influence]
axis: [モデル]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# What neural networks memorize and why

## TL;DR

**特定の訓練データを含む場合と含まない場合で、学習済みモデルに対する損失の差分**を用いて
暗記を定義した。影響度推定によりロングテールを発見する枠組み。

## 位置づけ

モデル軸。[反実仮想に基づく定義](../concepts/counterfactual-memorization.md)の原典
（[Ishihara 26](ishihara-2026-memorization-survey.md) 3·1§1）。

## 手法・実験

損失差分による暗記の定義と、影響度推定（influence estimation）による測定。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- 暗記を「そのデータが無かったらモデルはどう違っていたか」という**反実仮想**で定義できる
- ロングテールのデータほど暗記される

## 限界・批判

- **計算コストが高い**。この定義を測定するには多数のモデルを学習する必要がある
  （[Carlini 23b](carlini-2023-quantifying-memorization.md) の指摘）
- 結果として、サーベイが述べるとおり
  「出力に着目する定義と比べて研究は盛んではない」状態が続いている
- 言語モデル固有の設定（大規模コーパス、逐語的な長文の再現）に対して
  この定義がどう振る舞うかは、[Zhang 23](zhang-2023-counterfactual-memorization.md) を待つ

## Wiki 内の接点

- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) / [暗記](../concepts/memorization.md)
- 言語モデルへの展開: [Zhang 23](zhang-2023-counterfactual-memorization.md)
- 発想を共有する形式的枠組み: [差分プライバシ](../concepts/differential-privacy.md)
- 逆学習の理想と同じ構造: [逆学習](../concepts/machine-unlearning.md)
