---
title: LangGraph
date: 2026-04-13
tags: [ai-agents, framework, langchain, graph]
type: concept
sources: [raw/articles/dr-ryan-ahmed-ai-agent-roadmap.md]
---

# LangGraph

## Overview

LangChain ekibinin geliştirdiği, ajan iş akışlarını **yönlü graf** (DAG) olarak modelleyen framework. Döngüsel ve koşullu akışlar desteklenir.

## Temel Özellikler

- **State Machine**: Her node bir state üzerinde çalışır
- **Edges**: Koşullu geçişler (conditional edges)
- **Checkpointing**: Durum kaydı ve geri alma
- **Human-in-the-loop**: İnsan onayı noktaları

## [[CrewAI]] ile Farkı

| | LangGraph | CrewAI |
|---|---|---|
| Yaklaşım | Graf/state machine | Role-based crew |
| Esneklik | Yüksek (custom flow) | Hazır yapı |
| Öğrenme eğrisi | Dik | Düz |

## İlişkili Kavramlar

- [[CrewAI]]
- [[AutoGen]]
- [[agentic-workflows]]

## Kaynaklar

- [[2026-04-12-dr-ryan-ahmed-ai-agent-roadmap]]
