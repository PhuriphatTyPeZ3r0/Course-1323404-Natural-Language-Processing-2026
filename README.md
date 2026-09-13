# 1323404 Natural Language Processing (การประมวลผลภาษาธรรมชาติ)

คลังสรุปเนื้อหา แบบฝึกหัด และโปรเจกต์รายวิชา **1323404 การประมวลผลภาษาธรรมชาติ (Natural Language Processing)**
สถาบันการจัดการปัญญาภิวัฒน์ (PIM) — ภาคการศึกษา 1/2569, กลุ่มเรียน 1.2-1 (3 หน่วยกิต)

---

## <span class="material-symbols-outlined">push_pin</span> ข้อมูลรายวิชาเบื้องต้น

- **รหัสวิชา:** 1323404
- **หน่วยกิต:** 3
- **กลุ่มเรียน:** 1.2-1

---

## <span class="material-symbols-outlined">folder_copy</span> โครงสร้าง Repository (Project Structure)

```text
03_1323404_Natural-Language-Processing/
├── 00_Templates/          # Template โน้ตและคู่มือ format
├── 01_Lectures/
│   ├── 01_Docs/           # เอกสารและตำราประกอบการสอน (Ignored in Git)
│   ├── 02_Teaching_Slides/ # สไลด์ประกอบการสอนประจำสัปดาห์ (Ignored in Git)
│   └── Week*/              # โน้ตสรุปเนื้อหาบรรยายประจำสัปดาห์ (Markdown / Obsidian)
├── 02_Labs_Assignments/  # ใบงาน แบบฝึกหัด และโค้ดแล็บ
│   ├── .env.example       # แม่แบบ Environment Variables สำหรับตั้งค่า API Keys
│   ├── .env               # ไฟล์เก็บ API Keys ส่วนตัว (Ignored in Git)
│   └── Week*/             # โฟลเดอร์แล็บและแบบฝึกหัดประจำสัปดาห์ (Jupyter Notebooks)
├── 03_Projects/          # โครงงานและโปรเจกต์ประจำวิชา
├── 04_Exams_Review/      # แนวข้อสอบ สรุปทบทวนก่อนสอบกลางภาคและปลายภาค
├── .gitignore            # กำหนดไฟล์ที่ไม่ติดตามใน Git (ป้องกัน Secret รั่วไหล)
├── environment.yml       # Conda environment specification (nlp, Python 3.12)
└── README.md             # เอกสารแนะนำและสารบัญหลัก
```

---

## <span class="material-symbols-outlined">terminal</span> การติดตั้ง Conda Environment (`nlp`)

รายวิชานี้ใช้ Python **3.12** พร้อมไลบรารี NLP หลัก สามารถสร้างและเปิดใช้งาน Environment ได้ด้วย Conda:

```powershell
# สร้าง Environment จาก environment.yml
conda env create -f environment.yml

# เปิดใช้งาน Environment
conda activate nlp

# ดาวน์โหลดโมเดลภาษา spaCy (ภาษาอังกฤษ)
python -m spacy download en_core_web_sm
```

---

## <span class="material-symbols-outlined">key</span> การตั้งค่า Environment Variables (`.env`)

รายวิชานี้มีการใช้งาน API จากโมเดลภาษาขนาดใหญ่ (LLMs) และแพลตฟอร์ม NLP เช่น Google Gemini, OpenAI, Anthropic, และ Hugging Face ซึ่งจัดการ API Key ผ่านไฟล์ `.env` ในโฟลเดอร์ `02_Labs_Assignments/`:

### 1. การสร้างไฟล์ `.env`
คัดลอกแม่แบบจาก `.env.example`:
```powershell
# เข้าไปยังโฟลเดอร์ 02_Labs_Assignments
cd 02_Labs_Assignments
Copy-Item .env.example .env
```
จากนั้นเปิดไฟล์ `.env` แล้วกรอก API Key ส่วนตัว (ไฟล์ `.env` ถูกตั้งค่าใน `.gitignore` ไม่ถูกนำขึ้น Git เพื่อความปลอดภัย)

### 2. การเรียกใช้งานใน Jupyter Notebook / Python
ติดตั้งแพ็กเกจ `python-dotenv`:
```bash
pip install python-dotenv
```
เรียกใช้งานใน Notebook สัปดาห์ใดๆ (เช่น `02_Labs_Assignments/Week1/01Intro.ipynb`):
```python
import os
from dotenv import load_dotenv, find_dotenv

# ค้นหาไฟล์ .env อัตโนมัติ (ไต่ระดับโฟลเดอร์ขึ้นไปค้นหาใน 02_Labs_Assignments)
load_dotenv(find_dotenv())

# ตัวอย่างการดึงค่า API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
hf_token = os.getenv("HF_TOKEN")
```

---

## <span class="material-symbols-outlined">lightbulb</span> วิธีการใช้งาน (How to Use)

- **เปิดอ่านผ่าน GitHub:** สามารถคลิกลิงก์ Markdown เพื่ออ่านเนื้อหาผ่าน GitHub ได้ทันที
- **เปิดผ่าน Obsidian:** สามารถเปิดโฟลเดอร์นี้เป็น Obsidian Vault ได้ทันที รองรับ Wikilinks, MathJax ($...$), Callouts (`> [!info]`), และ Mermaid Diagrams

