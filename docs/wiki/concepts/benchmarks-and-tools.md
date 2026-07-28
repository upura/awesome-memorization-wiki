---
title: 評価セットとライブラリ（Benchmarks and Tools）
aliases: [WikiMIA, MIMIR, OLMoMIA, Fast-MIA, ベンチマーク, ライブラリ]
axis: 出力
survey_section: "3·2§2"
tags: [resource, evaluation, output]
type: concept
---

# 評価セットとライブラリ

## 定義

暗記の定量化、特に [メンバーシップ推論](membership-inference.md) の評価に用いられるデータセットと実装
（[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 3·2§2）。

## 評価セット

| 名前 | 構成 | 出典 |
|---|---|---|
| **WikiMIA** | Wikipedia ベース。2017 年以前に作成され訓練セットに含まれると期待される記事を**正例**、評価対象モデルの公開後（2023 年以降）に作成された記事を**負例**とする | [Shi 24](../papers/shi-2024-min-k-prob.md) |
| **MIMIR** | よりランダムな設定でデータセットを分割 | [Duan 24](../papers/duan-2024-do-mia-work.md) |
| **OLMoMIA** | 同上 | [Kim 26] |

## ライブラリ

メンバーシップ推論の手法を整備したライブラリが公開されている
[Duan 24, Murakonda 20, Ravaut 25, Takahashi 25a]。

| 名前 | 出典 |
|---|---|
| MIMIR | [Duan 24](../papers/duan-2024-do-mia-work.md) |
| ML Privacy Meter | [Murakonda 20] |
| Fast-MIA | [Takahashi 25a] — 効率的でスケーラブルな実装 |
| （汚染検出手法の整理） | [Ravaut 25] |

## コンペティション

言語モデルからの訓練データ抽出を題材にしたコンペティション
（<https://github.com/google-research/lm-extraction-benchmark>）では、
適合率や再現率だけではなく**攻撃速度**を測定した。

## 主要な論文

- [Shi 24](../papers/shi-2024-min-k-prob.md) — Min-K% Prob と WikiMIA を同時に提案。標準であり批判の的
- [Das 25](../papers/das-2025-blind-baselines.md) — 盲目的ベースラインが既存手法を上回ることを示した
- [Chen 25](../papers/chen-2025-revisiting-mia.md) — 統計的・多角的な再検討。非本質的な性能を指摘
- [Duan 24](../papers/duan-2024-do-mia-work.md) — MIMIR（よりランダムな分割）とライブラリ
- [Carlini 22](../papers/carlini-2022-first-principles.md) — 評価**指標**の水準での批判

## 横断的知見

**WikiMIA の設計が、この分野の実証的知見の一部を無効化しかねない。**
本 Wiki で最も影響範囲の広い方法論的問題。
WikiMIA は正例・負例を**作成時期**で分けているため、両者の分布が系統的に異なる。
その結果:

- [Das 25](../papers/das-2025-blind-baselines.md): **年の文字列に着目するといった素朴な手法でも、
  高度なメンバーシップ推論手法より高い性能**が観測される
- [Chen 25](../papers/chen-2025-revisiting-mia.md), [Kim 26]: 「非本質的な部分で高い性能が出ている」と指摘

WikiMIA は [Shi 24](../papers/shi-2024-min-k-prob.md) とともに提案され、以後の標準的な比較基盤になった。
つまり**Min-K% Prob 以降の手法比較の多くが、暗記ではなく分布差を測っていた可能性がある**。
MIMIR [Duan 24](../papers/duan-2024-do-mia-work.md) と OLMoMIA [Kim 26] のよりランダムな分割は
この批判への応答である。

**同じ設計判断が、汚染検出では推奨されている。** [データセット汚染](data-contamination.md) では
「訓練後に作成されたデータで評価する」ことが汚染回避の正攻法とされる
（[Uddin 25] の時間依存 QA など）。しかしメンバーシップ推論では、
まさにその時期による切り分けが分布差として批判される。
**同一の設計が、目的によって長所にも欠陥にもなる。**
サーベイ 7·1 節の「どのような状況を想定した研究なのかを明確にする」という要請の、
最も具体的な帰結である。→ [評価の枠組み](evaluation-framework.md)

**日本語の標準的な評価セットは、この Wiki には無い。**
[ドメインや言語横断](multilingual-and-domain.md) で整理したとおり日本語の実証研究は複数あるが、
WikiMIA / MIMIR に相当する共有ベンチマークは見当たらない。
[文脈長](context-length.md) の日本語での逆転が言語特性か評価セット構成かを切り分けるには、
まさにこの欠落が障害になっている。**明確な知識ギャップ。**

**評価指標の水準にも同種の批判がある。** [Carlini 22](../papers/carlini-2022-first-principles.md) は
AUC のような直接的な指標では不十分であり、低い偽陽性率における真陽性率を
評価すべきだと主張した。データセットの問題（分布差）と指標の問題（AUC）は
独立に存在し、両方を直さないと手法比較は信頼できない。

## 未解決の問い

- MIMIR / OLMoMIA 上で、WikiMIA 時代の手法ランキングを再構築した体系的な研究はあるか
- 「時期で分ける」以外に、訓練セット外のテキストを大量に得る方法はあるか。
  これは正例・負例の分布を揃えるための本質的な制約である
- 日本語のメンバーシップ推論の標準ベンチマークをどう構築するか
  → [ドメインや言語横断](multilingual-and-domain.md)
- 低偽陽性率領域の指標 [Carlini 22](../papers/carlini-2022-first-principles.md) を採用すると、
  手法のランキングはどう変わるか → [メンバーシップ推論](membership-inference.md)
- 攻撃速度を評価軸に含めるべき状況はどこか（コンペティションでの前例）
