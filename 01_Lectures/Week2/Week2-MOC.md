---
tags: [nlp, week2, moc]
course: 1323404
course-name: Natural Language Processing (การประมวลผลภาษาธรรมชาติ)
week: 2
date: 2026-09-12
instructor: Phuriphat Hemakul
source: "2-1_Word_Segmentation_POS_Tagging_Sequence_Labeling.pptx"
---

# Week 2 — Word Segmentation, POS Tagging & Sequence Labeling (MOC)

<span class="material-symbols-outlined">arrow_back</span> สัปดาห์ก่อนหน้า: [[Week1-MOC|MOC สัปดาห์ 1]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทบทวนวิธี tokenization และการตัดคำภาษาไทยจาก Week 1 เพราะ word segmentation คือก้าวถัดไป — ดู [[Word-Segmentation-POS-Tagging-Sequence-Labeling]]
- [ ] ทบทวนแนวคิด conditional probability พื้นฐาน ก่อนเรียน Hidden Markov Model
- [ ] เข้าใจว่าทำไมคำอย่าง "flies" ถึงกำกวมทาง POS ได้ — ดู [[Word-Segmentation-POS-Tagging-Sequence-Labeling]]
- [ ] ลองนึกภาพว่า BIO scheme กำกับ entity ในประโยคหนึ่งอย่างไร

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 2 (สรุปย่อ)

สัปดาห์นี้ต่อยอดจากการตัดคำในสัปดาห์ 1 ไปสู่การวิเคราะห์โครงสร้างไวยากรณ์ระดับคำ แบ่งเป็น 3 ส่วน: (1) **Word Segmentation** — ทบทวนแนวทาง dictionary-based, rule-based และ statistical/ML-based สำหรับภาษาที่ไม่มีช่องว่างระหว่างคำ (2) **POS Tagging** — ตั้งแต่วิธีใช้ความรู้ภาษาศาสตร์ (knowledge-based) ไปจนถึงวิธีเชิงสถิติอย่าง Hidden Markov Model (HMM), Viterbi decoding และ Conditional Random Field (CRF) และ (3) **Sequence Labeling** — กรอบคิดทั่วไปที่ครอบคลุมทั้ง POS tagging และ Named Entity Recognition (NER) ผ่าน BIO tagging scheme ทั้งสามหัวข้อนี้ใช้กลไกทางคณิตศาสตร์ร่วมกัน (HMM/CRF/Viterbi) จึงถูกจัดรวมไว้ในโน้ตเดียวกัน

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 2

```mermaid
graph TD
    MOC[Week 2: Word Segmentation, POS Tagging & Sequence Labeling] --> A[[Word-Segmentation-POS-Tagging-Sequence-Labeling]]

    A --> A1[Word Segmentation: Dictionary / Rule / Statistical]
    A --> A2[POS Tagging: Knowledge-based, HMM, Viterbi, CRF]
    A --> A3[Sequence Labeling & NER: BIO scheme]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| --- | --- | --- |
| [[Word-Segmentation-POS-Tagging-Sequence-Labeling]] | Word segmentation, POS tagging (knowledge-based, HMM, Viterbi, CRF), sequence labeling & NER (BIO scheme) | 1-10 |

> [!tip] จุดที่มักสับสน
> HMM, Viterbi และ CRF ไม่ใช่สามเรื่องแยกกัน — **HMM คือโมเดลความน่าจะเป็น**, **Viterbi คืออัลกอริทึมที่ใช้หาคำตอบจากโมเดลนั้น** และ **CRF คือโมเดลทางเลือกที่แก้ข้อจำกัดของ HMM** ทั้งสามอย่างล้วนถูกใช้แก้ปัญหาเดียวกันคือ sequence labeling

<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week3-MOC|MOC สัปดาห์ 3]]
