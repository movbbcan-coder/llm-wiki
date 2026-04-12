---
title: Agentic Workflows (Ajan İş Akışları)
date: 2026-04-12
tags: [concept, ai-agent, workflow, optimization]
sources: [Dr. Ryan Ahmed, Andrew Ng]
---

# Agentic Workflows (Ajan İş Akışları)

Ajan iş akışları, yapay zekanın tek seferlik bir prompt ile cevap vermesi yerine, adım adım ve kendi kendini düzelten döngüler (Iterative Design) ile çalışması prensibidir.

## 📋 Temel Bileşenler

1. **Reflection (Yansıma):** Ajanın bir çözüm ürettikten sonra o çözümü eleştirmesi ve "Nasıl daha iyi yapabilirim?" diye sorması.
2. **Tool Use (Araç Kullanımı):** Ajanın metin üretmekle kalmayıp, internetten araştırma yapması, kod çalıştırması veya API çağırması.
3. **Planning (Planlama):** Karmaşık bir görevin alt görevlere (Sub-tasks) bölünmesi ve bir yol haritası (Roadmap) oluşturulması.
4. **Multi-Agent Collaboration (Çoklu Ajan İşbirliği):** Birden fazla ajanın (örneğin: Tasarımcı, Geliştirici, Denetçi) birbirlerinin çıktılarını kullanarak ortak hedefe ulaşması.

## ⚙️ CEO Bot Uygulaması

CEO Bot altyapımız bu prensibi şu şekilde kullanır:
- **Decision Router:** Görevleri analiz eder ve hangi uzman modele (veya ajana) gideceğine karar verir.
- **Obsidian Memory:** Ajanın geçmiş kararlarını hatırlar ve yeni kararlarını buna göre şekillendirir.
- **Self-Correction:** Kod yazarken hata aldığında terminal çıktılarını okuyarak hatayı düzeltmeye çalışır (Mevcut yetenek).

## 🔗 İlgili Kavramlar

- [[Transformer]] — Temel mimari.
- [[CrewAI]] — Çoklu ajan orkestrasyon framework'ü.
- [[LangGraph]] — Graf tabanlı ajan iş akışları.

## 📉 Gelişim Notları
Dr. Ryan Ahmed'in roadmap'ine göre 2026'da ajanlar sadece cevap vermeyecek, "Autonomous Self-Optimization" (Otonom Kendi Kendini İyileştirme) aşamasına geçecekler.
