---
title: AutoGen
date: 2026-04-13
tags: [ai-agents, framework, microsoft, multi-agent]
type: concept
sources: [raw/articles/dr-ryan-ahmed-ai-agent-roadmap.md]
---

# AutoGen

## Overview

Microsoft Research tarafından geliştirilen multi-agent konuşma framework'ü. Ajanlar birbirleriyle mesajlaşarak görevleri çözer.

## Temel Özellikler

- **ConversableAgent**: Mesaj alıp gönderebilen temel ajan tipi
- **AssistantAgent**: LLM tabanlı ajan
- **UserProxyAgent**: İnsan veya kod çalıştırıcı ajan
- **GroupChat**: Birden fazla ajanın katıldığı sohbet

## [[CrewAI]] ve [[LangGraph]] ile Farkı

AutoGen konuşma/diyalog odaklıdır; ajanlar tartışarak sonuca ulaşır. CrewAI rol odaklı, LangGraph graf/akış odaklıdır.

## İlişkili Kavramlar

- [[CrewAI]]
- [[LangGraph]]
- [[agentic-workflows]]

## Kaynaklar

- [[2026-04-12-dr-ryan-ahmed-ai-agent-roadmap]]
