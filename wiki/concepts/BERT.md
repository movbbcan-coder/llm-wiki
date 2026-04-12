---
title: BERT
date: 2026-04-13
tags: [llm, transformer, nlp, google]
type: concept
sources: [raw/articles/attention-mechanism.md]
---

# BERT — Bidirectional Encoder Representations from Transformers

## Overview

Google tarafından 2018'de yayımlanan [[Transformer]] tabanlı dil modeli. Çift yönlü encoder mimarisi kullanır — cümleyi hem soldan sağa hem sağdan sola aynı anda işler.

## Temel Özellikler

- **Bidirectional**: Her token için bağlamı her iki yönden kullanır
- **Pre-training**: Masked Language Modeling (MLM) + Next Sentence Prediction (NSP)
- **Fine-tuning**: QA, NER, sınıflandırma görevlerine adapte edilir

## [[Transformer]] ile İlişkisi

BERT yalnızca [[Transformer]]'ın encoder kısmını kullanır. [[GPT]] ise decoder kısmını kullanır.

## İlişkili Kavramlar

- [[Transformer]]
- [[Attention Mechanism]]
- [[GPT]]
- [[Vaswani]]

## Kaynaklar

- [[2026-04-11-attention-mechanism]]
