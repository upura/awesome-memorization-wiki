---
title: 知識編集（Knowledge Editing）
aliases: [knowledge editing, 知識編集, model editing, モデル融合]
axis: モデル
survey_section: "5·2"
tags: [mitigation, model, interpretability]
type: concept
---

# 知識編集（Knowledge Editing）

## 定義

学習済みモデルの**パラメータに対する編集** [Wang 24a] を暗記の抑制に活用する手法
（[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 5·2）。
[Hartvigsen 23], [Kassem 25], [Meng 23], [Ruzzetti 25] が該当する。

再学習せずに特定の知識だけを書き換える点で、[逆学習](machine-unlearning.md)より
局所的な介入である。

## 主要な論文

- [Wang 24a] — 知識編集のサーベイ（ACM Computing Surveys）
- [Meng 23] — Transformer 内の記憶の一括編集（MEMIT）
- [Hartvigsen 23] — 離散キー・バリューアダプタによる生涯モデル編集（GRACE）
- [Ruzzetti 25] — **Private Memorization Editing**: 暗記を防御に転じてデータプライバシを強化する
- [Menta 25] — モデル寄与度の観点から、**暗記や汎化に寄与しているモデル構造**を分析
- [Zaman 24] — 学習済みモデルのパラメータを**混ぜ合わせる**ことでプライバシ懸念に対処（モデル融合）

## 横断的知見

**この系統だけが「暗記がどこに宿るか」を問うている。** サーベイの他の抑制手法は
暗記量をブラックボックス的に増減させるが、[Menta 25] は
暗記や汎化に寄与しているモデル構造そのものを分析する。
これは [暗記と汎化の区別](memorization-vs-generalization.md)という 7·1 節の問いに、
**モデル内部の局在という形で答えを与えうる**数少ない経路である。
[Hong 25b] が推論と暗記の相互作用を単一の方向（direction）が媒介すると報告したのも同じ路線にある。
→ 画像生成では [Hintersdorf 24] が暗記を担うニューロンの局在を報告しており
（[研究領域の拡張](multimodal-memorization.md)）、モダリティ横断で同じ問いが立っている。

**「暗記を防御に転じる」という反転がある。** [Ruzzetti 25] の Private Memorization Editing は、
暗記を除去すべき欠陥としてではなく、**編集の足がかり**として使う。
これは [暗記](memorization.md) の「暗記は常に排除すべき対象ではない」という
サーベイ 7·1 節の規範的主張と方向を同じくする、数少ない具体的手法である。

**局所編集は、暗記の分散性という前提と衝突しうる。**
知識編集は「特定の知識が特定のパラメータに局在する」ことを暗黙に前提とする。
しかし [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) が示した[重複](string-duplication.md)の効果や
[モデルサイズ](model-size.md)との対数線形関係は、
暗記が規模に比例して分散的に蓄積される像を示唆する。
局所編集が有効な範囲（事実的知識）と、逐語的な長文の暗記が同じ機構かは、
この Wiki では未確認である（推測）。

## 未解決の問い

- 知識編集で除去した内容は、[メンバーシップ推論](membership-inference.md) で検出されなくなるか。
  [逆学習](machine-unlearning.md) と同様、「検出されない」と「消えた」の区別が必要
- 事実的知識の編集と、長い文字列の逐語暗記の除去は同じ手法で扱えるか
- [Menta 25] の構造分析は、[モデルサイズ](model-size.md) を変えても同じ局在を示すか
- モデル融合 [Zaman 24] は暗記を平均化して薄めるだけか、除去するのか
- 編集の累積は性能を劣化させるか（生涯編集 [Hartvigsen 23] の限界）
