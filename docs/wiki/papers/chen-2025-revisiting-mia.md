---
title: A statistical and multi-perspective revisiting of the membership inference attack in large language models
authors: [Bowen Chen, Namgi Han, Yusuke Miyao]
year: 2025
venue: "ACL 2025 (Volume 1: Long Papers), pp. 22854–22874"
citekey: Chen 25
tags: [membership-inference, evaluation, empirical]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# A statistical and multi-perspective revisiting of the membership inference attack in LLMs

## TL;DR

メンバーシップ推論手法に対する**包括的な実証実験**を通じて、
既存の評価が非本質的な部分で高い性能を出していると指摘。
あわせて [モデルサイズ](../concepts/model-size.md) と [文脈長](../concepts/context-length.md) の知見を再確認した。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の包括的評価に取り組んだ研究
（サーベイ 3·2§2 が [Ravaut 25] と並べて挙げる）。

## 手法・実験

統計的・多角的な観点からのメンバーシップ推論手法の再検討。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- **WikiMIA** [Shi 24](shi-2024-min-k-prob.md) は正例・負例の分布の違いにより、
  **非本質的な部分で高い性能が出ている** [Chen 25, Kim 26]
- PPL/zlib [Carlini 21](carlini-2021-extracting-training-data.md) は基礎的な手法として
  よく用いられる
- [モデルサイズ](../concepts/model-size.md): モデルサイズが大きいほど暗記されやすいという知見を支持
- [文脈長](../concepts/context-length.md): 文脈長が大きいほど暗記量が増えるという知見を、
  メンバーシップ推論手法に対する包括的な実証実験を通じて確認

## 限界・批判

- 英語を対象とした実験である。日本語では [文脈長](../concepts/context-length.md) の知見が逆転する
  [小柳 24] → [ドメインや言語横断](../concepts/multilingual-and-domain.md)

## Wiki 内の接点

- [メンバーシップ推論](../concepts/membership-inference.md) / [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [文脈長](../concepts/context-length.md) / [モデルサイズ](../concepts/model-size.md)
- 批判対象: [Shi 24](shi-2024-min-k-prob.md)
- 同方向: [Das 25](das-2025-blind-baselines.md) / [Duan 24](duan-2024-do-mia-work.md)
- 本論文を引用している概念: [著作権](../concepts/copyright.md)
