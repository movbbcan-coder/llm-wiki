---
title: Attention Mechanism
date: 2026-04-13
tags: [neural-networks, deep-learning, nlp]
type: concept
sources: [raw/articles/attention-mechanism.md]
---

# Attention Mechanism

## Overview

Nöral ağlarda, özellikle dizi-dizi modellerinde kullanılan; modelin çıktı üretirken girdinin farklı bölümlerine odaklanmasını sağlayan teknik.

## Temel Bileşenler

- **Query**: Ne aradığımız
- **Key**: Elimizde ne var
- **Value**: Almak istediğimiz gerçek bilgi

Çıktı = softmax(QKᵀ/√d) · V

## Tarihsel Gelişim

- **2014**: [[Bahdanau]] et al. — nöral makine çevirisi için önerildi
- **2017**: [[Vaswani]] et al. — "Attention Is All You Need" ile [[Transformer]] mimarisinin temeli oldu

## İlişkili Kavramlar

- [[Self-Attention]]
- [[Multi-Head-Attention]]
- [[Transformer]]
- [[BERT]]
- [[GPT]]

## Kaynaklar

- [[2026-04-11-attention-mechanism]]
