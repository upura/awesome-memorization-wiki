---
title: What does it mean for a language model to preserve privacy?
authors: [Hannah Brown, Katherine Lee, Fatemehsadat Mireshghallah, et al.]
year: 2022
venue: FAccT 2022, pp. 2280–2292
citekey: Brown 22
tags: [privacy, critique, definition]
axis: [訓練セット, モデル]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# What does it mean for a language model to preserve privacy?

## TL;DR

**プライバシは文脈依存的**であり、形式的定義（差分プライバシ）も文字列ベースの削除も
言語データの複雑さを十分に捉えられない、という批判。

## 位置づけ

訓練セット軸・モデル軸の両方に、**同じ根本問題**として現れる批判。
サーベイでは 3·1§2（差分プライバシの限界）と 5·1（データ削除の限界）の
2 箇所で引用される。

## 手法・実験

概念的・規範的な論文。サーベイからは詳細は判明しない（原論文未読）。

## 主要な知見

- **差分プライバシに対して**: 個人情報保護には有効だが、言語データの複雑さを
  十分に捉えられない。テキストは粒度の定義が曖昧であり、
  トークンや文書の単位、ユーザに着目した括りなど、多様なレベルでの
  秘密境界設定が検討されている [Charles 25, Levy 21, McMahan 18]
- **データの削除に対して**: この手法は**文脈に依存しない静的な情報の除去にのみ
  限定的に有効**である。プライバシは文脈依存的 [Dourish 04, Nissenbaum 09] であり、
  文字列のみから一意に判定するのは困難

## 限界・批判

- 批判は説得的だが、代替となる操作的な定義を提供するものではない。
  「では何を守るのか」はサーベイ 7·1 節の未解決課題として残る

## Wiki 内の接点

- [差分プライバシ](../concepts/differential-privacy.md) / [重複排除](../concepts/deduplication.md) — この 2 ページの限界セクションは
  いずれもこの論文に依拠している
- [暗記](../concepts/memorization.md) / [評価の枠組み](../concepts/evaluation-framework.md)
- [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md)
- 本論文を引用している概念: [逆学習](../concepts/machine-unlearning.md) / [学習過程における抑制](../concepts/mitigation-in-training.md)
