---
tags: [nlp, week<N>, <แท็กหัวข้อ-1>, <แท็กหัวข้อ-2>]
course: 1323404
week: <N>
date: {{date}}
---

# {{title}}

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week<N>-MOC|MOC สัปดาห์ <N>]] | ก่อนหน้า: [[<ชื่อโน้ตก่อนหน้า>]]

## <span class="material-symbols-outlined">key</span> Keyword

- **<คำศัพท์/แนวคิดหลัก (English Term)>** — <คำอธิบายสั้น ๆ บรรทัดเดียว>
- **<คำศัพท์/แนวคิดหลัก (English Term)>** — <คำอธิบายสั้น ๆ บรรทัดเดียว>

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

<อธิบายเนื้อหาหลักด้วยภาษาที่เข้าใจง่าย ใช้ตาราง/สูตร ($...$)/ตัวอย่างประกอบได้ตามความเหมาะสม แบ่งเป็นหัวข้อย่อยด้วย ### ได้ถ้าเนื้อหายาว>

> [!tip] เคล็ดลับ
> <เทคนิคช่วยจำ หรือวิธีเช็คคำตอบ>

## <span class="material-symbols-outlined">schema</span> Diagram

<!--
เกณฑ์มาตรฐาน UML Diagram (เลือกประเภทให้ตรงกับบริบทของเนื้อหา):
1. UML Activity Diagram (กระบวนการไปป์ไลน์ข้อความ/Tokenization/Encoding-Decoding) -> ใช้ flowchart TD/LR พร้อมโหนด Start ((●)), Action ([...]), Decision {...}, End (((●)))
2. UML Sequence Diagram (ลำดับการทำงาน RAG/การคุยโต้ตอบกับ LLM/Agent Tool Calling) -> ใช้ sequenceDiagram
3. UML State Machine Diagram (สถานะการประมวลผลประโยค/Lifecycle ของ Model) -> ใช้ stateDiagram-v2
4. UML Class/Architecture Diagram (โครงสร้างโมเดล/สถาปัตยกรรม Transformer/Embedding) -> ใช้ classDiagram หรือ flowchart

*หากเนื้อหาเป็นคำอธิบาย/นิยาม/ตารางล้วน ๆ ไม่มีขั้นตอนหรือสภาวะ ให้ลบ section นี้ทิ้งทั้งหมด*
-->

```mermaid
flowchart TD
    Start((●)) --> Step1(["<ขั้นตอนที่ 1 : Action Name>"])
    Step1 --> Check{"<เงื่อนไขการตัดสินใจ?>"}
    Check -->|"<เงื่อนไขจริง (True)>"| Step2(["<ขั้นตอนที่ 2 : Action Name>"])
    Check -->|"<เงื่อนไขเท็จ (False)>"| StepAlt(["<ขั้นตอนสำรอง : Alternative Action>"])
    Step2 --> EndNode(((●)))
    StepAlt --> EndNode
```

**ตัวอย่าง:** <ตัวอย่างประกอบสั้น ๆ พร้อมอ้างอิงเลขหน้าสไลด์ถ้ามี>

---
<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[<ชื่อโน้ตถัดไป>]]
