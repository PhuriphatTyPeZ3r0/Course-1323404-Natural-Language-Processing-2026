---
tags: [nlp, overview, syllabus]
course: 1323404
course-secondary: 1323326
date: 2026-10-17
instructor: Satida Sookpong
source: "0_Intro_to_the_Class.pdf"
---

# ภาพรวมรายวิชาและการปฐมนิเทศ (Course Overview & Orientation)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week1-MOC|MOC สัปดาห์ 1]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Course Learning Outcomes (CLOs)** — วัตถุประสงค์การเรียนรู้ระดับรายวิชา มุ่งเน้นความเข้าใจหลักการและการเลือกใช้เทคโนโลยี NLP
- **Evaluation & Grading Scale** — เกณฑ์การกระจายคะแนน (สอบ 40%, มินิโปรเจกต์ 40%, งานในชั้น 10%, การเข้าเรียน 10%) และช่วงตัดเกรด A ถึง F
- **Mini-Project (Group Project)** — โครงงานกลุ่ม 6-7 คน ประยุกต์ใช้โมเดลภาษาแก้ปัญหาโจทย์จริง
- **Attendance & Classroom Policy** — กฎการเช็คชื่อตรงเวลา (8:30 / 14:30) และเงื่อนไขการลากิจ/ลาป่วย

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. ข้อมูลรายวิชาเบื้องต้น (Course Information)

| รายการ | รายละเอียด |
| :--- | :--- |
| **รหัสวิชา** | `1323404` (ตามแผนหลักสูตร CAI) / `1323326` (รหัสตามเอกสารสไลด์) |
| **ชื่อวิชา** | การประมวลผลภาษาธรรมชาติ (Natural Language Processing) |
| **วันและเวลาเรียน** | • **Sec 1:** วันเสาร์ เวลา **08:00 – 12:30 น.**<br>• **Sec 2:** วันเสาร์ เวลา **14:00 – 18:30 น.** |
| **ห้องเรียนปฏิบัติการ** | ห้อง **1-0303 Computer & Sound Lab 2** |
| **อาจารย์ผู้สอน** | **อาจารย์ สธิดา สุขพงษ์ (Satida Sookpong)** |
| **Microsoft Teams Code** | • **Sec 1:** `pdm1hti`<br>• **Sec 2:** `k3hlsii` |

### 2. วัตถุประสงค์การเรียนรู้ (Course Learning Outcomes: CLOs)

1. **CLO 1:** อธิบายหลักการเบื้องต้นและทฤษฎีพื้นฐานทางภาษาธรรมชาติและการประมวลผลเชิงคำนวณได้อย่างถูกต้อง
2. **CLO 2:** เลือกใช้สถาปัตยกรรมและเทคโนโลยีการประมวลผลภาษาธรรมชาติ (NLP / LLM Models) เพื่อแก้ไขปัญหาได้อย่างเหมาะสมและมีประสิทธิภาพ

### 3. ขอบเขตเนื้อหาตลอดภาคการศึกษา (Course Outline)

> **คำอธิบายรายวิชา (ตามสไลด์หน้า 4):**  
> *"หลักการคำนวณนำไปสู่พื้นความรู้ของการประมวลผลภาษาธรรมชาติ แบบจำลองภาษา การตัดคำ เอ็นแกรม การฝังคำ การกำกับส่วนของคำพูด การติดป้ายลำดับ แบบจำลองภาษาประสาทวกกลับ แบบจำลอง เข้ารหัส-ถอดรหัส แบบจำลองความสนใจ วากยสัมพันธ์ ต้นไม้ และการวิเคราะห์คำ"*

