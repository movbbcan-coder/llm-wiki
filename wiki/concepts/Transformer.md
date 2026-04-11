---
title: Transformer
date: 2026-04-11
tags: [architecture, deep-learning, nlp]
type: concept
---

# Transformer

## Overview

The **Transformer** is a neural network architecture introduced by [[Vaswani]] et al. in 2017 in the paper "Attention Is All You Need". It relies entirely on [[Attention Mechanism]] (specifically [[Self-Attention]]) without using recurrence.

## Key Innovation

Unlike RNNs/LSTMs, Transformers process sequences in parallel using [[Self-Attention]] and [[Multi-Head Attention]], leading to:
- Faster training
- Better handling of long-range dependencies
- State-of-the-art performance across many tasks

## Impact

The Transformer architecture became the foundation for:
- [[BERT]] (Bidirectional Encoder Representations from Transformers)
- [[GPT]] (Generative Pre-trained Transformer)
- Modern large language models

## Related Concepts

- [[Attention Mechanism]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[BERT]]
- [[GPT]]

## Sources

- [[2026-04-11-attention-mechanism]]
