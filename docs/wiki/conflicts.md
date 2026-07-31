---
title: 対立の台帳（Conflicts）
type: ledger
---

# 対立の台帳

**この Wiki が最も価値を持つのは、対立を消さずに残している部分である。**

サーベイと後続研究、あるいは言語や設定の違いで結論が食い違う箇所を、
どちらかを採用せずに一覧化する。各項目には**何をすれば決着するか**を併記する。

`lint` は矛盾を検出したら、どちらかを消すのではなくこのページに追記すること
（`.claude/skills/lint/SKILL.md` B-11）。

## 状態の凡例

| 記号 | 意味 |
|---|---|
| **未決着** | 両論が併存し、交絡が切り分けられていない |
| **説明あり** | 対立に見えるが、測っているものが違うと整理できる |
| **保留** | 決着させうる材料が存在するが、この Wiki が未検証 |

---

## 1. 文脈長の効果が英語と日本語で逆転する

**状態: 未決着** ｜ 主ページ: [文脈長](concepts/context-length.md)

この Wiki で唯一、実証的知見の符号そのものが反転している対立。

| 立場 | 根拠 |
|---|---|
| **正の関係**（文脈長が長いほど暗記が増える） | [Carlini 23b](papers/carlini-2023-quantifying-memorization.md)、[Chen 25](papers/chen-2025-revisiting-mia.md)、[Shi 24](papers/shi-2024-min-k-prob.md)、[Kandpal 22](papers/kandpal-2022-deduplicating-privacy.md) |
| **負の関係**（文脈長が短いほど性能が高い） | [小柳 24]（日本語 MIA）、[Takahashi 25b](papers/takahashi-2025-continual-pretraining-japanese.md)（一部の実験） |

### 切り分けられていない交絡

1. **言語**: 日本語には語境界が無い。ユニグラム言語モデル [Kudo 18] のトークン分割が影響する可能性
2. **定量化手法**: 反例はいずれもメンバーシップ推論の設定。英語の正の関係は文字列類似度でも確認されている
3. **ドメイン**: [Takahashi 25b](papers/takahashi-2025-continual-pretraining-japanese.md) は継続事前学習という特殊な設定
4. **評価セットの構成**: 分布差の検出しやすさを反映している可能性（推測）

### 決着させる実験

- **日本語で文字列類似度ベースの文脈長分析を行う。** 正の関係が出れば手法要因、
  出なければ言語要因の可能性が高まる。**最も安価で情報量が大きい**
- [Takahashi 25b](papers/takahashi-2025-continual-pretraining-japanese.md) で
  **逆転が起きた実験と起きなかった実験の差**を特定する
- 中国語・タイ語など、語境界の無い他言語で再現するか確認する

---

## 2. デコーディング戦略が抽出量に影響するか

**状態: 未決着** ｜ 主ページ: [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)

| 立場 | 根拠 |
|---|---|
| **影響しない** | [Carlini 23b](papers/carlini-2023-quantifying-memorization.md): デコーディング戦略の違いは実験結果に大きな影響を与えない |
| **影響する** | [Lee 23]: top-k / top-p サンプリングの方が訓練データをより多く抽出する傾向 |

サーベイはどちらも採用せず両論を併記している。この Wiki でも消さない。

### 切り分けられていない交絡

- モデル規模（[Carlini 23b](papers/carlini-2023-quantifying-memorization.md) は最大 6B）
- ドメイン（[Lee 23] は特許・学術論文・COVID-19 の継続事前学習）
- 暗記の定義（逐語 vs 近似）
- [Hayes 25] が指摘する**サンプリングの確率的な揺らぎ**を、どちらも十分に扱っていない可能性

### 決着させる実験

- 同一モデル・同一コーパスで、デコーディング戦略のみを変えて抽出量を測る
- [Hayes 25] の確率的抽出の枠組みで両者を再測定する

---

## 3. 「時期で分ける」設計が長所か欠陥か

**状態: 説明あり（ただし含意は重い）** ｜ 主ページ: [評価セットとライブラリ](concepts/benchmarks-and-tools.md)

**同一の設計判断が、目的によって正反対の評価を受けている。**

| 文脈 | 評価 | 根拠 |
|---|---|---|
| データセット汚染の回避 | **推奨** | [Jacovi 23]、[Uddin 25]（訓練後に作成されたデータで評価する） |
| メンバーシップ推論の評価 | **欠陥** | [Das 25](papers/das-2025-blind-baselines.md)（WikiMIA は年の文字列だけで解ける） |

### 整理

汚染回避では「訓練セットに入っていないこと」が保証されればよく、分布差は問題にならない。
メンバーシップ推論では**分布差そのものが正解ラベルと相関してしまう**ため致命的になる。
つまり対立ではなく、**要求が違う**。