การคำนวณและทฤษฎีพื้นฐานของ NLP (`Introduction to basic computation of natural language processing`) ประกอบด้วย:
- แบบจำลองภาษา (`Language Model`)
- การตัดคำและการประมวลผลข้อความ (`Tokenization & Word Segmentation`)
- แบบจำลองเอ็นแกรม (`N-gram`)
- การฝังคำในปริภูมิเวกเตอร์ (`Word Embedding`)
- การกำกับส่วนของคำพูด (`Part-of-Speech Tagging`)
- การติดป้ายลำดับและการสกัดเอนทิตี (`Sequence Labelling & NER`)
- แบบจำลองภาษาประสาทวกกลับ (`Recurrent Neural Language Model - RNN/LSTM/GRU`)
- แบบจำลองเข้ารหัส-ถอดรหัส (`Encoder-Decoder Model`)
- แบบจำลองความสนใจ (`Attention Model`)
- วากยสัมพันธ์ ต้นไม้ และการวิเคราะห์คำ (`Syntax Trees and Parsing`)
- สถาปัตยกรรมหม้อแปลงและแบบจำลองภาษาขนาดใหญ่ (`Transformers, LLMs & Multimodal LLMs`)

### 4. สัดส่วนคะแนน (Grading Scheme)

```mermaid
pie title สัดส่วนคะแนนรายวิชา (Total 100%)
    "Mini-Project (โครงงานกลุ่ม)" : 40
    "Final Exam: Paper-based" : 20
    "Final Exam: Lab Practical" : 20
    "Attendance (การเข้าเรียน)" : 10
    "In-class Assignment" : 10
```

| องค์ประกอบคะแนน | สัดส่วน | เงื่อนไขและรายละเอียด |
| :--- | :---: | :--- |
| **Mini-Project** | **40%** | โครงงานกลุ่ม 6-7 คน จัดทำระบบ NLP ประยุกต์ (TBC) |
| **Exam (การสอบวัดผล)** | **40%** | แบ่งเป็น 2 ส่วนเท่ากัน (TBC):<br>• **Paper-based (ทฤษฎี):** 20%<br>• **Lab (ปฏิบัติการเขียนโค้ด):** 20% |
| **In-class assignment** | **10%** | แบบฝึกหัดและงานที่มอบหมายในห้องเรียน |
| **Attendance (การเข้าเรียน)** | **10%** | ความตรงต่อเวลาและระเบียบวินัยในชั้นเรียน |

> [!important] ระเบียบการเช็คชื่อและการลา (Attendance Policy)
> - **เวลาเช็คชื่อ:** เช็คชื่อได้ไม่เกิน **8:30 น.** (สำหรับคาบเช้า Sec 1) และ **14:30 น.** (สำหรับคาบบ่าย Sec 2) หลังจากนี้ถือเป็นสาย/ขาด
> - **การลาป่วย:** ต้องมีเอกสาร **ใบรับรองแพทย์** แนบยืนยันเท่านั้น
> - **การลากิจ:** ต้องแจ้งให้อาจารย์ทราบล่วงหน้าอย่างน้อย 1 วัน (ก่อน **23:59 น.** ของวันก่อนหน้า)
> - **กรณีฉุกเฉิน:** การอนุมัติการลาขึ้นอยู่กับดุลยพินิจของอาจารย์ผู้สอนเป็นรายกรณี

### 5. เกณฑ์การตัดเกรด (Grading Scale)

ระบบตัดเกรดอิงเกณฑ์มาตรฐาน มีช่วงคะแนนดังนี้:

| ช่วงคะแนนรวม | เกรดที่ได้รับ |
| :---: | :---: |
| 80.00 – 100.00 | **A** |
| 75.00 – 79.99 | **B+** |
| 70.00 – 74.99 | **B** |
| 65.00 – 69.99 | **C+** |
| 60.00 – 64.99 | **C** |
| 55.00 – 59.99 | **D+** |
| 40.00 – 54.99 | **D** |
| < 40.00 | **F** |

### 6. โครงงานประจำวิชา (Mini-Project Details)

- **รูปแบบ:** การทำงานร่วมกันเป็นกลุ่มย่อย กลุ่มละ **6 – 7 คน**
- **การจัดกลุ่มตาม Section:**
  - **Sec 1 (นักศึกษา 39 คน):** แบ่งเป็นกลุ่ม 6 คน จำนวน 3 กลุ่ม และกลุ่ม 7 คน จำนวน 3 กลุ่ม
  - **Sec 2 (นักศึกษา 26 คน):** แบ่งเป็นกลุ่ม 6 คน จำนวน 2 กลุ่ม และกลุ่ม 7 คน จำนวน 2 กลุ่ม
