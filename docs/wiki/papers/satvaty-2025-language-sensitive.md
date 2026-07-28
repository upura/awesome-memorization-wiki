---
title: "Memorization is language-sensitive: Analyzing memorization and inference risks of LLMs in a multilingual setting"
authors: [Ali Satvaty, Anna Visman, Dan Seidel, et al.]
year: 2025
venue: 1st Workshop on Large Language Model Memorization (L2M2), pp. 106–126
citekey: Satvaty 25
tags: [multilingual, low-resource, empirical]
axis: [モデル, 出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Memorization is language-sensitive

## TL;DR

オランダ語・スロベニア語・ポーランド語・チェコ語での暗記を、
[文字列の類似度](../concepts/string-similarity-memorization.md)と[メンバーシップ推論](../concepts/membership-inference.md)の両方で分析した。
[モデルサイズ](../concepts/model-size.md) の知見が再現された上、**低資源言語ほどメンバーシップ推論の性能が高まる**と報告。

## 位置づけ

モデル軸・出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) 4·4 節と 7·2 節で引用される。
英語以外の言語を複数扱った数少ない研究。

## 手法・実験

オランダ語・スロベニア語・ポーランド語・チェコ語を対象に、
文字列の類似度とメンバーシップ推論の 2 系統で暗記を分析する。

## 主要な知見

- [モデルサイズ](../concepts/model-size.md): モデルサイズに関する知見が再現された
  → **言語横断で頑健な因子である**という本 Wiki の整理を支持
- **低資源言語ほどメンバーシップ推論の性能が高まる**
- [学習順と忘却](../concepts/training-order-and-forgetting.md): 学習の後半に用いられたテキストの方が
  暗記されやすいという学習順の影響も観測

## 限界・批判

- 対象言語はいずれもヨーロッパ言語であり、語境界の無い日本語・中国語などとは
  言語特性が異なる。[文脈長](../concepts/context-length.md) の日本語での逆転を説明する材料にはならない
- 「低資源ほどメンバーシップ推論の性能が高まる」は、
  低資源言語のデータ自体が[分布として識別しやすい](../concepts/benchmarks-and-tools.md)ことを
  反映している可能性が排除されていない（推測）

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [モデルサイズ](../concepts/model-size.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md)（低資源・外れ値ほど識別されやすい構造）
- 臨床ドメインでの類似の報告: [Jagannatha 21]
- 同著者のサーベイ: [Satvaty 24](satvaty-2024-undesirable-memorization.md)
