---
title: Quantifying memorization and detecting training data of pre-trained language models using Japanese newspaper
authors: [Shotaro Ishihara, Hiromu Takahashi]
year: 2024
venue: INLG 2024, pp. 165–179
citekey: Ishihara 24
url: https://aclanthology.org/2024.inlg-main.14/
tags: [japanese, domain-specific, newspaper, empirical]
axis: [訓練セット, モデル, 出力]
type: paper
---

# Quantifying memorization and detecting training data using Japanese newspaper

## TL;DR

**日本語新聞記事という限られたコーパスでドメイン特化 GPT-2 を事前学習し、
3 因子（文字列の重複・モデルサイズ・プロンプト長）すべてが日本語でも再現される**ことを示した。
メンバーシップ推論も日本語で機能する。
「ドメイン特化モデルは、貴重な非公開データを大規模に『コピー&ペースト』しうる」と警告する。

## 位置づけ

3 軸すべて。[Ishihara 26](ishihara-2026-memorization-survey.md) の著者による先行研究で、
4·4 節（英語以外のドメインや言語）に位置づけられる。

**この Wiki が「日本語で 3 因子が再現するか」を判断する主要な根拠**である。
[Kiyomaru 24](kiyomaru-2024-comprehensive-analysis.md) が一般的な日本語モデルを扱うのに対し、
本研究は**ドメイン特化かつ自前で事前学習した**点が違う。

## 手法・実験

- **新聞記事コーパスで GPT-2 モデルを自前で事前学習**（既存モデルの分析ではない）
- 生成した文字列と訓練データの類似度で暗記を定量化
- あわせてメンバーシップ推論攻撃も実施

訓練セットを完全に統制できるため、**重複回数を正確に把握したうえで暗記を測れる**。
これは訓練セットが未公開の既存モデルを分析する研究には無い強みである。

## 主要な知見

### 1. 3 因子すべてが日本語で再現する

[Carlini 23b](carlini-2023-quantifying-memorization.md) が示した
**文字列の重複・モデルサイズ・プロンプト長**の 3 つとの関係が、
**日本語でも英語の先行研究と同じように再現された**。

> **プロンプト長も含めて再現している点が重要である。**
> この Wiki は当初「[文脈長](../concepts/context-length.md)は日本語で逆転する」と整理していたが、
> 本研究はその反例にあたる。→ [対立の台帳](../conflicts.md) 1 番

### 2. メンバーシップ推論も日本語で機能する

訓練データの検出が日本語でも可能であり、**重複が多くプロンプトが長いほど検出しやすい**。
英語と同じ傾向である。

### 3. エポック数の増加は文字列の重複と等価である

ドメイン特化モデルは一般モデルより事前学習コーパスが小さく、
データ量が少ないときは**複数エポック学習される傾向がある**。
しかし論文が指摘するとおり、**エポック数を増やすことは文字列の重複と等価**であり、
暗記のリスクを高める。

これは[文字列の重複](../concepts/string-duplication.md)を
「データの性質」ではなく**「学習レシピの帰結」**として捉え直す視点であり、
[学習順と忘却](../concepts/training-order-and-forgetting.md)とも接続する。
ドメイン特化モデルの開発は、構造的に暗記リスクが高い。

## 限界・批判

- **0.1B 規模の GPT-2** であり、実用規模から離れている。
  [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md) は
  8B Llama 3 がわずか 1,000 ステップで本研究の 30 エポック相当の暗記量を超えたと報告している
- **単一ドメイン**（新聞記事）であり、他の日本語ドメインへの一般化は未検証
- 新聞記事は冒頭に定型表現（見出し・リード）が来やすく、
  「冒頭の数トークンをプロンプトに」という評価セット構築の慣行が
  系統的なバイアスを生む可能性がある（推測）→ [評価の枠組み](../concepts/evaluation-framework.md)
- 非公開コーパスを用いるため再現性に制約がある

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文字列の重複](../concepts/string-duplication.md) / [文脈長](../concepts/context-length.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- [学習順と忘却](../concepts/training-order-and-forgetting.md)（エポック数と重複の等価性）
- 発展: [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md)
- 総括: [Ishihara 26](ishihara-2026-memorization-survey.md) ／ 前身のサーベイ: [Ishihara 23](ishihara-2023-training-data-extraction-survey.md)
- [著作権](../concepts/copyright.md)（報道分野と「忘れられる権利」）
