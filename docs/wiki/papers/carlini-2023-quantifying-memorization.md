---
title: Quantifying memorization across neural language models
authors: [Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr, Chiyuan Zhang]
year: 2023
venue: ICLR 2023
citekey: Carlini 23b
url: https://arxiv.org/abs/2202.07646
tags: [quantification, scaling, duplication, context-length, landmark]
axis: [訓練セット, モデル, 出力]
type: paper
---

# Quantifying memorization across neural language models

## TL;DR

暗記を初めて包括的に定量化し、**モデルサイズ・文字列の重複・文脈長**の 3 つと
対数線形関係があることを実証した。GPT-J 6B は **The Pile の少なくとも 1%** を暗記している。
ただし**追試では 3 因子のうちモデルサイズしか綺麗に一般化せず**、
重複の効果はデータセットの特異性に強く依存する。

## 位置づけ

3 軸すべてにまたがる。[Ishihara 26](ishihara-2026-memorization-survey.md) 4 章の骨格を提供しており、
本 Wiki では[軸論文](ishihara-2026-memorization-survey.md)に次いで参照が多い（**11 概念ページが依存**）。

先行研究 [Carlini 21](carlini-2021-extracting-training-data.md) が GPT-2 から
手作業で 600 例を特定し「データセットの 0.00000015% 以上が暗記されている」という
緩い下界を示したのに対し、本論文は**桁違いに精密な下界**を与えることを狙う。

## 手法・実験

### 暗記の定義（Definition 3.1）

> 文字列 `s` がモデル `f` から **k トークンの文脈で抽出可能（extractable）**であるとは、
> 長さ k の文字列 `p` が存在して、`[p || s]` が `f` の訓練データに含まれ、
> かつ `f` が `p` をプロンプトとして**貪欲デコーディング**で `s` を生成することをいう。

**他の定義を意図的に退けている**点が重要である。
[反実仮想暗記](../concepts/counterfactual-memorization.md)や差分プライバシの下界は
**数百〜数千のモデルを学習する必要があり**大規模言語モデルでは非現実的、
exposure [Carlini 19] は 1 系列あたり数千回の生成が必要、と述べている。
「実行可能（actionable）であること」を基準に定義を選んだ、という自覚的な選択である。

### 評価セットの構築

訓練セット全件の評価は非現実的（800GB を 6B モデルで走らせると **30 GPU 年**）。そこで 2 種類:

| 抽出方法 | 内容 |
|---|---|
| **一様ランダム** | 訓練セットから 50,000〜100,000 系列を一様サンプリング |
| **重複数・系列長で正規化** | 系列長 ℓ ∈ {50, 100, ..., 500} と整数 n について、訓練セット中に 2^(n/4) 〜 2^((n+1)/4) 回出現する系列を各 1,000 本選ぶ。計約 500,000 系列 |

重複部分列の同定には [Lee 22](lee-2022-deduplicating.md) の suffix array を用いる。

各系列について**先頭 ℓ−50 トークンをプロンプト**とし、
**残り 50 トークンを完全一致で生成できたら「抽出可能」**とする
（50 トークン ≒ 127 文字 ≒ 25 単語）。

> **重複正規化サンプルは重複文字列を過剰代表しているため、暗記量の絶対値には意味がない。**
> 論文自身が明記している。読めるのは傾向のみである。

### 対象モデル

- 主実験: **GPT-Neo** 系（125M / 1.3B / 2.7B / 6B、Pile で学習）
- **ベースライン: GPT-2** 系（WebText で学習。Pile は見ていない）
- 追試: **T5**（C4、マスク型）、**Lee 22 の重複排除済み C4 モデル**、**OPT**（〜66B）

## 主要な知見

### 1. モデルサイズ

**ほぼ完全な対数線形関係（R² = 99.8%）。モデルサイズ 10 倍で暗記量が 19 パーセントポイント増加。**
同一モデル族内で、大きいモデルは小さいモデルの **2〜5 倍**暗記する。

**GPT-2 ベースラインが決定的である。** 「大きいモデルほど暗記する」が
単に予測性能が高いからではないことを示すため、同規模の GPT-2（Pile 未学習）で同じ評価をした。
GPT-2 は約 **6%** しか正解できないのに対し、同規模の GPT-Neo 1.3B は **40%**。
GPT-2 が当てられる例は数列や定型句などの「つまらない」系列だった。
→ **暗記であって汎化ではない**ことの直接的な証拠。→ [モデルサイズ](../concepts/model-size.md)

### 2. 文字列の重複

2〜900 回のバケットで対数線形の傾向。ただし
**数回しか出現しない文字列でも暗記は起きるため、重複排除で漏洩を完全には防げない**。
→ [文字列の重複](../concepts/string-duplication.md)

### 3. 文脈長と「発見可能性（discoverability）」

文脈長に対しても対数線形。6B モデルで **50 トークンの文脈では 33%、450 トークンでは 65%** が抽出可能。

