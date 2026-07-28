---
title: Quantifying memorization in continual pre-training with Japanese general or industry-specific corpora
authors: [Hiromu Takahashi, Shotaro Ishihara]
year: 2025
venue: 1st Workshop on Large Language Model Memorization (L2M2), pp. 95–105
citekey: Takahashi 25b
tags: [japanese, continual-pretraining, domain-specific, conflict]
axis: [訓練セット, 出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Quantifying memorization in continual pre-training with Japanese corpora

## TL;DR

日本語の**一般 / 産業特化コーパス**を用いた継続事前学習 [Ke 23] における暗記を定量化した。
[重複](../concepts/string-duplication.md)の知見は再現される一方、
**[文脈長](../concepts/context-length.md)については一部の実験で英語と逆の結果**を報告している。

## 位置づけ

訓練セット軸・出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) 4·4 節と 7·2 節の両方で引用される。
[学習順の影響](../concepts/training-order-and-forgetting.md)が構造的に最大化される設定
（継続事前学習では追加コーパスが必ず学習の後半に来る）。

## 手法・実験

日本語の一般コーパスと産業特化コーパスによる継続事前学習。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- [文字列の重複](../concepts/string-duplication.md): 文字列の重複に関する知見が再現される
- [文脈長](../concepts/context-length.md): **一部の実験で、文脈長が小さいほど性能が高いという
  英語と逆の関係**が報告された。[小柳 24] の結果と類似する
- サーベイはこの反例を受けて、
  「多様なドメインや言語を対象にした詳細な分析の必要性を示唆している」と述べる

## 限界・批判

- 逆転が「一部の実験で」観測された点が重要である。
  **再現しなかった実験との差が何か**は、この Wiki では未解明であり、
  日本語での逆転の原因（言語特性 / 定量化手法 / 評価セット構成）を
  切り分ける最大の手がかりである → [文脈長](../concepts/context-length.md)

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文脈長](../concepts/context-length.md) / [文字列の重複](../concepts/string-duplication.md)
- [学習順と忘却](../concepts/training-order-and-forgetting.md)（継続事前学習と学習順）
- 先行: [Ishihara 24](ishihara-2024-japanese-newspaper.md)
- 総括: [Ishihara 26](ishihara-2026-memorization-survey.md)
- 本論文を引用している概念: [メンバーシップ推論](../concepts/membership-inference.md)
