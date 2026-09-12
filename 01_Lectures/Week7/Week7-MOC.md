---
tags: [nlp, week7, moc]
course: 1323404
course-name: Natural Language Processing (การประมวลผลภาษาธรรมชาติ)
week: 7
date: 2026-09-12
instructor: Phuriphat Hemakul
source: "7-1_Transformer.pptx"
---

# Week 7 — The Transformer (MOC)

<span class="material-symbols-outlined">arrow_back</span> สัปดาห์ก่อนหน้า: [[Week6-MOC|MOC สัปดาห์ 6]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทบทวนกลไก Attention (Query/Key/Value, Bahdanau/Luong) จากสัปดาห์ที่แล้ว เพราะ self-attention ต่อยอดจากแนวคิดเดียวกัน — ดู [[Attention-Mechanism]]
- [ ] ทบทวนพื้นฐาน softmax และ dot product เพื่อเข้าใจสูตร Scaled Dot-Product Attention — ดู [[Transformer]]
- [ ] เตรียมทำความเข้าใจ residual connection และ layer normalization ที่ใช้กับโครงข่ายลึกหลายสิบชั้น — ดู [[Transformer]]
- [ ] ลองเปิดดูโมเดล `bert-base-uncased` และ `gpt2` บน Hugging Face เพื่อเห็นตัวอย่าง Transformer จริงก่อนเข้าเรียน — ดู [[Transformer]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 7 (สรุปย่อ)

สัปดาห์นี้เป็นบทเรียนหลัก 3 ชั่วโมงแบ่งเป็นสองภาค ภาคแรก (Lecture A) ปูพื้นฐาน **Self-Attention และ Multi-Head Attention** ตั้งแต่ข้อจำกัดของ RNN, สูตร scaled dot-product attention, เหตุผลของการ scale ด้วย $\sqrt{d_k}$, multi-head attention, positional encoding และ masked self-attention สำหรับ decoding แบบ autoregressive ภาคที่สอง (Lecture B) ประกอบร่างเป็น **สถาปัตยกรรม Encoder-Decoder แบบเต็มรูปแบบ** ที่มี residual connection, layer normalization, cross-attention เชื่อม encoder กับ decoder, การฝึกและการอนุมานอย่างมีประสิทธิภาพ (KV-cache, byte-level BPE) และปิดท้ายด้วยตระกูลโมเดล Transformer สามสาย (encoder-only อย่าง BERT, decoder-only อย่าง GPT, encoder-decoder อย่าง T5) พร้อม scaling laws ที่นำไปสู่ LLM ขนาดใหญ่ในสัปดาห์ถัดไป

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 7

```mermaid
graph TD
    MOC[Week 7: The Transformer] --> A[[Transformer]]

    A --> A1[Self-Attention และ Scaled Dot-Product Attention]
    A --> A2[Multi-Head Attention และ Positional Encoding]
    A --> A3[Encoder-Decoder Stack และ Cross-Attention]
    A --> A4[Training/Inference Efficiency และ Transformer Variants]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| --- | --- | --- |
| [[Transformer]] | Self-attention, scaled dot-product attention, multi-head attention, positional encoding, masking, สถาปัตยกรรม encoder-decoder เต็มรูปแบบ, cross-attention, training/inference efficiency, ตระกูล BERT/GPT/T5, scaling laws | สไลด์ 1-43 (Lecture A + Lecture B) |

> [!tip] จุดที่มักสับสน
> อย่าสับสนระหว่าง self-attention (Q/K/V มาจากลำดับเดียวกัน ใช้ในทั้ง encoder และ masked-decoder) กับ cross-attention (Q มาจาก decoder แต่ K/V มาจาก encoder) — ทั้งสองอยู่ในสถาปัตยกรรมเดียวกันแต่ทำหน้าที่ต่างกันคนละจุด

<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week8-MOC|MOC สัปดาห์ 8]]
