---
title: "Undesirable memorization in large language models: A survey"
authors: [Ali Satvaty, Suzan Verberne, Fatih Turkmen]
year: 2024
venue: arXiv [cs.CL]
citekey: Satvaty 24
tags: [survey]
axis: [横断]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Undesirable memorization in large language models: A survey

## TL;DR

大規模言語モデルの**意図せぬ（望ましくない）暗記**に絞ったサーベイ。

## 位置づけ

[Ishihara 26](ishihara-2026-memorization-survey.md) が明示的に差分を述べる関連サーベイの一つ。

サーベイの整理によれば、既存の関連する取り組みは
「暗記に関する**特定の話題に絞ったもの**」と
「**言語モデルに限らず**広範に調査しているもの」に大別され、本論文は前者に属する。
[Ishihara 26](ishihara-2026-memorization-survey.md) は
「悪意を持った攻撃やメンバーシップ推論以外の暗記定量化の方法も含めて
幅広く暗記を扱っている」点で差別化している。

同じ位置づけの関連サーベイ:

| 論文 | 焦点 |
|---|---|
| [Meeus 25] | メンバーシップ推論（SoK。「どこにも向かっていない」という批判） |
| [Wu 25] | 大規模モデルへのメンバーシップ推論 |
| [Cheng 25b], [Xu 24] | データ汚染 → [データセット汚染](../concepts/data-contamination.md) |
| [Ravaut 25] | 汚染検出手法。サーベイ 3·2 節の分類の元 |
| [Kaneko 25a] | 事前学習データ漏洩とモデルの再現・検出能力 |
| [Wei 25] | 深層学習一般の暗記（対象が広い） |
| [Hu 22b] | メンバーシップ推論全般（対象が広い）。5 章の抑制手法の分類の参考文献 |

## 手法・実験

サーベイ論文。

## 主要な知見

**要 ingest。**

## 限界・批判

- 「望ましくない暗記」に絞ることで、
  [暗記](../concepts/memorization.md) の「暗記は常に排除すべき対象ではない」という
  サーベイ 7·1 節の論点を扱いにくくなっている可能性がある（推測）

## Wiki 内の接点

- [Ishihara 26](ishihara-2026-memorization-survey.md) / [暗記](../concepts/memorization.md)
- 同著者の実証研究: [Satvaty 25](satvaty-2025-language-sensitive.md)
