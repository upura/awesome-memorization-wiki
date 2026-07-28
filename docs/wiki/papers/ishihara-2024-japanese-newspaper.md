---
title: Quantifying memorization and detecting training data of pre-trained language models using Japanese newspaper
authors: [Shotaro Ishihara, Hiromu Takahashi]
year: 2024
venue: INLG 2024, pp. 165–179
citekey: Ishihara 24
tags: [japanese, domain-specific, newspaper, empirical]
axis: [訓練セット, 出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Quantifying memorization and detecting training data using Japanese newspaper

## TL;DR

**日本語新聞記事**というドメイン特化コーパスを用いて、
事前学習済み言語モデルの暗記の定量化と訓練データの検出に取り組んだ。
[文字列の重複](../concepts/string-duplication.md)に関する知見を日本語で再現した。

## 位置づけ

訓練セット軸・出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) の著者による先行研究であり、
4·4 節（英語以外のドメインや言語）に位置づけられる。

## 手法・実験

日本語新聞記事コーパス。暗記の定量化と訓練データの検出
（[メンバーシップ推論](../concepts/membership-inference.md)）の両方に取り組む。

## 主要な知見

- [文字列の重複](../concepts/string-duplication.md): 文字列の重複に関する知見が日本語新聞記事でも再現される

## 限界・批判

- 単一ドメイン（新聞記事）であり、他の日本語ドメインへの一般化は未検証
- 新聞記事は冒頭に定型表現（見出し・リード）が来やすく、
  「冒頭の数トークンをプロンプトに」という評価セット構築の慣行が
  系統的なバイアスを生む可能性がある（推測）→ [評価の枠組み](../concepts/evaluation-framework.md)

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文字列の重複](../concepts/string-duplication.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- 発展: [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md)
- 総括: [Ishihara 26](ishihara-2026-memorization-survey.md)
- [著作権](../concepts/copyright.md)（報道分野と「忘れられる権利」）
