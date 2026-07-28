---
title: Detecting pretraining data from large language models
authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, et al.]
year: 2024
venue: ICLR 2024
citekey: Shi 24
tags: [membership-inference, benchmark, output]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Detecting pretraining data from large language models（Min-K% Prob / WikiMIA）

## TL;DR

**Min-K% Prob**（生成確率の低い K% のトークンのみに着目して平均対数尤度を計算）と、
評価セット **WikiMIA** を提案した。事前学習データ検出の標準的な出発点になった。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の言語モデル向け代表手法。
提案手法と評価セットが同時に標準化された点が、後の批判の焦点になる
→ [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## 手法・実験

**Min-K% Prob**: 生成確率の低い K% のトークンのみに着目し平均の対数尤度を計算すると、
メンバーシップ推論の性能が上がることを実証的に示した。

**WikiMIA**: Wikipedia を元に構築。
2017 年以前に作成され訓練セットに含まれると期待される記事を**正例**、
評価対象モデルの公開後（2023 年以降）に作成された記事を**負例**とする。

## 主要な知見

- 低確率トークンに絞ることでメンバーシップ推論の性能が向上する
- [文脈長](../concepts/context-length.md) について、文脈長が大きいほど暗記量が増えるという知見を支持する報告

## 限界・批判

**この Wiki で最も重い批判が集まっている論文である。**

- WikiMIA は正例・負例を作成時期で分けているため**分布が系統的に異なる**。
  [Das 25](das-2025-blind-baselines.md) は**年の文字列に着目するといった素朴な手法でも
  高度なメンバーシップ推論手法より高い性能が出る**と報告した
- [Chen 25](chen-2025-revisiting-mia.md) と [Kim 26] も「非本質的な部分で高い性能が出ている」と指摘
- 応答として MIMIR [Duan 24](duan-2024-do-mia-work.md) や OLMoMIA [Kim 26] が
  よりランダムな分割を採用している
- 改良版として Min-K%++ [Zhang 25b]（生成確率の正規化と標準化を追加）がある

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [文脈長](../concepts/context-length.md)
- 批判: [Das 25](das-2025-blind-baselines.md) / [Chen 25](chen-2025-revisiting-mia.md) / [Duan 24](duan-2024-do-mia-work.md)
- 原典: [Shokri 17](shokri-2017-membership-inference.md)
