# 1323404 Natural Language Processing (การประมวลผลภาษาธรรมชาติ)

<div align="center">

[![Institution: PIM](https://img.shields.io/badge/Institution-PIM-003366?style=for-the-badge&logo=google-classroom&logoColor=white)](https://www.pim.ac.th/)
[![Program: CAI](https://img.shields.io/badge/Program-CAI-blue?style=for-the-badge)](https://www.pim.ac.th/)
[![Academic Year](https://img.shields.io/badge/Academic%20Year-1%2F2569%20(2026)-orange?style=for-the-badge)](https://github.com/PhuriphatTyPeZ3r0)
[![Grade](https://img.shields.io/badge/Status-In%20Progress%20(กำลังศึกษา)-yellow?style=for-the-badge)](https://github.com/PhuriphatTyPeZ3r0)
[![Obsidian Compatible](https://img.shields.io/badge/Obsidian-Vault%20Ready-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)](https://obsidian.md/)

**คลังสรุปเนื้อหา แบบฝึกหัด โมเดลภาษา โครงงาน และแนวข้อสอบประจำรายวิชา**  
*สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI) — สถาบันการจัดการปัญญาภิวัฒน์ (PIM)*

</div>

---

## <img src="https://api.iconify.design/material-symbols:list-alt-outline.svg?color=%236366F1" width="20" height="20" align="center" /> สารบัญ (Table of Contents)
- [<img src="https://api.iconify.design/material-symbols:menu-book-outline.svg?color=%230284C7" width="16" height="16" align="center" /> 1. ข้อมูลรายวิชาเบื้องต้น (Course Information)](#-1-ข้อมูลรายวิชาเบื้องต้น-course-information)
- [<img src="https://api.iconify.design/material-symbols:folder-open-outline.svg?color=%23F59E0B" width="16" height="16" align="center" /> 2. โครงสร้าง Repository (Standard Course Layout)](#-2-โครงสร้าง-repository-standard-course-layout)
- [<img src="https://api.iconify.design/material-symbols:school-outline.svg?color=%230284C7" width="16" height="16" align="center" /> 3. เนื้อหาและการบรรยาย (Lectures & Slides)](#-3-เนื้อหาและการบรรยาย-lectures--slides)
- [<img src="https://api.iconify.design/material-symbols:terminal-outline.svg?color=%2310B981" width="16" height="16" align="center" /> 4. แบบฝึกหัดและการทดลองภาคปฏิบัติ (Labs & Assignments)](#-4-แบบฝึกหัดและการทดลองภาคปฏิบัติ-labs--assignments)
- [<img src="https://api.iconify.design/material-symbols:trophy-outline.svg?color=%23F59E0B" width="16" height="16" align="center" /> 5. โครงงานประจำรายวิชา (Course Projects)](#-5-โครงงานประจำรายวิชา-course-projects)
- [<img src="https://api.iconify.design/material-symbols:edit-note-outline.svg?color=%238B5CF6" width="16" height="16" align="center" /> 6. สรุปทบทวนและเตรียมสอบ (Exams Review)](#-6-สรุปทบทวนและเตรียมสอบ-exams-review)
- [<img src="https://api.iconify.design/material-symbols:verified-user-outline.svg?color=%23EF4444" width="16" height="16" align="center" /> 7. จริยธรรมทางวิชาการ (Academic Integrity Notice)](#-7-จริยธรรมทางวิชาการ-academic-integrity-notice)
- [<img src="https://api.iconify.design/material-symbols:person-outline.svg?color=%2306B6D4" width="16" height="16" align="center" /> 8. ผู้จัดทำ (Author)](#-8-ผู้จัดทำ-author)

---

## <img src="https://api.iconify.design/material-symbols:menu-book-outline.svg?color=%230284C7" width="22" height="22" align="center" /> 1. ข้อมูลรายวิชาเบื้องต้น (Course Information)

- **รหัสวิชา:** `1323404`
- **ชื่อวิชาภาษาอังกฤษ:** Natural Language Processing
- **ชื่อวิชาภาษาไทย:** การประมวลผลภาษาธรรมชาติ
- **หน่วยกิต:** 3 หน่วยกิต (บรรยาย-ปฏิบัติ-ศึกษาด้วยตนเอง)
- **กลุ่มเรียน:** 1.2-1
- **ภาคการศึกษา / ปีการศึกษา:** ภาคเรียนที่ 1 / ปีการศึกษา 2569 (2026)
- **ผลการเรียนที่ได้รับ (Grade):** **กำลังศึกษา (In Progress / Enrolled - Term 1/2569)**
- **สภาพแวดล้อมภาษาโปรแกรม:** Python 3.12, PyTorch, Hugging Face Transformers, spaCy, Pythainlp, LangChain

---

## <img src="https://api.iconify.design/material-symbols:folder-open-outline.svg?color=%23F59E0B" width="22" height="22" align="center" /> 2. โครงสร้าง Repository (Standard Course Layout)

```text
Course-1323404-Natural-Language-Processing-2026/
├── 00_Templates/               # Template โน้ตสรุปและคู่มือ Markdown/Obsidian
├── 01_Lectures/                # เอกสารการสอน สไลด์ และเลกเชอร์สรุปเนื้อหา
│   ├── 01_Docs/               # ประมวลรายวิชา และเอกสารอ้างอิง (Ignored in Git)
│   ├── 02_Teaching_Slides/    # สไลด์บรรยายประจำสัปดาห์ (Ignored in Git)
│   ├── Week1/                 # Intro to NLP, Tokenization
│   ├── Week2/                 # Word Segmentation & Normalization
│   ├── Week3/                 # Syntax and Dependency Parsing
│   ├── Week4/                 # Word Embeddings (Word2Vec, GloVe)
│   ├── Week5/                 # N-gram & Recurrent Neural Networks (RNN/LSTM)
│   ├── Week6/                 # Seq2Seq & Attention Mechanism
│   ├── Week7/                 # Transformer Architecture & Self-Attention
│   ├── Week8/                 # Large Language Models (LLMs) & Fine-Tuning
│   ├── Week9/                 # Advanced NLP Applications & RAG
│   └── Week10/                # Multimodal Large Language Models
├── 02_Labs_Assignments/       # ใบงาน แบบฝึกหัด และ Jupyter Notebooks
│   ├── .env.example           # แม่แบบ Environment Variables สำหรับตั้งค่า API Keys
│   └── Week1/                 # Notebook พื้นฐานการประมวลผลข้อความและ spaCy
├── 03_Projects/                # โครงงานและโปรเจกต์ประจำวิชา
│   └── README.md
├── 04_Exams_Review/            # สรุปทบทวนเนื้อหาและแนวข้อสอบกลางภาค/ปลายภาค
├── custom_football_ner/        # Custom spaCy NER Pipeline สำหรับจำแนกข้อมูลฟุตบอล
├── environment.yml             # Conda environment specification (nlp, Python 3.12)
└── README.md                   # สารบัญหลักและภาพรวมรายวิชา
```

> **หมายเหตุ:** โครงสร้างนี้รองรับการเปิดอ่านบน GitHub และเปิดเป็น **Obsidian Vault** โดยสมบูรณ์ (รองรับ Wikilinks, MathJax, Callouts, Mermaid)

---

## <img src="https://api.iconify.design/material-symbols:school-outline.svg?color=%230284C7" width="22" height="22" align="center" /> 3. เนื้อหาและการบรรยาย (Lectures & Slides)

| สัปดาห์ | หัวข้อการเรียนรู้ (Topics) | โน้ตสรุป (MOC & Notes) | สไลด์บรรยาย |
| :---: | :--- | :--- | :---: |
| **Week 01** | **Intro to NLP & Tokenization**<br>• ความท้าทายของภาษาธรรมชาติ (Ambiguity, Context, Morphology)<br>• Pipeline เบื้องต้น: Sentence Splitting, Tokenization, Regex | [Week 1 MOC](01_Lectures/Week1/Week1-MOC.md)<br>• [Intro to NLP](01_Lectures/Week1/Intro-to-NLP.md)<br>• [Tokenization](01_Lectures/Week1/Tokenization.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 02** | **Word Segmentation & Normalization**<br>• การตัดคำภาษาไทยที่ไม่มีช่องว่างระหว่างคำ (MaxMatch, DeepCut)<br>• Text Normalization, Stemming, Lemmatization, Stopwords | [Week 2 MOC](01_Lectures/Week2/Week2-MOC.md)<br>• [Segmentation & Norm](01_Lectures/Week2/Word-Segmentation-and-Normalization.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 03** | **Syntax & Dependency Parsing**<br>• Part-of-Speech (POS) Tagging และ Grammar Formalisms (CFG)<br>• Dependency Parsing, Head-Dependent Relations, Universal Dependencies | [Week 3 MOC](01_Lectures/Week3/Week3-MOC.md)<br>• [Syntax and Parsing](01_Lectures/Week3/Syntax-and-Parsing.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 04** | **Word Representations & Embeddings**<br>• One-Hot Encoding, TF-IDF และมิติแฝงทางภาษาศาสตร์<br>• Word2Vec (Skip-gram & CBOW), GloVe, FastText Subword Information | [Week 4 MOC](01_Lectures/Week4/Week4-MOC.md)<br>• [Word Embeddings](01_Lectures/Week4/Word-Embeddings.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 05** | **Language Modeling & Sequence Models**<br>• N-gram Language Modeling และ Perplexity Metric<br>• Recurrent Neural Networks (RNN), Exploding/Vanishing Gradients, LSTM, GRU | [Week 5 MOC](01_Lectures/Week5/Week5-MOC.md)<br>• [Language Models](01_Lectures/Week5/Language-Models-Ngram.md)<br>• [RNN Architectures](01_Lectures/Week5/RNN.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 06** | **Encoder-Decoder & Attention Mechanisms**<br>• โครงสร้าง Sequence-to-Sequence (Seq2Seq) สำหรับ Machine Translation<br>• กลไก Attention (Bahdanau & Luong) และ Information Bottleneck | [Week 6 MOC](01_Lectures/Week6/Week6-MOC.md)<br>• [Seq2Seq Architecture](01_Lectures/Week6/Encoder-Decoder-Seq2Seq.md)<br>• [Attention Mechanism](01_Lectures/Week6/Attention-Mechanism.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 07** | **The Transformer Architecture**<br>• Scaled Dot-Product Attention & Multi-Head Attention<br>• Positional Encoding, Residual Connections & Layer Normalization | [Week 7 MOC](01_Lectures/Week7/Week7-MOC.md)<br>• [Transformer](01_Lectures/Week7/Transformer.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 08** | **Large Language Models (LLMs) & Fine-Tuning**<br>• Pre-training & Fine-tuning Paradigm (BERT, GPT, T5)<br>• Parameter-Efficient Fine-Tuning (PEFT, LoRA, QLoRA), Prompt Engineering | [Week 8 MOC](01_Lectures/Week8/Week8-MOC.md)<br>• [LLMs Foundations](01_Lectures/Week8/LLMs.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 09** | **Advanced NLP Applications & RAG**<br>• Retrieval-Augmented Generation (RAG) Architecture<br>• Vector Databases (Chroma, FAISS), Semantic Search, AI Agents | [Week 9 MOC](01_Lectures/Week9/Week9-MOC.md)<br>• [Advanced Applications](01_Lectures/Week9/Advanced-Applications.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |
| **Week 10** | **Multimodal Large Language Models**<br>• Cross-attention และ Projection Layers เชื่อมโยงข้อความกับภาพ/เสียง<br>• Visual Question Answering (VQA) และ Multimodal Reasoning | [Week 10 MOC](01_Lectures/Week10/Week10-MOC.md)<br>• [Multimodal LLMs](01_Lectures/Week10/Multimodal-LLMs.md) | [สไลด์](01_Lectures/02_Teaching_Slides/) |

---

## <img src="https://api.iconify.design/material-symbols:terminal-outline.svg?color=%2310B981" width="22" height="22" align="center" /> 4. แบบฝึกหัดและการทดลองภาคปฏิบัติ (Labs & Assignments)

### 🛠️ การติดตั้งสภาพแวดล้อมการทดลอง (Environment Setup)
รายวิชานี้ใช้ **Python 3.12** พร้อมไลบรารี NLP หลัก สามารถติดตั้งได้ด้วย Conda:

```powershell
# สร้าง Environment จาก environment.yml
conda env create -f environment.yml

# เปิดใช้งาน Environment
conda activate nlp

# ติดตั้งแพ็กเกจโมเดลภาษา spaCy (ภาษาอังกฤษ)
python -m spacy download en_core_web_sm
```

### 🔑 การตั้งค่า Environment Variables (`.env`)
รองรับการเชื่อมต่อ API ของ LLMs (Google Gemini, OpenAI, Anthropic, Hugging Face) ผ่านไฟล์ `.env`:
```powershell
cd 02_Labs_Assignments
Copy-Item .env.example .env
```

| สัปดาห์ | หัวข้อแบบฝึกหัด (Lab / Assignment) | รายละเอียดและเนื้อหาการทดลอง | โฟลเดอร์ซอร์สโค้ด |
| :---: | :--- | :--- | :---: |
| **Lab 01** | Text Preprocessing & Named Entity Recognition | การตัดคำภาษาไทยและอังกฤษ, Part-of-Speech Tagging, และการประยุกต์ใช้งาน spaCy | [เปิด Notebook](02_Labs_Assignments/Week1/01Intro.ipynb) |

---

## <img src="https://api.iconify.design/material-symbols:trophy-outline.svg?color=%23F59E0B" width="22" height="22" align="center" /> 5. โครงงานประจำรายวิชา (Course Projects)

> โครงงานและโมเดลประมวลผลภาษาธรรมชาติที่พัฒนาขึ้นในรายวิชานี้ (เก็บอยู่ในโฟลเดอร์ `03_Projects/`)

### ⚽ Custom Football Entity Recognizer (NER Pipeline)
- **บทบาทและหน้าที่:** โมเดล Named Entity Recognition (NER) ที่เทรนขึ้นเฉพาะเจาะจง (Custom Trained spaCy Pipeline) เพื่อตรวจจับและสกัดชื่อผู้เล่น สโมสรฟุตบอล ตำแหน่ง และเหตุการณ์สำคัญจากการแข่งขัน
- **เทคโนโลยีและเครื่องมือ:** `spaCy v3, Python 3.12, Custom Annotated Dataset, Rule-based & Statistical Entity Linker`
- **ซอร์สโค้ดและโมเดล:** [โฟลเดอร์โมเดล custom_football_ner](custom_football_ner/) | [โฟลเดอร์โครงการ](03_Projects/)

---

## <img src="https://api.iconify.design/material-symbols:edit-note-outline.svg?color=%238B5CF6" width="22" height="22" align="center" /> 6. สรุปทบทวนและเตรียมสอบ (Exams Review)

- [x] **สรุปทบทวนการสอบกลางภาค (Midterm Review):** [บันทึกสรุปและแนวคิดสถิติภาษา](04_Exams_Review/)
- [x] **สรุปทบทวนการสอบปลายภาค (Final Review):** [บันทึกสรุปสถาปัตยกรรม Transformer & LLMs](04_Exams_Review/)

---

## <img src="https://api.iconify.design/material-symbols:verified-user-outline.svg?color=%23EF4444" width="22" height="22" align="center" /> 7. จริยธรรมทางวิชาการ (Academic Integrity Notice)

> [!NOTE]  
> คลังนี้จัดทำขึ้นเพื่อเป็น **บันทึกการเรียนรู้ส่วนบุคคล (Personal Learning Archive)** และนำเสนอพัฒนาการทางวิชาการ (Academic Portfolio) เท่านั้น  
> ไม่อนุญาตให้นำโค้ด การบ้าน หรือรายงานไปคัดลอก (Plagiarism) เพื่อส่งงานในรายวิชาโดยไม่ได้รับอนุญาตตามระเบียบของสถาบันฯ

---

## <img src="https://api.iconify.design/material-symbols:person-outline.svg?color=%2306B6D4" width="22" height="22" align="center" /> 8. ผู้จัดทำ (Author)

**Phuriphat Hemakul (PhuriphatTyPeZ3r0)**
- <img src="https://api.iconify.design/material-symbols:school-outline.svg?color=%230284C7" width="16" height="16" align="center" /> นักศึกษา สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)
- <img src="https://api.iconify.design/material-symbols:apartment-rounded.svg?color=%230284C7" width="16" height="16" align="center" /> สถาบันการจัดการปัญญาภิวัฒน์ (PIM)
- <img src="https://api.iconify.design/simple-icons:github.svg?color=%23181717" width="16" height="16" align="center" /> GitHub: [@PhuriphatTyPeZ3r0](https://github.com/PhuriphatTyPeZ3r0)
- <img src="https://api.iconify.design/material-symbols:language.svg?color=%233B82F6" width="16" height="16" align="center" /> Portfolio: [portfolio-phuriphatizamus-projects.vercel.app](https://portfolio-phuriphatizamus-projects.vercel.app)
