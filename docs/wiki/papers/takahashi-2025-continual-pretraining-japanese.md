---
title: Quantifying memorization in continual pre-training with Japanese general or industry-specific corpora
authors: [Hiromu Takahashi, Shotaro Ishihara]
year: 2025
venue: 1st Workshop on Large Language Model Memorization (L2M2) 2025, pp. 95–105
citekey: Takahashi 25b
url: https://aclanthology.org/2025.l2m2-1.8/
tags: [japanese, continual-pretraining, domain-specific, empirical]
axis: [訓練セット, 出力]
type: paper
---

# Quantifying memorization in continual pre-training with Japanese corpora

## TL;DR

Llama 3 を**日本語 Wikipedia（一般）**と**日経電子版の金融記事（産業特化）**で
継続事前学習し、暗記を定量化した。学習が進むほど暗記が増える傾向は英語と同じで、
**産業特化コーパスで顕著**だった。日本語固有の傾向として
**Min-K% Prob より LOSS が優位**であることを報告している。

## 位置づけ

訓練セット軸・出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) 4·4 節と 7·2 節で引用される。
**非英語かつ産業特化のコーパスでの継続事前学習における暗記を、体系的に定量化した最初の研究**
と論文自身が位置づける。

[学習順と忘却](../concepts/training-order-and-forgetting.md)の効果が構造的に最大化される設定
（継続事前学習では追加コーパスが必ず学習の後半に来る）。

## 手法・実験

- **モデル**: Llama 3 (8B) を **LoRA**（rank 16、対象 q_proj / v_proj / fc_in / fc_out、
  学習率 1e-4、最大トークン長 512、マイクロバッチ 8）で継続事前学習
- **コーパス**:
  - 日本語 Wikipedia（一般）
  - **日経電子版**の 2010〜2022 年の記事、重複排除後で約 **7 億トークン**（産業特化）
- **open 設定**（訓練セット既知）: 1,000 記事について、先頭 200 文字
  （または記事長の半分の短い方）をプロンプト、残りを参照として類似度を測る
- **closed 設定**（訓練セット未知）: 訓練データから 1,000 記事を正例、
  **2023 年の記事 1,000 件を負例**とし、AUC で評価
- 手法: LOSS / PPL/zlib / Min-K% Prob / Min-K%++ / ReCaLL
- 入力語数を 32 / 64 / 128 / 256 と変えて評価

## 主要な知見

### 1. 産業特化コーパスで暗記が顕著に増える

open・closed 両設定で、日経電子版が Wikipedia より**有意に大きな暗記**を示した。
固有の専門用語と文体が原因と考察される。
論文は「価値ある非一般的な産業コーパスを使う際のリスク」を強調する。

### 2. モデルサイズの知見を再現

日経電子版で、大きいモデルほど暗記が多い。
**8B Llama 3 は、わずか 1,000 ステップ（0.25 エポック）で、
[Ishihara 24](ishihara-2024-japanese-newspaper.md) の 0.1B GPT-2 が
30 エポック後に到達した近似暗記量を超えた。**

### 3. 文脈長：コーパスによって向きが逆になる（**この Wiki にとって最重要**）

論文の Discussion は「closed 設定でメンバーシップ推論の性能は語数（プロンプト長）とともに
**向上した**、特に ReCaLL と LOSS で」と述べる。ただし本文は
「**日経電子版に限れば**、検出性能は学習ステップ数と語数とともに増加する傾向がある」とも書く。

Table 5 の数値を読むと、**コーパスで向きが分かれている**。

| コーパス | 手法 | 32 語 | 64 語 | 128 語 | 256 語 | 向き |
|---|---|---|---|---|---|---|
| Wikipedia | LOSS (12000 步) | 0.515 | 0.514 | 0.479 | 0.486 | **減少** |
| Wikipedia | ReCaLL (1000 步) | 0.613 | 0.605 | 0.569 | 0.520 | **減少** |
| 日経 | LOSS (12000 步) | 0.641 | 0.647 | 0.650 | 0.590 | 128 語まで増加 |
| 日経 | ReCaLL (12000 步) | 0.637 | 0.660 | 0.689 | 0.603 | 128 語まで増加 |

> **重要な留保**: Wikipedia での AUC は**ほぼすべて 0.46〜0.53 の範囲**にあり、
> メンバーシップ推論がそもそもほとんど機能していない（偶然と同等の）領域である。
> その中での減少傾向を「文脈長の効果の逆転」と読むのは慎重であるべきだ。
> 一方、日経電子版では AUC が 0.69 まで達しており、そこでは**増加**している。

→ [対立の台帳](../conflicts.md) 1 番を大きく更新する材料。

### 4. 日本語固有の傾向は「手法の優劣」に現れた

[小柳 24] は日本語では Min-K% Prob が大きい K で良いと示唆したが、本研究では
**LOSS が Min-K% Prob を上回った**。トークン分布に基づく手法は全般に性能が低く、
K を 10 刻みで変えても 0.5 以下の場合が複数あった。
論文は**日本語に語の区切りが無い特性**の影響を示唆する。

ReCaLL は 8 列中 6 列で最良だった。
「テキストを変換する手法は、言語固有の情報を暗黙に考慮している可能性がある」。

## 限界・批判

- **データセットの入手性。** 日経電子版は購入可能だが誰もが自由にアクセスできるわけではない。
  データ汚染を避けられる利点と引き換えに、**再現性が犠牲になる**と論文自身が認めている
- **危険度を区別していない。** 「すべてのテキストを等しく扱っている。
  電話番号やメールアドレスなど個人識別情報の望ましくない暗記は、
  許容可能な暗記と区別されるべきである」と論文自身が限界に挙げる
  → [評価の枠組み](../concepts/evaluation-framework.md)
- **LoRA を使っている。** 論文は LoRA が暗記に比較的耐性があるという報告に触れ、
  **全パラメータ学習との比較は今後の課題**としている。
  つまり本研究の暗記量は、全パラメータ継続事前学習より低い可能性がある
  → [学習過程における抑制](../concepts/mitigation-in-training.md)
- **closed 設定の負例が 2023 年の記事**であり、正例（2010〜2022 年）と時期で分かれている。
  [Das 25](das-2025-blind-baselines.md) が批判した分布シフトと同じ構造を持つ
  → [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## Wiki 内の接点

- [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文脈長](../concepts/context-length.md) / [文字列の重複](../concepts/string-duplication.md)
- [学習順と忘却](../concepts/training-order-and-forgetting.md)（継続事前学習と学習順）
- [メンバーシップ推論](../concepts/membership-inference.md)（手法の優劣が日本語で変わる）
- [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)（時期による分割）
- 先行: [Ishihara 24](ishihara-2024-japanese-newspaper.md) ／ 総括: [Ishihara 26](ishihara-2026-memorization-survey.md)
- 本論文を引用している概念: [モデルサイズ](../concepts/model-size.md)