ただし含意は重い。サーベイ 7·1 節の
「どのような状況を想定した研究なのかを明確にした上で、適切な実験設定を選ぶ」という要請の、
最も具体的な帰結である。→ [評価の枠組み](concepts/evaluation-framework.md)

---

## 4. 「メンバーシップ推論が効かない」は方法論の失敗か理論的帰結か

**状態: 保留（決着材料が存在する可能性）** ｜ 主ページ: [メンバーシップ推論](concepts/membership-inference.md)

| 立場 | 根拠 |
|---|---|
| **方法論の失敗** | [Das 25](papers/das-2025-blind-baselines.md)、[Chen 25](papers/chen-2025-revisiting-mia.md)、[Duan 24](papers/duan-2024-do-mia-work.md): 評価セットの分布差が非本質的な性能を生んでいた |
| **理論的帰結** | Morris et al.「How much do language models memorize?」（ICML 2026）: トークン/パラメータ比が大きいモデルは原理的にメンバーシップ推論から遮蔽される（**この Wiki 未 ingest・未検証**） |

この 2 つは排他ではない。しかし後者が正しければ、
**否定的な結果の一部は評価セットを直しても解消しない**ことになり、
[評価セットとライブラリ](concepts/benchmarks-and-tools.md) と
[メンバーシップ推論](concepts/membership-inference.md) の横断的知見は書き換えが要る。

### 決着させる手順

- **Morris et al. を ingest して主張を確認する**（→ [未解決の問い](questions.md) 最優先 5）
- MIMIR / OLMoMIA 上での再ランキングが、理論の予測と整合するか照合する

---

## 5. 暗記されやすさと識別されやすさが逆を向く

**状態: 説明あり** ｜ 主ページ: [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)

| 立場 | 根拠 |
|---|---|
| **重複が多いほど暗記されやすい** | [Carlini 23b](papers/carlini-2023-quantifying-memorization.md)、[Lee 22](papers/lee-2022-deduplicating.md)、[Kandpal 22](papers/kandpal-2022-deduplicating-privacy.md) |
| **希少・低資源ほど漏洩リスクが高い** | [Jagannatha 21]（希少疾患の患者）、[Satvaty 25](papers/satvaty-2025-language-sensitive.md)（低資源言語ほど MIA の性能が高い） |

### 整理

矛盾ではなく**測っている量が違う**。暗記されやすさは重複に依存し、
識別されやすさは希少性（外れ値性）に依存する。

**含意が重要**: 守るべき機密情報はまさに外れ値の側にあるため、
[重複排除](concepts/deduplication.md)は**最も守るべきデータには効かない**。

---

## 6. 正則化は暗記に効くのに、暗記は過学習ではない

**状態: 説明あり（機序は未解明）** ｜ 主ページ: [学習過程における抑制](concepts/mitigation-in-training.md)

| 立場 | 根拠 |
|---|---|
| **正則化は暗記の抑制に有効** | [Yeom 18]、[Zhang 21] |
| **暗記は過学習の副産物ではない** | [Tirumala 22](papers/tirumala-2022-memorization-without-overfitting.md)（過学習前に大半を暗記）、[Carlini 23b](papers/carlini-2023-quantifying-memorization.md) |

### 整理

両立しうる（正則化は過学習以外の経路にも効きうる）。しかし
**なぜ効くのかの説明はこの Wiki に無い**。過学習経由なのか別経路なのかが未解明である。

さらに [Mireshghallah 21] は正則化が[差分プライバシ](concepts/differential-privacy.md)より
有用と主張しており、形式的保証の強さと実用上の有効性が一致しないことも示している。

---

## 7. 形式的定義は言語データを捉えられるか

**状態: 未決着（枠組みの問題）** ｜ 主ページ: [差分プライバシ](concepts/differential-privacy.md)

| 立場 | 根拠 |
|---|---|
| **有効** | [Downey 22]（DP の導入は暗記の抑制に有効）、[Li 22]、[Yu 21, 22]、[He 23] |
| **捉えきれない** | [Brown 22](papers/brown-2022-what-does-it-mean-privacy.md)（テキストは粒度の定義が曖昧）、[Cummings 21]、[Tramèr 24] |

### 整理

この対立は[重複排除](concepts/deduplication.md)（データの削除）でも同じ形で現れる。
根本は「**言語データにおける秘密の単位が定義できない**」という一点であり、
前処理（5·1）と学習アルゴリズム（5·2）という異なる段階の手法が、同一の壁に阻まれている。

→ [未解決の問い](questions.md) C 分類。実験では閉じない。
