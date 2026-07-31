---
title: モデルサイズ（Model Size）
aliases: [model size, パラメータ数, スケーリング]
axis: モデル
survey_section: "4·2"
tags: [empirical, model, scaling]
type: concept
---

# モデルサイズ：大規模モデルはより多く暗記する

## 定義

パラメータ数と暗記量の関係。3 つの実証的知見のうち**モデル軸**に対応するもの
（[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 4·2）。

[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) は、モデルサイズと暗記量の間に
**ほぼ完全な対数線形関係（R² = 99.8%）**が存在することを示した。
**モデルサイズ 10 倍で暗記量が 19 パーセントポイント増加**し、
同一モデル族内では大きいモデルが小さいモデルの **2〜5 倍**暗記する。
実験は GPT-Neo 系モデル [Black 22]（125M / 1.3B / 2.7B / 6B の 4 種類）を対象とする。

## 主要な論文

- [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) — 対数線形関係を示した原典。逐語暗記の定義に基づく
- [Ippolito 23](../papers/ippolito-2023-false-sense-of-privacy.md) — **近似暗記でも同様の結果**を確認
- [Morris 26](../papers/morris-2026-how-much-memorize.md) — **1 パラメータあたり約 3.6 ビット**という容量を測定。対数線形関係に機序を与える
- [Huang 24] — モデルの一般的な性能と暗記が密接に関係していると考察
- [Lu 24] — 事実の暗記に関するスケーリング則
- [Kiyomaru 24](../papers/kiyomaru-2024-comprehensive-analysis.md) — 日本語でも再現
- [Satvaty 25](../papers/satvaty-2025-language-sensitive.md) — オランダ語・スロベニア語・ポーランド語・チェコ語でも再現

多くの研究が支持: [Chang 25, Chen 25, Huang 22a, Huang 24, Kandpal 22,
Karamolegkou 23, Kiyomaru 24, Lee 23, Lu 24, McCoy 23]。

## 横断的知見

**3 因子のうち、唯一データセット・モデル族を跨いで綺麗に一般化する。**
[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) の追試節が明示している
（「this is indeed true for model scale」）。T5 / C4（マスク型）でも
OPT / 整理済み Pile でも傾向は再現した。対照的に
[文字列の重複](string-duplication.md)は T5 で単調性を失い、
[文脈長](context-length.md)は日本語で符号が反転する。
**普遍的要因の最有力候補はモデルサイズである。**

ただし**絶対量は設定で大きく変わる**。マスク型の T5 は因果型より 1 桁少なく
（T5-XL 3B: 3.5% vs GPT-Neo 2.7B: 53.6%、100 回重複時）、
OPT は 66B でも 125M GPT-Neo より Pile の暗記が少ない。
つまり「大きいほど暗記する」は族内の傾向であって、
**族を跨いだ絶対量の比較には使えない**。

**「暗記であって汎化ではない」ことの直接的な証拠がある。**
[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) は同規模の GPT-2（Pile 未学習）を
ベースラインに置き、GPT-2 が **6%** しか正解できないのに対し
同規模の GPT-Neo 1.3B が **40%** 正解することを示した。
GPT-2 が当てられた例は数列や定型句などの「つまらない」系列だった。
この対照実験があるため、対数線形関係を「大きいモデルは予測が上手いだけ」で
説明することはできない。→ [暗記](memorization.md)

**「なぜ大きいほど暗記するのか」に容量という答えが出た（2026-07-31 追記）。**
[Morris 26](../papers/morris-2026-how-much-memorize.md) は、汎化の余地を消した
一様ランダムなビット列で学習することで、GPT 系 Transformer が
**1 パラメータあたり 3.5〜4 ビット**（半精度で α = 3.64）を格納できると測定した。

容量がパラメータ数に比例するなら、暗記量がモデルサイズとともに増えるのは当然である。
さらにこの描像は**上限**も与える——モデルは容量が埋まるまで暗記し、
埋まると意図せぬ暗記は**減少に転じる**（grokking）。
[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) の対数線形関係は、
**容量が飽和していない領域での観測**だったと読み直せる。

ただし [Morris 26](../papers/morris-2026-how-much-memorize.md) が自前で学習したのは
1.5B までであり、フロンティア規模への適用はスケーリング則による外挿である。

**それでも「性能が上がる」の副産物かもしれない。**
[Huang 24] の考察が最も説明力が高い。モデルサイズが暗記と関連するのは、
一般にモデルサイズが大きいほど**性能が高まる**ためと解釈できる。
この解釈を採ると、モデルサイズは重複や文脈長と同列の「暗記の原因」ではなく、
**能力一般の代理変数**ということになる。
[暗記](memorization.md) の「暗記は排除すべき対象ではない」という規範的論点は、ここに根拠を持つ——
暗記を減らすためにモデルを小さくすることは、有用性を直接削ることを意味する。

**定義を緩めても関係は崩れない。** [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) は
逐語暗記、[Ippolito 23](../papers/ippolito-2023-false-sense-of-privacy.md) は
BLEU ベースの近似暗記で同じ傾向を得た。
後者は逐語暗記を完全阻止する防御（MemFree）を有効にした状態でも
「大きいモデルほど正解後続に近い」ことを確認している。
3 因子の中で、**定義への頑健性が最も明確に確認されている**のはモデルサイズである。
（[重複](string-duplication.md)は複数の定量化手法で再現され、
[文脈長](context-length.md)は言語によって逆転する。）

**言語横断でも再現される数少ない知見。** [Satvaty 25](../papers/satvaty-2025-language-sensitive.md) は
低資源言語を含む複数言語でモデルサイズの知見が再現されたと報告している。
[Kiyomaru 24](../papers/kiyomaru-2024-comprehensive-analysis.md) は日本語でも再現を確認した。
[文字列の重複](string-duplication.md) と並び、**普遍的要因の候補**である。

**[PEFT による抑制](mitigation-in-training.md)はこの知見の系である。** [Hong 25a] は
LoRA に代表される PEFT で訓練データの暗記が抑制されると報告した。
PEFT では**学習対象のモデルのパラメータ数が小さくなる**ため、
モデルサイズと暗記の相関という実証的知見と合致する。
つまり抑制手法（5·2）が実証的知見（4·2）から導出されている好例であり、
サーベイ図1 の「3章→4章→5章」という流れが実際に機能していることを示す。

## 未解決の問い

- 対数線形関係は 6B を大きく超える規模（数百 B〜）でも維持されるか。
  主実験は最大 6B。追試の OPT は 66B まで傾向を再現したが**効果の大きさが数桁小さい**ため、
  規模の外挿とデータ整理の効果が交絡している。論文自身が
  「現在の最先端モデルは 6B の 200 倍以上のパラメータを持つ」と留保している
- OPT の結果は (a) 丁寧なデータ整理で暗記を緩和できる のか
  (b) わずかな分布の差で暗記される内容が変わる のか。
  [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) は**区別できないとしている**
- [Huang 24] の「性能の副産物」説が正しいなら、**同じ性能で暗記量だけ少ないモデル**は
  原理的に作れるのか。それとも性能と暗記のトレードオフは不可避か
- 混合エキスパート（MoE）のように総パラメータ数と活性パラメータ数が乖離するモデルでは、
  どちらが暗記量を規定するか（Wiki 未回答）
- PEFT による抑制 [Hong 25a] は、パラメータ数の減少で説明しきれるか。
  それとも凍結された事前学習パラメータ側の寄与があるか
