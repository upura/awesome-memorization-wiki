---
title: A comprehensive analysis of memorization in large language models
authors: [Hirokazu Kiyomaru, Issa Sugiura, Daisuke Kawahara, et al.]
year: 2024
venue: INLG 2024, pp. 584–596
citekey: Kiyomaru 24
tags: [japanese, empirical, quantification]
axis: [訓練セット, モデル, 出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# A comprehensive analysis of memorization in large language models

## TL;DR

**日本語**を対象に、続きを生成する方法で暗記を定量化し、
英語での実証的知見が日本語でも再現されると確認した。

## 位置づけ

3 軸すべて。[Ishihara 26](ishihara-2026-memorization-survey.md) 4·4 節が、
日本語に関する研究として最初に挙げる論文。

## 手法・実験

[続きの生成](../concepts/string-similarity-memorization.md)（サーベイ図2 の手法）による暗記の定量化。

## 主要な知見

- **英語での実証的知見が日本語でも再現される**
- [文字列の重複](../concepts/string-duplication.md): 重複が多いほど暗記されやすい
- [モデルサイズ](../concepts/model-size.md): モデルサイズが大きいほど暗記されやすい

## 限界・批判

- [文脈長](../concepts/context-length.md) については、[小柳 24] が日本語のメンバーシップ推論で
  **逆の関係**を報告している。定量化手法（続きの生成 vs メンバーシップ推論）の
  違いが効いている可能性があり、この Wiki では切り分けられていない
  → [ドメインや言語横断](../concepts/multilingual-and-domain.md)
- 抑制手法（[重複排除](../concepts/deduplication.md) など）の日本語での有効性は扱っていない

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文字列の重複](../concepts/string-duplication.md) / [モデルサイズ](../concepts/model-size.md)
- 日本語のドメイン特化: [Ishihara 24](ishihara-2024-japanese-newspaper.md) / [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md)