論文はこれを **discoverability phenomenon** と名付け、**両義的**だと論じる。

- **防御側に有利**: 100 トークンの正確なプロンプトが必要なら、現実の攻撃者は実行できない。
  **提供者は利用者に許すプロンプト長の上限を制限することで抽出リスクを大きく下げられる**
  （GitHub Copilot が良性の状況では暗記コードを稀にしか出さないのはこの効果と読める）
- **監査側に不利**: 「大きな文脈を与えずに暗記の裾を同定する既知の手法は無い」。
  つまり**正しく監査するには訓練データでプロンプトするしかない**

→ [文脈長](../concepts/context-length.md)

### 4. 追試：一般化するのはモデルサイズだけだった

**サーベイの記述に現れない、最も重要な留保。**

> We expected our results to cleanly generalize across settings, and this is indeed true for
> **model scale**. Yet, the situation is more complicated when considering **data duplication**,
> due to training set idiosyncrasies.

| 追試 | モデルサイズ | 重複 |
|---|---|---|
| **T5 / C4**（マスク型） | 再現する。ただし**絶対量は因果型より 1 桁小さい**（T5-XL 3B: 3.5% vs GPT-Neo 2.7B: 53.6%、100 回重複時） | **単調でない。** 138〜158 回重複が 159〜196 回重複より暗記されやすい（3σ で有意）。原因は前者が空白トークン主体で予測しやすいこと |
| **重複排除済み C4** | — | 35 回未満の重複では暗記が **3 分の 1**（1.2% vs 3.6%）。しかし**約 100 回を超える重複には効かない**。408 回以上は有意に高い。大規模な重複排除は原理的に不完全にならざるを得ないため |
| **OPT**（〜66B、整理済み Pile） | 傾向は同一だが**効果の大きさが数桁小さい**。66B OPT が 125M GPT-Neo より Pile の暗記が少ない | — |

OPT の結果について論文は 2 つの解釈を挙げ、**区別できないとしている**:
(a) 丁寧なデータ整理と学習で暗記は緩和できる、
(b) わずかなデータ分布の差でも暗記される内容が大きく変わる。

### 5. デコーディング戦略

貪欲デコーディングと**ビームサーチ（100 ビーム）**を比較し、
差は平均 2 パーセントポイント未満（最大 5.6%）、出力が一致したのは 45%。

**ランダムサンプリング（top-k / top-p）は実験していない。**
理由は「本研究の目的は発見可能性の最大化であり、言語的新規性の最大化とは対極だから」。
→ [対立の台帳](../conflicts.md) 2 番の解消に直結する。

### 6. 定義を緩めると暗記量は倍増する

生成が「訓練セットのどこかに」含まれていればよいとすると、
100 回重複の例で **32.6%**（正解の後続と一致するのは 15.8%）。

## 限界・批判

- **絶対値は解釈できない。** 重複正規化サンプルは重複を過剰代表している（論文自身が明記）
- **最大 6B。** 論文自身が「現在の最先端モデルは 6B の 200 倍以上のパラメータを持つ」と述べ、
  外挿は未検証としている → [モデルサイズ](../concepts/model-size.md)の未解決の問い
- **英語コーパスのみ**（Pile / C4）。日本語では[文脈長](../concepts/context-length.md)の知見が逆転する
- **最悪ケースの測定であって現実の攻撃ではない。** 論文は
  [Kandpal 22](kandpal-2022-deduplicating-privacy.md) との差を
  「あちらは攻撃が成功する理由の評価、こちらは訓練データの接頭辞を明示的に与える最悪ケースの測定で、
  現実の攻撃には必ずしもできないこと」と説明している
- **重複の知見はデータセット横断では成立しない**（上記 4）

## Wiki 内の接点

- 3 因子: [文字列の重複](../concepts/string-duplication.md) / [モデルサイズ](../concepts/model-size.md) / [文脈長](../concepts/context-length.md)
- [暗記](../concepts/memorization.md)（暗記 ≠ 汎化の主要な根拠 = GPT-2 ベースライン）
- [重複排除](../concepts/deduplication.md)（効果の上限を定量的に示した）
- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md)・[差分プライバシ](../concepts/differential-privacy.md)（計算コストを理由に退けた）
- [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)（プロンプト長の制限という緩和策）
- [評価の枠組み](../concepts/evaluation-framework.md)（抽出バイアスと監査の困難）
- [研究領域の拡張](../concepts/multimodal-memorization.md)（マスク型 T5 での追試）
- 前身: [Carlini 21](carlini-2021-extracting-training-data.md) ／ 定義を緩めた追試: [Ippolito 23](ippolito-2023-false-sense-of-privacy.md)
- 本論文を引用している概念: [逆学習](../concepts/machine-unlearning.md) / [暗記と汎化](../concepts/memorization-vs-generalization.md) / [学習過程における抑制](../concepts/mitigation-in-training.md) / [知識編集](../concepts/knowledge-editing.md) / [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) / [文字列の類似度](../concepts/string-similarity-memorization.md)