- **การส่งงาน:** ลงทะเบียนรายชื่อสมาชิกกลุ่มในช่องทาง Microsoft Teams ตามกลุ่มเรียน (`** Submit members' names in MS Teams **`, หัวข้อโจทย์และรายละเอียดเพิ่มเติม TBC)

### 7. ตารางเรียน 10 สัปดาห์ และกำหนดการสำคัญ (Time Table & Syllabus Schedule)

#### ตารางแผนการเรียนรายสัปดาห์ (10-Week Course Schedule)

| สัปดาห์ | วัน-เดือน-ปี | รหัสบทเรียนและหัวข้อการสอน (Topics) | ลิงก์สรุปบทเรียน |
| :---: | :--- | :--- | :--- |
| **Week 1** | เสาร์ที่ 12 ก.ย. 2026 | • `0` Intro to the Class<br>• `1-1` Intro to NLP<br>• `1-2` Tokenization | [[Week1-MOC]] |
| **Week 2** | เสาร์ที่ 19 ก.ย. 2026 | • `2-1` Word Segmentation, POS Tagging and Sequence Labeling | [[Week2-MOC]] |
| **Week 3** | เสาร์ที่ 26 ก.ย. 2026 | • `3-1` Syntax and Parsing | [[Week3-MOC]] |
| **Week 4** | เสาร์ที่ 3 ต.ค. 2026 | • `4-1` Word Embeddings and Vector Representations | [[Week4-MOC]] |
| **Week 5** | เสาร์ที่ 10 ต.ค. 2026 | • `5-1` Language Models, N-grams<br>• `5-2` Recurrent Neural Networks (RNN) | [[Week5-MOC]] |
| **Week 6** | เสาร์ที่ 17 ต.ค. 2026 | • `6-1` Encoder-Decoder (Seq2Seq)<br>• `6-2` Attention Model | [[Week6-MOC]] |
| **Week 7** | เสาร์ที่ 24 ต.ค. 2026 | • `7-1` Transformer | [[Week7-MOC]] |
| **Week 8** | เสาร์ที่ 31 ต.ค. 2026 | • `8-1` Large Language Models (LLMs) | [[Week8-MOC]] |
| **Week 9** | เสาร์ที่ 7 พ.ย. 2026 | • `9-1` Advanced Applications | [[Week9-MOC]] |
| **Week 10** | เสาร์ที่ 14 พ.ย. 2026 | • `10-1` Multimodal LLMs<br>• `10-2` Project Presentation | [[Week10-MOC]] |

#### กำหนดการสำคัญทางวิชาการ (Important Academic Dates)

| วันที่ / สัปดาห์ | กิจกรรมสำคัญ |
| :--- | :--- |
| **11 กันยายน 2026** | กำหนดการวันสุดท้ายของการ **Drop รายวิชาโดยไม่ติด W** |
| **30 ตุลาคม 2026** | กำหนดการวันสุดท้ายของการ **Drop รายวิชาแบบติด W** |
| **18 – 22 พฤศจิกายน 2026** | สัปดาห์การ **สอบปลายภาค (Final Examination Week)** |

### 8. เอกสารและตำราอ้างอิงหลัก (References)

- **Lee, Raymond. (2023).** *Natural Language Processing : A Textbook with Python Implementation.* Springer, Singapore. [DOI: 10.1007/978-981-99-1999-4](https://doi.org/10.1007/978-981-99-1999-4).
- **Daniel Jurafsky and James H. Martin. (2026).** *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models*, 3rd edition. Online manuscript released January 6, 2026. Available at: [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3).

---

<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[Week1-MOC|เข้าสู่สารบัญสัปดาห์ 1 (Week 1 MOC)]]
