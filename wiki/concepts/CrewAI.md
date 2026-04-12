---
title: CrewAI
date: 2026-04-13
tags: [ai-agents, framework, multi-agent]
type: concept
sources: [raw/articles/dr-ryan-ahmed-ai-agent-roadmap.md]
---

# CrewAI

## Overview

Çok ajanlı (multi-agent) AI sistemleri kurmak için Python framework. Roller, görevler ve araçlar tanımlanarak ajanlara koordineli çalışma sağlar.

## Temel Kavramlar

- **Crew**: Birlikte çalışan ajan grubu
- **Agent**: Rol + hedef + araç seti olan birim
- **Task**: Ajana verilen görev
- **Process**: Sequential / Hierarchical

## [[agentic-workflows]] ile İlişkisi

CrewAI, [[agentic-workflows]] prensiplerini multi-agent seviyeye taşır — her ajan kendi döngüsünde çalışır, çıktılar diğer ajanlara aktarılır.

## İlişkili Kavramlar

- [[LangGraph]]
- [[AutoGen]]
- [[agentic-workflows]]

## Kaynaklar

- [[2026-04-12-dr-ryan-ahmed-ai-agent-roadmap]]
