---
tags: [nlp, week1, moc]
course: 1323404
course-secondary: 1323326
course-name: Natural Language Processing (การประมวลผลภาษาธรรมชาติ)
week: 1
date: 2026-10-17
instructor: Satida Sookpong
source: "0_Intro_to_the_Class.pdf, 1-1_Intro_to_NLP.pdf, 1-2_Tokenization.pdf"
---

# Week 1 — Introduction to NLP & Tokenization (MOC)

<span class="material-symbols-outlined">menu_book</span> เอกสารปฐมนิเทศและภาพรวมรายวิชา: [[Course-Overview|ประมวลรายวิชา เกณฑ์คะแนน ตารางเรียน 10 สัปดาห์ และโครงงาน (Course Overview)]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] อ่านข้อกำหนดวิชา เกณฑ์การตัดเกรด การเข้าเรียน ตารางเรียน 10 สัปดาห์ และข้อกำหนด Mini-Project — ดู [[Course-Overview]]
- [ ] ทบทวนว่า NLP ประกอบด้วย 3 ศาสตร์อะไรบ้าง และประวัติศาสตร์ 6 Stages ตั้งแต่ Rule-based สู่ ยุค Modern LLM — ดู [[Intro-to-NLP]]
- [ ] เปรียบเทียบโครงสร้างภาษาศาสตร์ 6 ระดับชั้น (Phonetics $\to$ Pragmatics) กับ 5 ขั้นตอนการวิเคราะห์ใน NLP (Lexical $\to$ Pragmatic Analysis) — ดู [[Intro-to-NLP]]
- [ ] ทำความเข้าใจ 5 ความท้าทายหลักของ NLP พร้อมกรณีศึกษาภาษาไทย ("สวยกี่โมง", "กับข้าว", "ไปสบาย", วรรณยุกต์ 7 คำ, "ไปส่งกินข้าวหน่อย") — ดู [[Intro-to-NLP]]
- [ ] เข้าใจความแตกต่างระหว่าง Upstream vs Downstream Tasks, สถาปัตยกรรม NLU / KAI / NLG และ 7 ระบบ NLP ในชีวิตประจำวัน — ดู [[Intro-to-NLP]]
- [ ] แยกแยะหน่วยพื้นฐานของข้อความ: Corpus, Token vs Type, Word Form, Morpheme และ Stem vs Lemma — ดู [[Tokenization]]
- [ ] เข้าใจขั้นตอน Text Normalization 5 ขั้นตอน, การประยุกต์ใช้ Regex และ Penn Treebank Tokenization — ดู [[Tokenization]]
- [ ] ฝึกคำนวณการเทรน BPE ทีละขั้นตอนจากคลังคำตัวอย่าง (`new`, `renew`, `set`, `reset`) และเข้าใจข้อดีของ Byte-level BPE บน UTF-8 — ดู [[Tokenization]]
- [ ] เปรียบเทียบความแตกต่างระหว่าง BPE, WordPiece และ Unigram LM (SentencePiece) — ดู [[Tokenization]]
- [ ] ทำความเข้าใจว่าทำไมภาษาไทยถึงตัดคำยาก (No Whitespace Boundary) และการใช้ Longest Matching (FMM/BMM) / PyThaiNLP — ดู [[Tokenization]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 1 (สรุปย่อ)

สัปดาห์แรกของวิชาปูพื้นฐานสำคัญ 2 ส่วนหลัก:
1. **ภาพรวมของ NLP (Introduction to NLP):** นิยามที่เกิดจากจุดตัดของ 3 ศาสตร์ (ภาษาศาสตร์, วิทยาการคอมพิวเตอร์, AI), วิวัฒนาการ 6 ยุคสมัย (Machine Translation, Early AI, Grammatical Logic, ML/Corpus, Deep Networks สู่ Transformer & Modern LLMs), โครงสร้างภาษาศาสตร์ 6 ระดับคู่กับ 5 ขั้นตอนการประมวลผล NLP, ความท้าทายหลัก 5 มิติพร้อมกรณีศึกษาภาษาไทย, สถาปัตยกรรม NLU/KAI/NLG, งาน Upstream vs Downstream, การประยุกต์ใช้งานจริง 7 ระบบ และเครื่องมือมาตรฐาน (NLTK, spaCy, PyThaiNLP, Hugging Face)
2. **การตัดคำและการปรับมาตรฐานข้อความ (Tokenization & Normalization):** ระดับการแทนข้อมูลข้อความ 4 รูปแบบ (Words, Morphemes, Unicode, Subwords), นิยามหน่วยพื้นฐาน (Corpus, Token vs Type, Word Form, Stem vs Lemma), ความสำคัญของ Tokenization (1 Token $\neq$ 1 Word), ข้อจำกัดของ Word-based และ Character-based, ไปป์ไลน์ Normalization 5 ขั้นตอน, Regex เบื้องต้น, การเจาะลึกอัลกอริทึม Subword (การฝึก BPE ทีละขั้น, BPE Encoding, Byte-Level BPE ไร้ OOV บน UTF-8) พร้อมตารางเปรียบเทียบ BPE vs WordPiece vs Unigram LM และความท้าทายของการตัดคำภาษาไทย (Dictionary-based, FMM/BMM, PyThaiNLP)

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 1

```mermaid
graph TD
    MOC[Week 1: Intro to NLP & Tokenization] --> S[[Course-Overview]]
    MOC --> A[[Intro-to-NLP]]
    MOC --> B[[Tokenization]]

    S --> S1[เกณฑ์คะแนนและตัดเกรด A-F]
    S --> S2[โครงงานกลุ่ม Mini-Project]
    S --> S3[ตารางเรียน 10 สัปดาห์ & วันสอบ]

    A --> A1[นิยาม NLP และวิวัฒนาการ 6 Stages]
    A --> A2[6 Linguistic Levels & 5 NLP Steps]
    A --> A3[5 ความท้าทายและกรณีศึกษาภาษาไทย]
    A --> A4[NLU / KAI / NLG & Upstream-Downstream]
    A --> A5[NLP Applications & Libraries]

    B --> B1[Text Units: Corpus, Token, Type, Lemma]
    B --> B2[Normalization & Regex Cheat Sheet]
    B --> B3[BPE Step-by-Step & Byte-Level BPE]
    B --> B4[BPE vs WordPiece vs Unigram LM]
    B --> B5[Thai Word Segmentation & PyThaiNLP]

    style MOC fill:#2b6cb0,color:#fff
    style S fill:#805ad5,color:#fff
    style A fill:#38a169,color:#fff
    style B fill:#dd6b20,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | แหล่งอ้างอิงต้นฉบับ |
| :--- | :--- | :---: |
| [[Course-Overview]] | ประมวลรายวิชา, CLOs, สัดส่วนคะแนน (Exam 40%, Mini-Project 40%), กฎการเช็คชื่อ, ตารางเรียน 10 สัปดาห์ | `0_Intro_to_the_Class.pdf` (หน้า 1–10) |
| [[Intro-to-NLP]] | นิยาม NLP, 6 Stages วิวัฒนาการ, 6 ระดับภาษา & 5 Steps, ความท้าทายภาษาไทย, NLU/KAI/NLG, Applications, เครื่องมือ | `1-1_Intro_to_NLP.pdf` (หน้า 1–33) |
| [[Tokenization]] | หน่วยพื้นฐาน (Token/Type/Lemma), Normalization 5 ขั้น, Regex, คำนวณ BPE step-by-step, Byte-level BPE, ตัดคำไทย | `1-2_Tokenization.pdf` (หน้า 1–15) |

> [!tip] แอบดูสัปดาห์หน้า
> สัปดาห์ 2 จะต่อยอดจาก Word Segmentation ในสัปดาห์นี้ไปสู่การตัดคำเชิงสถิติ, การกำกับชนิดคำ (POS Tagging) ด้วย Rule-based, HMM (Viterbi) และ Linear-chain CRF ตลอดจนการทำ Sequence Labeling สำหรับ Named Entity Recognition (NER) บนข้อความภาษาไทย

---

<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week2-MOC|MOC สัปดาห์ 2]]
