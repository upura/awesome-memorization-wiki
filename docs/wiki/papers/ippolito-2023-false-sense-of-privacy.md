---
title: Preventing generation of verbatim memorization in language models gives a false sense of privacy
authors: [Daphne Ippolito, Florian Tramèr, Milad Nasr, et al.]
year: 2023
venue: INLG 2023, pp. 28–53
citekey: Ippolito 23
tags: [mitigation, critique, approximate-memorization, output]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Preventing generation of verbatim memorization gives a false sense of privacy

## TL;DR

逐語暗記の生成を防いでも**偽りの安心感**しか得られない。
近似暗記（言い換え・並び替え）は素通りする。
同時に、近似暗記の定義でも [モデルサイズ](../concepts/model-size.md) の知見が再現されることを確認した。

## 位置づけ

出力軸。5·3 節（後処理による抑制）への最も強い批判であり、
同時に 3·2§1（[近似暗記](../concepts/string-similarity-memorization.md)の定義）と
4·2（[モデルサイズ](../concepts/model-size.md)）の両方に寄与する。

## 手法・実験

暗記の類似度指標に **BLEU スコア**を用いた（[Lee 22](lee-2022-deduplicating.md) のトークン一致率と対比）。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- **逐語暗記のフィルタリングは防御として不十分である**。言い換え・並び替えを経た
  近似暗記が残る → [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)
- **近似暗記でもモデルサイズとの関係が再現される**。
  定義を緩めても実証的知見の骨格は崩れない → [モデルサイズ](../concepts/model-size.md)
- トークン分割が暗記の測定に影響している可能性を指摘（サーベイ 7·2 節が引用）
  → [ドメインや言語横断](../concepts/multilingual-and-domain.md)
- 画像生成や剽窃検出といった研究領域での知見が、**暗記の定義の改善に資する**と主張
  （サーベイ 7·3 節）→ [研究領域の拡張](../concepts/multimodal-memorization.md)

## 限界・批判

- 「逐語フィルタリングは不十分」は示すが、**近似暗記まで捕捉する実用的なフィルタリング**を
  提供するものではない。この Wiki の未解決の問いとして残っている

## Wiki 内の接点

- [文字列の類似度](../concepts/string-similarity-memorization.md) / [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md) / [モデルサイズ](../concepts/model-size.md)
- [研究領域の拡張](../concepts/multimodal-memorization.md) / [ドメインや言語横断](../concepts/multilingual-and-domain.md)
- 逐語暗記の原典: [Carlini 23b](carlini-2023-quantifying-memorization.md)
- 本論文を引用している概念: [評価の枠組み](../concepts/evaluation-framework.md) / [逆学習](../concepts/machine-unlearning.md)
