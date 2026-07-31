---
title: Extracting training data from large language models
authors: [Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Úlfar Erlingsson, Alina Oprea, Colin Raffel]
year: 2021
venue: USENIX Security 21, pp. 2633–2650
citekey: Carlini 21
url: https://arxiv.org/abs/2012.07805
tags: [extraction, membership-inference, privacy, landmark]
axis: [出力]
type: paper
---

# Extracting training data from large language models

## TL;DR

GPT-2 から **1,800 件の候補のうち 600 件以上が訓練データそのもの**だと確認し、
個人の氏名・住所・メール・電話・FAX 番号までを抽出してみせた。
**k-eidetic memorization** という、危険度を k で表す**スペクトラム型の定義**を導入した。

## 位置づけ

出力軸。この分野の起点となる論文であり、
[Ishihara 26](ishihara-2026-memorization-survey.md) 冒頭で「先駆的な研究」として紹介される。
[訓練データ抽出](../concepts/security-and-privacy-leakage.md)の 2 段階手続き
（候補生成 + [メンバーシップ推論](../concepts/membership-inference.md)）を確立した。

**GPT-2 を対象にしたのは現実の被害を最小化するため**である
（モデルと訓練データの出所がすでに公開されているため）。

## 手法・実験

### 定義：k-Eidetic Memorization（Definition 2）

> 文字列 `s` が LM から **k-eidetic memorized** であるとは、`s` が抽出可能であり、
> かつ `s` が訓練データ中の**高々 k 個の「例」**に出現することをいう。

**「例」の数**を数える点が重要である。GPT-2 では 1 つの Web ページが 1 例なので、
同じページに何度現れても k = 1 と数える。

**この定義は暗記をスペクトラムとして扱う。**

> 暗記が意図せぬもので有害だと言える k の決定的な値は存在しないが、
> **小さい値ほどその可能性が高い**。同じ k なら、長い文字列の暗記の方が「悪い」
> （定義は簡潔さのためこの区別を省いている）。

例: ある単語の正しい綴りの暗記は、多くの例に出現するなら（k が大きい）深刻でない。
特定の都市の郵便番号は、言及が多いか少ないかによる。
個人の氏名と電話番号は、インターネット上の数文書にしか含まれないため k が小さく、
プライバシ期待を明確に侵害する。

### 攻撃

**3 つのサンプリング戦略 × 6 つのランキング指標 = 18 構成**、各 100 件で計 1,800 候補。

1. **200,000 件を生成**（空または非空の接頭辞で条件付け）
2. 6 指標のいずれかで**並べ替え、重複を除去**
3. 上位 100 件を、**インターネット検索で人手確認**し、
   さらに **OpenAI と協働して元の訓練データを照会**して確定

サンプリング戦略には**温度付きサンプリング**と、
**自前の Common Crawl スクレイプからの接頭辞で条件付け**する戦略を含む。
後者は GPT-2 の収集手順（Reddit リンク）と意図的に変えて、訓練データとの交差を減らしている。

ランキング指標は**参照モデル（別の LM）との尤度比**を使う。
**より小さい GPT-2（Small 117M / Medium 345M）**との比較も含む——
小さいモデルは暗記容量が小さいので、大モデルだけが小さい k で暗記した例を炙り出せる、という発想。
[PPL/zlib](../concepts/membership-inference.md) や Lowercase もここで導入された。

## 主要な知見

- **1,800 候補のうち 600 件超が訓練データの逐語コピー。最良の構成では精度 67%。**
- 最も機微な抽出例は、ある個人の**氏名・住所・メールアドレス・電話番号・FAX 番号**
- 素朴なメンバーシップ推論は精度が低い。原因は言語モデル側の失敗にあり、
  **自明な暗記（trivial memorization）**などが偽陽性を生む
- 学習の進展の中で、特定の訓練データが**異常に低い損失**を示すことを観測
  （→ [学習順と忘却](../concepts/training-order-and-forgetting.md)）
- 明示的に公開されていなくても「Bob's phone number is」のような推察が可能

### 緩和策についての評価

- **差分プライバシ**: 理論的に十分な基礎があり、**適切なレコード単位で適用すれば**
  プライベートなモデルを保証する。ただし学習時間が延び、有用性が劣化するのが通常
- **文書の丁寧な重複排除**: 経験的に暗記の緩和に役立つが、**すべての攻撃を防ぐことはできない**

## 限界・批判

- **狙い撃ちの攻撃ではない。** 論文自身が「特定の訓練データを狙うのではなく、
  無差別に抽出する」と明言している。目的は言語モデル一般の暗記能力の研究であり、
  「実際の敵対者が特定ユーザを狙うために運用できる攻撃を作ること」ではない
- 抽出できたことは示すが、**暗記量の全体像は与えない**。
  [Carlini 23b](carlini-2023-quantifying-memorization.md) は本論文の下界を
  「データセットの 0.00000015% 以上」という緩いものだと評している
- 確認に人手のインターネット検索と OpenAI の協力を要しており、**再現の敷居が高い**
- PPL/zlib・Lowercase は基礎的手法としてよく用いられる [Chen 25] が、
  その後の評価セットの分布差問題（→ [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)）の影響を受ける

## Wiki 内の接点

- [暗記](../concepts/memorization.md) / [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- [評価の枠組み](../concepts/evaluation-framework.md)（k による危険度のスペクトラム化）
- [文字列の類似度](../concepts/string-similarity-memorization.md) / [重複排除](../concepts/deduplication.md)
- 定量的な後継: [Carlini 23b](carlini-2023-quantifying-memorization.md)
- 評価指標への自己批判: [Carlini 22](carlini-2022-first-principles.md)
- 本論文を引用している概念: [学習過程における抑制](../concepts/mitigation-in-training.md) / [学習順と忘却](../concepts/training-order-and-forgetting.md) / [差分プライバシ](../concepts/differential-privacy.md)
