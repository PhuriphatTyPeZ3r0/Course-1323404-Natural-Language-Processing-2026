# -*- coding: utf-8 -*-
"""
HTML to PDF Generator for NLP Midterm Cheatsheet
Generates a beautifully styled, print-optimized A4 PDF via headless Microsoft Edge.
"""

import os
import subprocess
import sys
import tempfile

HTML_CONTENT = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>NLP Midterm Exam Cheatsheet - 1323404</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap');

    @page {
        size: A4 portrait;
        margin: 8mm 11mm 8mm 11mm;
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: 'Sarabun', 'Segoe UI', Tahoma, sans-serif;
        color: #1e293b;
        background: #ffffff;
        line-height: 1.36;
        font-size: 10.5px;
        margin: 0;
        padding: 0;
    }

    .header-banner {
        border-bottom: 2.5px solid #1e40af;
        padding-bottom: 6px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }

    .header-title h1 {
        font-size: 17px;
        font-weight: 700;
        color: #0f172a;
        margin: 0 0 3px 0;
    }

    .header-title .subtitle {
        font-size: 11px;
        color: #475569;
    }

    .header-badge {
        text-align: right;
        font-size: 10.5px;
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 4px 8px;
    }

    .header-badge strong {
        color: #dc2626;
    }

    .section-header {
        background: #1e40af;
        color: white;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .section-header .pts {
        background: rgba(255, 255, 255, 0.25);
        padding: 1px 7px;
        border-radius: 12px;
        font-size: 11px;
    }

    h2 {
        font-size: 13px;
        font-weight: 700;
        color: #1e3a8a;
        margin: 5px 0 2px 0;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 2px;
    }

    h3 {
        font-size: 12px;
        font-weight: 600;
        color: #0369a1;
        margin: 4px 0 2px 0;
    }

    p {
        margin: 3px 0;
    }

    ul, ol {
        margin: 3px 0;
        padding-left: 18px;
    }

    li {
        margin-bottom: 2px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 5px 0 8px 0;
        font-size: 10.5px;
    }

    th, td {
        border: 1px solid #cbd5e1;
        padding: 2.5px 5px;
        text-align: left;
        vertical-align: top;
    }

    th {
        background-color: #f1f5f9;
        color: #0f172a;
        font-weight: 600;
    }

    tr:nth-child(even) {
        background-color: #f8fafc;
    }

    .box-formula {
        background: #eff6ff;
        border: 1.5px solid #3b82f6;
        border-radius: 5px;
        padding: 6px 10px;
        margin: 3px 0;
        font-family: 'Fira Code', 'Consolas', monospace;
        font-size: 10.8px;
        color: #1e3a8a;
    }

    .box-calc {
        background: #f0fdf4;
        border-left: 3.5px solid #16a34a;
        border-radius: 0 4px 4px 0;
        padding: 5px 9px;
        margin: 3px 0;
        font-size: 11px;
    }

    .box-calc strong {
        color: #15803d;
    }

    .box-warning {
        background: #fef2f2;
        border-left: 3.5px solid #ef4444;
        border-radius: 0 4px 4px 0;
        padding: 5px 9px;
        margin: 3px 0;
        font-size: 11px;
    }

    .box-warning strong {
        color: #b91c1c;
    }

    .box-info {
        background: #f8fafc;
        border-left: 3.5px solid #0284c7;
        border-radius: 0 4px 4px 0;
        padding: 5px 9px;
        margin: 3px 0;
        font-size: 11px;
    }

    .code-block {
        font-family: 'Fira Code', 'Consolas', monospace;
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        padding: 5px 8px;
        font-size: 10px;
        white-space: pre-wrap;
        margin: 3px 0;
        line-height: 1.35;
    }

    .page-break {
        page-break-before: always;
    }

    .grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }

    .highlight {
        font-weight: 600;
        color: #b91c1c;
    }

    .math {
        font-family: 'Fira Code', 'Consolas', monospace;
        font-weight: 500;
    }
</style>
</head>
<body>

<!-- ========================================== PAGE 1 ========================================== -->
<div class="header-banner">
    <div class="header-title">
        <h1>📋 MIDTERM EXAM CHEATSHEET — Natural Language Processing (1323404)</h1>
        <div class="subtitle">สถาบันการจัดการปัญญาภิวัฒน์ | ผู้สอน: อ. สธิดา สุขพงษ์ | เวลาสอบ: 17 ต.ค. 2026 (1 ชั่วโมง 30 นาที)</div>
    </div>
    <div class="header-badge">
        จดลายมือเข้าได้ <strong>ไม่จำกัดหน้า</strong><br>
        เครื่องคิดเลข: <strong>เข้าได้ ✅</strong> | โทรศัพท์: <strong>ห้าม ❌</strong>
    </div>
</div>

<table>
    <tr>
        <th style="width:12%">ข้อที่</th>
        <th style="width:50%">หัวข้อข้อสอบ</th>
        <th style="width:18%; text-align:center;">คะแนน</th>
        <th style="width:20%">สัดส่วนคะแนน</th>
    </tr>
    <tr>
        <td><strong>ข้อ 1</strong></td>
        <td>Introduction to Natural Language Processing</td>
        <td style="text-align:center;">1 คะแนน</td>
        <td>5%</td>
    </tr>
    <tr>
        <td><strong>ข้อ 2</strong></td>
        <td>Tokenization & Text Preprocessing</td>
        <td style="text-align:center;">2 คะแนน</td>
        <td>10%</td>
    </tr>
    <tr style="background:#fef3c7;">
        <td><strong>ข้อ 3</strong></td>
        <td><strong>Word Segmentation, POS Tagging & Sequence Labeling</strong></td>
        <td style="text-align:center;"><strong style="color:#b45309;">10 คะแนน (ข้อใหญ่!)</strong></td>
        <td><strong style="color:#b45309;">50% ของข้อสอบ</strong></td>
    </tr>
    <tr>
        <td><strong>ข้อ 4</strong></td>
        <td>Syntax and Parsing (CFG, CYK, Dependency)</td>
        <td style="text-align:center;">4 คะแนน</td>
        <td>20%</td>
    </tr>
    <tr>
        <td><strong>ข้อ 5</strong></td>
        <td>Word Embedding (TF-IDF, Cosine, Word2Vec, GloVe)</td>
        <td style="text-align:center;">3 คะแนน</td>
        <td>15%</td>
    </tr>
    <tr style="background:#e0f2fe; font-weight:bold;">
        <td colspan="2">รวมทั้งหมด 5 ข้อ</td>
        <td style="text-align:center;">20 คะแนน</td>
        <td>100%</td>
    </tr>
</table>

<div class="section-header">
    <span>แผ่นที่ 1: ข้อที่ 1 — Introduction to NLP</span>
    <span class="pts">1 คะแนน</span>
</div>

<h2>1.1 นิยามและจุดตัด 3 ศาสตร์</h2>
<p><strong>NLP (Natural Language Processing)</strong> คือ จุดตัดระหว่าง:</p>
<ul>
    <li><strong>ภาษาศาสตร์ (Linguistics):</strong> กฎเกณฑ์, สัทศาสตร์, โครงสร้างไวยากรณ์ และความหมายของภาษา</li>
    <li><strong>วิทยาการคอมพิวเตอร์ (Computer Science):</strong> โครงสร้างข้อมูล, ประสิทธิภาพเชิงคำนวณ และอัลกอริทึม</li>
    <li><strong>ปัญญาประดิษฐ์ (AI):</strong> การแทนความรู้ (Representation), การเรียนรู้ของเครื่อง (ML/DL) และการอนุมานเหตุผล (Inference)</li>
</ul>
<p><strong>เป้าหมาย:</strong> เพื่อให้คอมพิวเตอร์สามารถ <em>เข้าใจ (Understand)</em>, <em>ตีความ (Interpret)</em>, และ <em>สร้าง (Generate)</em> ภาษามนุษย์ได้อย่างถูกต้องเป็นธรรมชาติ</p>

<h2>1.2 สถาปัตยกรรม 3 เสาหลักของระบบ NLP</h2>
<div class="code-block" style="text-align:center;">[Raw Text Input] ──> [ NLU (ขาเข้า) ] ──> [ KAI (แกนกลาง) ] ──> [ NLG (ขาออก) ] ──> [Natural Output]</div>
<ul>
    <li><strong>NLU (Natural Language Understanding) — ขาเข้า:</strong> ตีความเจตนา (Intent), โครงสร้างไวยากรณ์ (Syntax), และความหมาย (Semantics) จากข้อความดิบ</li>
    <li><strong>KAI (Knowledge Acquisition and Inferencing) — สมอง/แกนกลาง:</strong> จัดเก็บความรู้ (Knowledge Representation / Ontology / Knowledge Graph) และทำการอนุมานด้วยตรรกะและเหตุผล (Reasoning & Inference) เพื่อหาคำตอบ</li>
    <li><strong>NLG (Natural Language Generation) — ขาออก:</strong> สังเคราะห์และสร้างข้อความหรือเสียงพูดที่ถูกต้องตามหลักภาษาและสละสลวยส่งกลับให้มนุษย์</li>
</ul>

<h2>1.3 5 ระดับชั้นโครงสร้างทางภาษา (Levels of Linguistic Structure)</h2>
<ol>
    <li><strong>Morphology (หน่วยคำ/สัณฐานวิทยา):</strong> การประกอบคำ, รากศัพท์, คำนำหน้า/ต่อท้าย (Prefix/Suffix)</li>
    <li><strong>Syntax (ไวยากรณ์/วากยสัมพันธ์):</strong> โครงสร้างประโยค กฎเกณฑ์ความสัมพันธ์ระหว่างคำ</li>
    <li><strong>Semantics (อรรถศาสตร์):</strong> ความหมายตรงตัวตามตัวอักษรของแต่ละประโยคเดี่ยว</li>
    <li><strong>Discourse (สัมพันธสาร):</strong> ความหมายเชื่อมโยงระหว่างประโยค, การอ้างอิงคำสรรพนาม (Coreference Resolution)</li>
    <li><strong>Pragmatics & World Knowledge (วัจนปฏิบัติศาสตร์):</strong> ความหมายตามบริบทโลกจริง, เจตนาแฝง, และวัฒนธรรม</li>
</ol>

<h2>1.4 5 มิติความท้าทายหลักของ NLP และกรณีศึกษาภาษาไทย</h2>
<table>
    <tr>
        <th style="width:20%">มิติความท้าทาย</th>
        <th style="width:40%">คำอธิบายทางทฤษฎี</th>
        <th style="width:40%">ตัวอย่างรูปธรรมในภาษาไทย</th>
    </tr>
    <tr>
        <td><strong>1. Abstractness</strong> (นามธรรม)</td>
        <td>ความหมายแฝง ประชดประชัน ไม่ตรงรูปคำ</td>
        <td>• <em>"สวยกี่โมง"</em> = <strong>ไม่สวย</strong><br>• <em>"ได้อยู่"</em> = <strong>ไม่ได้ / แย่</strong><br>• <em>"ไปให้แม่แกทำ"</em> = ปฏิเสธ/ประชด</td>
    </tr>
    <tr>
        <td><strong>2. Combinability</strong> (ผสมคำไม่จำกัด)</td>
        <td>คำเดี่ยวนำมารวมกันเกิดความหมายใหม่</td>
        <td>• แม่ + น้ำ = <strong>แม่น้ำ</strong> (river)<br>• กับ + ข้าว = <strong>กับข้าว</strong> (side dish ไม่มีข้าวสาร)</td>
    </tr>
    <tr>
        <td><strong>3. Evolutiveness</strong> (ภาษาไม่หยุดนิ่ง)</td>
        <td>ศัพท์สแลง คำย่อ เกิดขึ้นใหม่อย่างรวดเร็ว</td>
        <td>• <em>"ใช่ไหม"</em> $\to$ <em>"ใช่ปะ"</em> $\to$ <em>"ช้ะ"</em><br>• <em>"จะรั่ว"</em> (ขำมากจนทนไม่ไหว), <em>"เลิศ"</em> $\to$ <em>"เริด"</em></td>
    </tr>
    <tr>
        <td><strong>4. Nonstandardness</strong> (ความไร้ระเบียบ)</td>
        <td>ไวยากรณ์ยืดหยุ่น สลับคำขยายได้หลากหลาย</td>
        <td>• <em>"กำลังจะไปกินข้าว"</em>, <em>"กินข้าวอยู่"</em>, <em>"ไปกินข้าวแล้ว"</em></td>
    </tr>
    <tr>
        <td><strong>5. Subjectivity</strong> (ขึ้นกับบริบท/บุคคล)</td>
        <td>ความหมายขึ้นกับวัฒนธรรมและภูมิภาค</td>
        <td>• <em>"แกงส้ม"</em> ภาคกลาง vs ภาคใต้ (แกงเหลือง)</td>
    </tr>
</table>
<div class="box-warning">
    <strong>⚠️ ความท้าทายสูงสุดของภาษาไทย:</strong> ภาษาไทยเขียนติดกัน <strong>ไม่มีช่องว่างคั่นคำ (No whitespace word boundary)</strong> ทำให้งาน <strong>Word Segmentation (การตัดคำ)</strong> เป็นอุปสรรคสำคัญอันดับแรกสุดของทั้งระบบ
</div>

<h2>1.5 Pipeline: Upstream Tasks vs Downstream Tasks</h2>
<ul>
    <li><strong>Upstream Tasks (งานระดับรากฐาน):</strong> สกัดฟีเจอร์ทางภาษาและเตรียมข้อมูล เช่น Tokenization, Word Segmentation, POS Tagging, Syntactic Parsing</li>
    <li><strong>Downstream Tasks (งานประยุกต์ใช้งานจริง):</strong> นำผลลัพธ์ไปใช้งานปลายทาง เช่น Text Classification, Sentiment Analysis, Machine Translation, Text Summarization, Question Answering (QA)</li>
    <li><em>(หมายเหตุ: Named Entity Recognition: NER ทำหน้าที่เป็นสะพานเชื่อมระหว่าง Upstream และ Downstream)</em></li>
</ul>

<!-- ========================================== PAGE 2 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 2: ข้อที่ 2 — Tokenization & Text Preprocessing</span>
    <span class="pts">2 คะแนน</span>
</div>

<h2>2.1 Tokenization คืออะไร และทำไม $1\text{ Token} \neq 1\text{ Word}$</h2>
<p><strong>Tokenization</strong> คือการแบ่งข้อความดิบออกเป็นหน่วยย่อย (Tokens) ก่อนแปลงเป็นตัวเลข (IDs) ป้อนเข้าโมเดล</p>
<p><strong>1 Token $\neq$ 1 Word:</strong> เช่นคำว่า <code>"don't"</code> สามารถตัดได้ 3 รูปแบบ:</p>
<ul>
    <li>1 Token: <code>["don't"]</code></li>
    <li>2 Tokens: <code>["do", "n't"]</code> (มาตรฐาน Penn Treebank แยกคำปฏิเสธ)</li>
    <li>3 Tokens: <code>["don", "'", "t"]</code> (ตัดตามเครื่องหมายวรรคตอน)</li>
</ul>

<h2>2.2 เปรียบเทียบ 3 แนวทางการตัด Token</h2>
<table>
    <tr>
        <th style="width:20%">แนวทาง</th>
        <th style="width:40%">ข้อดี</th>
        <th style="width:40%">ข้อจำกัด</th>
    </tr>
    <tr>
        <td><strong>Word-Based</strong></td>
        <td>เข้าใจง่าย รักษาความหมายระดับคำ</td>
        <td>เกิดปัญหา <strong>Out-of-Vocabulary (OOV)</strong>, คลังคำศัพท์ (Vocab) มีขนาดใหญ่เกินไป</td>
    </tr>
    <tr>
        <td><strong>Character-Based</strong></td>
        <td>ไม่มีปัญหา OOV, Vocab ขนาดเล็กมาก (~100-300 ตัว)</td>
        <td>สูญเสียความหมายของคำ, Sequence ยาวมาก กินหน่วยความจำมหาศาล</td>
    </tr>
    <tr>
        <td><strong>Subword-Based</strong></td>
        <td><strong>สมดุลสมบูรณ์แบบ</strong> จัดการคำใหม่ได้ Vocab ขนาดเหมาะสม (~30K-100K)</td>
        <td>ต้องใช้เวลาในการฝึก Tokenizer บนคลังข้อมูลล่วงหน้า</td>
    </tr>
</table>

<h2>2.3 ตารางเปรียบเทียบ Subword Tokenization Algorithms (ออกสอบบ่อย!)</h2>
<table>
    <tr>
        <th style="width:22%">คุณลักษณะ</th>
        <th style="width:26%">Byte-Pair Encoding (BPE)</th>
        <th style="width:26%">WordPiece</th>
        <th style="width:26%">Unigram Language Model (ULM)</th>
    </tr>
    <tr>
        <td><strong>ทิศทางการรวม</strong></td>
        <td>Bottom-up (จากตัวอักษร รวมขึ้นไป)</td>
        <td>Bottom-up (จากตัวอักษร รวมขึ้นไป)</td>
        <td><strong>Top-down</strong> (เริ่มจากคลังใหญ่ แล้วตัดทิ้ง)</td>
    </tr>
    <tr>
        <td><strong>เกณฑ์ Merge / Prune</strong></td>
        <td>เลือกคู่ที่มี <strong>ความถี่สูงสุด (Most Frequent Pair)</strong> ในคลังข้อมูล</td>
        <td>เลือกคู่ที่ช่วย <strong>เพิ่ม Language Model Likelihood สูงสุด</strong></td>
        <td>ค่อยๆ <strong>ตัดทอน (Prune)</strong> หน่วยย่อยที่ลด Likelihood น้อยสุดออก</td>
    </tr>
    <tr>
        <td><strong>สัญลักษณ์กำกับ Subword</strong></td>
        <td>ใช้ตัวคั่นเฉพาะ เช่น <code>Ġ</code> (GPT)</td>
        <td>ใช้ Prefix <code>##</code> เช่น <code>play</code>, <code>##ing</code></td>
        <td>ใช้เครื่องหมายขีดล่าง <code> </code> (SentencePiece)</td>
    </tr>
    <tr>
        <td><strong>โมเดลที่นำไปใช้งาน</strong></td>
        <td><strong>GPT-2/3/4, LLaMA, RoBERTa</strong></td>
        <td><strong>BERT, DistilBERT, Electra</strong></td>
        <td><strong>SentencePiece, T5, ALBERT</strong></td>
    </tr>
</table>

<h2>2.4 ขั้นตอนการฝึก BPE ด้วยมือทีละ Step (Worked Example)</h2>
<p>สมมติ Corpus ฝึกสอน: <code>"new" (x2), "renew" (x2), "set" (x1), "reset" (x1)</code></p>
<div class="code-block">[Init] แตกเป็นตัวอักษรเดี่ยว:
  n e w (x2)  |  r e n e w (x2)  |  s e t (x1)  |  r e s e t (x1)
  Vocab เริ่มต้น: {e, n, r, s, t, w}

[Step 1] นับความถี่คู่ติดกัน:
  คู่ (n, e) ปรากฏ 4 ครั้ง (ใน new×2 และ renew×2) ซึ่งบ่อยที่สุด --> Merge: (n, e) -> "ne"
  Corpus ใหม่: ne w (x2) | r e ne w (x2) | s e t (x1) | r e s e t (x1)
  Vocab: {e, n, r, s, t, w, "ne"}

[Step 2] นับคู่ความถี่สูงสุดใหม่:
  คู่ (ne, w) ปรากฏ 4 ครั้ง (ใน new×2 และ renew×2) --> Merge: (ne, w) -> "new"
  Corpus ใหม่: new (x2) | r e new (x2) | s e t (x1) | r e s e t (x1)

[Step 3] นับคู่ติดกันใหม่:
  คู่ (r, e) ปรากฏ 3 ครั้ง (ใน renew×2 และ reset×1) --> Merge: (r, e) -> "re"
  Corpus ใหม่: new (x2) | re new (x2) | s e t (x1) | re s e t (x1)

[Step 4] รวม (re, new) -> "renew", รวม (s, e) -> "se", รวม (se, t) -> "set"
  ผลลัพธ์: คำว่า "reset" ประกอบด้วย subwords: ["re", "set"]</div>
<div class="box-info">
    <strong>📌 กฎการนำไป Encode ข้อความใหม่ (Deterministic Rules):</strong> เมื่อนำ BPE ไปตัดคำใหม่ จะต้องไล่รวมคู่ตาม <strong>ลำดับกฎที่เรียนรู้มาจากการเทรนเท่านั้น</strong> (ห้ามนับความถี่ในข้อความทดสอบมาใช้ตัดสิน)
</div>

<h2>2.5 Byte-Level BPE และ Text Normalization Pipeline</h2>
<ul>
    <li><strong>Byte-Level BPE:</strong> ทำงานบนระดับ <strong>256 Base Bytes ของ UTF-8</strong> ทำให้รองรับทุกภาษาในโลก อีโมจิ และสัญลักษณ์คณิตศาสตร์ โดย <strong>ไม่มี Unknown Token (&lt;unk&gt;) อีกต่อไป</strong> (แต่มีข้อจำกัดเรื่อง Language Bias: ภาษาไทย 1 ตัวอักษรใช้ 3 ไบต์ ทำให้กินจำนวน Token มากกว่าภาษาอังกฤษ)</li>
    <li><strong>Text Normalization 5 ขั้นตอน:</strong>
        <ol>
            <li><em>Lowercasing:</em> แปลงเป็นตัวพิมพ์เล็ก (ลดความซ้ำซ้อน)</li>
            <li><em>Punctuation Removal:</em> แยกหรือตัดเครื่องหมายวรรคตอน</li>
            <li><em>Stop Word Removal:</em> ลบคำหยุดที่พบบ่อยแต่ไม่มีความหมายเฉพาะ (เช่น "the", "is", "at")</li>
            <li><em>Stemming vs Lemmatization:</em> Stemming ตัดท้ายคำตามกฎฮิวริสติก ("studies" $\to$ "studi") ส่วน Lemmatization คืนรูปพจนานุกรมโดยดู POS ("studies" $\to$ "study")</li>
            <li><em>Unicode Normalization:</em> ปรับมาตรฐานสระ/วรรณยุกต์ซ้อน (NFC / NFD)</li>
        </ol>
    </li>
</ul>

<!-- ========================================== PAGE 3 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 3: ข้อที่ 3 — Word Segmentation</span>
    <span class="pts">10 คะแนน (ส่วนที่ 1)</span>
</div>

<h2>3.1 ความท้าทายหลักของการตัดคำภาษาไทย</h2>
<p>ภาษาไทยไม่มีช่องว่างคั่นคำ ทำให้เกิด <strong>Boundary Ambiguity (ความกำกวมของขอบเขตคำ)</strong> เช่น <code>"ตากลม"</code> $\to$ <code>"ตาก-ลม"</code> (นั่งตากลม) หรือ <code>"ตา-กลม"</code> (เด็กตากลมโต)</p>

<h2>3.2 Maximum Matching: FMM vs BMM (ออกสอบแน่นอน!)</h2>
<div class="grid-2">
    <div class="box-info">
        <strong>Forward Max Match (FMM):</strong><br>
        • สแกนจาก <strong>ซ้ายไปขวา</strong> (เริ่ม $i=0$)<br>
        • เลือกคำที่ <strong>ยาวที่สุด</strong> ในพจนานุกรม<br>
        • ถ้าไม่พบเลย ให้ตัดอักขระเดี่ยว 1 ตัว
    </div>
    <div class="box-info">
        <strong>Backward Max Match (BMM):</strong><br>
        • สแกนจาก <strong>ขวาไปซ้าย</strong> (เริ่มท้ายสุด)<br>
        • เลือกคำที่ <strong>ยาวที่สุด</strong> ที่สิ้นสุดที่ตำแหน่งนั้น<br>
        • ถ้าไม่พบเลย ให้ตัดอักขระเดี่ยว 1 ตัว
    </div>
</div>

<h3>📝 ตัวอย่าง Trace ข้อสอบ: "อากาศตากลม" (พจนานุกรม: {อากาศ, ตาก, ตา, ลม, กลม})</h3>
<ul>
    <li><strong>FMM (ซ้าย $\to$ ขวา):</strong>
        <ol>
            <li>ตำแหน่งเริ่มต้น: คำยาวสุดที่พบคือ <code>"อากาศ"</code> (ตัด <code>"อากาศ"</code> เหลือ <code>"ตากลม"</code>)</li>
            <li>ตำแหน่งถัดมา: คำยาวสุดในพจนานุกรมคือ <code>"ตาก"</code> (ยาว 3 ตัว ยาวกว่า <code>"ตา"</code>) $\implies$ ตัด <code>"ตาก"</code> เหลือ <code>"ลม"</code></li>
            <li>ตำแหน่งสุดท้าย: พบคำว่า <code>"ลม"</code> $\implies$ ผลลัพธ์: <strong><code>["อากาศ", "ตาก", "ลม"]</code></strong></li>
        </ol>
    </li>
    <li><strong>BMM (ขวา $\to$ ซ้าย):</strong>
        <ol>
            <li>มองจากขวาสุด (<code>"ตากลม"</code>): คำยาวสุดที่สิ้นสุดขวาสุดคือ <code>"กลม"</code> (ยาว 3 ตัว ยาวกว่า <code>"ลม"</code>) $\implies$ ตัด <code>"กลม"</code> เหลือ <code>"อากาศตา"</code></li>
            <li>มองจากขวาที่เหลือ: คำยาวสุดคือ <code>"ตา"</code> $\implies$ ตัด <code>"ตา"</code> เหลือ <code>"อากาศ"</code></li>
            <li>มองคำข้างหน้า: พบ <code>"อากาศ"</code> $\implies$ ผลลัพธ์: <strong><code>["อากาศ", "ตา", "กลม"]</code></strong></li>
        </ol>
    </li>
</ul>
<div class="box-calc">
    <strong>บทสรุปข้อสอบ:</strong> FMM และ BMM ให้ผลลัพธ์ <strong>ไม่ตรงกัน (Disagree)</strong> โดย FMM ได้ <em>ตาก-ลม</em> ส่วน BMM ได้ <em>ตา-กลม</em>
</div>

<h2>3.3 Statistical Word Segmentation (การคำนวณด้วยความน่าจะเป็น)</h2>
<h3>1. Unigram Model (โมเดลคำเดี่ยว)</h3>
<div class="box-formula">
    P(w_1, w_2, ..., w_k) = ∏_{i=1}^k P(w_i) = ∏_{i=1}^k [ Count(w_i) / N ]
</div>
<div class="box-calc">
    <strong>ตัวอย่างคำนวณ (จาก Assignment 2 DIY 2):</strong> ตัดคำว่า <code>"ลมกลม"</code> ระหว่าง 1 คำ vs 2 คำ (กำหนด $N = 100,000$)<br>
    • สถิติ: $\text{Count}(\text{"ลมกลม"}) = 50$, $\text{Count}(\text{"ลม"}) = 5,000$, $\text{Count}(\text{"กลม"}) = 3,000$<br>
    • $P(\text{1 word}) = P(\text{"ลมกลม"}) = \frac{50}{100,000} = \mathbf{0.0005}$<br>
    • $P(\text{2 words}) = P(\text{"ลม"}) \times P(\text{"กลม"}) = \frac{5,000}{100,000} \times \frac{3,000}{100,000} = 0.05 \times 0.03 = \mathbf{0.0015}$<br>
    • <strong>ผลลัพธ์:</strong> การตัด 2 คำ ชนะ! ด้วยอัตราส่วน $\frac{0.0015}{0.0005} = \mathbf{3\text{ เท่า}}$ (สองคำพบบ่อยชนะคำประสมหายาก)
</div>

<h3>2. Bigram Model (บริบท 1 คำก่อนหน้าช่วยแก้ความกำกวมได้อย่างเด็ดขาด)</h3>
<div class="box-formula">
    P(w_1, ..., w_k) = P(w_1) * ∏_{i=2}^k P(w_i | w_{i-1}) = P(w_1) * ∏_{i=2}^k [ Count(w_{i-1}, w_i) / Count(w_{i-1}) ]
</div>
<div class="box-calc">
    <strong>ตัวอย่างคำนวณจริงจาก Lab:</strong> มีคำว่า <code>"นั่ง"</code> นำหน้าประโยค<br>
    • สถิติ: $\text{Count}(\text{นั่ง}) = 2,000, \text{Count}(\text{ตา}) = 4,200, \text{Count}(\text{ตาก}) = 320$<br>
    • $\text{Count}(\text{นั่ง, ตา}) = 4, \text{Count}(\text{ตา, กลม}) = 380, \text{Count}(\text{นั่ง, ตาก}) = 180, \text{Count}(\text{ตาก, ลม}) = 240$<br>
    <strong>แบบ A (ตา-กลม):</strong> $P(\text{ตา} \mid \text{นั่ง}) \times P(\text{กลม} \mid \text{ตา}) = \frac{4}{2,000} \times \frac{380}{4,200} = 0.002 \times 0.090476 = \mathbf{1.8095 \times 10^{-4}}$<br>
    <strong>แบบ B (ตาก-ลม):</strong> $P(\text{ตาก} \mid \text{นั่ง}) \times P(\text{ลม} \mid \text{ตาก}) = \frac{180}{2,000} \times \frac{240}{320} = 0.09 \times 0.75 = \mathbf{0.0675}$<br>
    <strong>เปรียบเทียบ:</strong> แบบ B ชนะแบบ A ด้วยอัตราส่วน $\frac{0.0675}{1.8095 \times 10^{-4}} \approx \mathbf{373\text{ เท่า!}}$
</div>

<!-- ========================================== PAGE 4 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 4: ข้อที่ 3 — POS Tagging & Viterbi Algorithm</span>
    <span class="pts">10 คะแนน (ส่วนที่ 2)</span>
</div>

<h2>4.1 ความกำกวมของ POS (POS Ambiguity)</h2>
<p>คำรูปเดียวกันทำหน้าที่ต่างกันได้ขึ้นอยู่กับบริบท เช่น คำว่า <code>"flies"</code>:</p>
<ul>
    <li><em>"Time flies like an arrow"</em> $\implies$ <code>flies</code> ทำหน้าที่เป็น <strong>VERB</strong> (บิน/ผ่านไปเร็ว)</li>
    <li><em>"Fruit flies like a banana"</em> $\implies$ <code>flies</code> ทำหน้าที่เป็น <strong>NOUN</strong> (แมลงวันผลไม้)</li>
</ul>

<h2>4.2 เปรียบเทียบ 3 แนวทาง POS Tagging</h2>
<table>
    <tr>
        <th style="width:20%">แนวทาง</th>
        <th style="width:22%">ประเภทโมเดล</th>
        <th style="width:29%">จุดเด่น</th>
        <th style="width:29%">ข้อจำกัด</th>
    </tr>
    <tr>
        <td><strong>Rule-Based / Brill TBL</strong></td>
        <td>Knowledge-Based / Hybrid</td>
        <td>อธิบายเหตุผลได้ชัดเจน ไม่ต้องใช้สถิติซับซ้อน</td>
        <td>เขียนกฎครอบคลุมยาก ปรับขนาดได้ลำบาก</td>
    </tr>
    <tr>
        <td><strong>Hidden Markov Model (HMM)</strong></td>
        <td><strong>Generative Model</strong><br>(จำลอง $P(W, T)$)</td>
        <td>คำนวณรวดเร็ว ถอดรหัสด้วย Viterbi Dynamic Programming ได้ในเวลาเชิงเส้น</td>
        <td>สมมติฐาน Independence เข้มงวดเกินจริง, ใส่ Feature ซ้อนทับไม่ได้</td>
    </tr>
    <tr>
        <td><strong>Conditional Random Field (CRF)</strong></td>
        <td><strong>Discriminative Model</strong><br>(จำลอง $P(T \mid W)$ ตรง)</td>
        <td><strong>ใส่ Overlapping Features ได้อิสระ</strong> เช่น Word Shape, Prefix/Suffix, คำแวดล้อม</td>
        <td>ใช้เวลาเทรนนานกว่า ต้องการ Labeled Data มาก</td>
    </tr>
</table>

<h2>4.3 ทฤษฎี HMM และ Viterbi Decoding Algorithm (กดเครื่องคิดเลข!)</h2>
<div class="box-formula">
    HMM Objective:  T̂ = argmax_T ∏_{i=1}^n P(t_i | t_{i-1}) * P(w_i | t_i) = argmax_T ∏ a_{i-1, i} * b_i(w_i)
</div>
<p>กำหนดให้ $v_t(j)$ คือค่าความน่าจะเป็นสูงสุดของเส้นทาง Tag ที่มาสิ้นสุดที่ Tag $j$ ณ ตำแหน่งคำที่ $t$</p>
<ol>
    <li><strong>Initialization ($t = 1$):</strong>
        <div class="box-formula">v_1(j) = a_{&lt;s&gt;, j} * b_j(w_1),  bt_1(j) = 0</div>
    </li>
    <li><strong>Recursion ($t > 1$):</strong>
        <div class="box-formula">v_t(j) = max_{i=1}^N [ v_{t-1}(i) * a_{ij} ] * b_j(w_t),  bt_t(j) = argmax_{i=1}^N [ v_{t-1}(i) * a_{ij} ]</div>
    </li>
    <li><strong>Termination ($t = T$):</strong> $P^* = \max_j v_T(j)$, และ $\hat{t}_T = \arg\max_j v_T(j)$</li>
    <li><strong>Backtracking (ย้อนรอย):</strong> $\hat{t}_{t-1} = bt_t(\hat{t}_t)$</li>
</ol>
<div class="box-warning">
    <strong>💡 ทำไมต้องใช้ Log-space Viterbi:</strong> ในประโยคยาว ค่าความน่าจะเป็นจะเกิด <strong>Arithmetic Underflow</strong> (ตัวเลขเข้าใกล้ 0 จนปัดเป็น 0.0) จึงแปลงเป็นการบวก Log: $v_t(j) = \max_i [ v_{t-1}(i) + \log a_{ij} ] + \log b_j(w_t)$<br>
    <strong>Time Complexity:</strong> $\mathcal{O}(T \times N^2)$ โดย $T$ คือความยาวประโยค และ $N$ คือจำนวน Tag
</div>

<h2>4.4 ตัวอย่างการคำนวณจริงจาก Lab/Assignment: "Janet will back the bill"</h2>
<p>กำหนดข้อมูล Transition Matrix $A$ และ Emission Matrix $B$:</p>
<ul>
    <li>$v_1(\text{NNP}) = a_{<s>, \text{NNP}} \times b_{\text{NNP}}(\text{"Janet"}) = 0.2767 \times 0.000032 = \mathbf{8.8544 \times 10^{-6}}$</li>
    <li>Transition จาก NNP: $a_{\text{NNP}, \text{MD}} = 0.0110$, $a_{\text{NNP}, \text{NN}} = 0.0584$</li>
    <li>Emission ของคำว่า <code>"will"</code>: $b_{\text{MD}}(\text{"will"}) = 0.308431$, $b_{\text{NN}}(\text{"will"}) = 0.000200$</li>
</ul>
<div class="box-calc">
    <strong>ขั้นตอนกดเครื่องคิดเลข:</strong><br>
    1. คำนวณ $v_2(\text{MD})$ (เมื่อ <code>will</code> เป็น Modal Verb):<br>
    $$v_2(\text{MD}) = v_1(\text{NNP}) \times a_{\text{NNP}, \text{MD}} \times b_{\text{MD}}(\text{"will"}) = (8.8544 \times 10^{-6}) \times 0.0110 \times 0.308431 = \mathbf{3.0041 \times 10^{-8}}$$<br>
    2. คำนวณ $v_2(\text{NN})$ (เมื่อ <code>will</code> เป็น Noun คำนาม):<br>
    $$v_2(\text{NN}) = v_1(\text{NNP}) \times a_{\text{NNP}, \text{NN}} \times b_{\text{NN}}(\text{"will"}) = (8.8544 \times 10^{-6}) \times 0.0584 \times 0.000200 = \mathbf{1.0342 \times 10^{-10}}$$<br>
    3. เปรียบเทียบอัตราส่วนความน่าจะเป็น:<br>
    $$\text{Ratio} = \frac{v_2(\text{MD})}{v_2(\text{NN})} = \frac{3.0041 \times 10^{-8}}{1.0342 \times 10^{-10}} \approx \mathbf{290.47\text{ เท่า}}$$
    <em>ความหมาย:</em> คำว่า "will" มีโอกาสเป็น Modal Verb มากกว่า Noun ~290 เท่า เพราะ $b_{\text{MD}}(\text{will})$ สูงมาก
</div>

<!-- ========================================== PAGE 5 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 5: ข้อที่ 3 — Sequence Labelling & NER</span>
    <span class="pts">10 คะแนน (ส่วนที่ 3)</span>
</div>

<h2>5.1 กรอบแนวคิด Sequence Labeling</h2>
<p>กำหนดป้าย $y_i$ ให้กับทุกสัญลักษณ์ $x_i$ ในลำดับ $X = (x_1, \dots, x_n) \implies Y = (y_1, \dots, y_n)$ โดยผลลัพธ์ $Y$ มีความยาวเท่ากับ $X$ เสมอ</p>

<h2>5.2 รูปแบบการติดป้าย: เปรียบเทียบ IO vs BIO vs BIOES</h2>
<ul>
    <li><strong>IO Scheme:</strong> มีแค่ <code>I-TYPE</code> และ <code>O</code> (ข้อจำกัด: แยก 2 เอนทิตีประเภทเดียวกันที่อยู่ติดกันไม่ได้)</li>
    <li><strong>BIO Scheme (IOB):</strong> มี <code>B</code> (Begin), <code>I</code> (Inside), <code>O</code> (Outside) $\implies$ จำนวน Tag $= 2K + 1$ ($K$ คือจำนวน Entity Types)</li>
    <li><strong>BIOES Scheme (BILOU):</strong> มี <code>B</code> (Begin), <code>I</code> (Inside), <code>O</code> (Outside), <code>E</code> (End), <code>S</code> (Single — เอนทิตียาว 1 คำเดี่ยว)</li>
</ul>

<h3>ตารางเปรียบเทียบตัวอย่างภาษาไทย (จาก Assignment 2 DIY 4)</h3>
<p>ประโยค: <code>["บริษัท", "ปูนซิเมนต์", "ไทย", "ตั้งอยู่", "ที่", "กรุงเทพมหานคร"]</code> | เฉลย: ปูนซิเมนต์ไทย (ORG), กรุงเทพมหานคร (LOC)</p>
<table>
    <tr>
        <th>Token</th>
        <th style="text-align:center;">ดัชนี</th>
        <th style="text-align:center;">IO Scheme</th>
        <th style="text-align:center;">BIO Scheme</th>
        <th style="text-align:center;">BIOES Scheme</th>
        <th>คำอธิบาย</th>
    </tr>
    <tr>
        <td>บริษัท</td>
        <td style="text-align:center;">0</td>
        <td style="text-align:center;">O</td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td>คำนำหน้าทั่วไป ไม่ใช่ชื่อเฉพาะ</td>
    </tr>
    <tr>
        <td>ปูนซิเมนต์</td>
        <td style="text-align:center;">1</td>
        <td style="text-align:center;">I-ORG</td>
        <td style="text-align:center;"><strong>B-ORG</strong></td>
        <td style="text-align:center;"><strong>B-ORG</strong></td>
        <td>จุดเริ่มต้นชื่อองค์กร</td>
    </tr>
    <tr>
        <td>ไทย</td>
        <td style="text-align:center;">2</td>
        <td style="text-align:center;">I-ORG</td>
        <td style="text-align:center;"><strong>I-ORG</strong></td>
        <td style="text-align:center;"><strong>E-ORG</strong></td>
        <td>จุดสิ้นสุดชื่อองค์กร (End)</td>
    </tr>
    <tr>
        <td>ตั้งอยู่</td>
        <td style="text-align:center;">3</td>
        <td style="text-align:center;">O</td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td>คำกริยา</td>
    </tr>
    <tr>
        <td>ที่</td>
        <td style="text-align:center;">4</td>
        <td style="text-align:center;">O</td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td style="text-align:center;"><strong>O</strong></td>
        <td>คำบุพบท</td>
    </tr>
    <tr>
        <td>กรุงเทพมหานคร</td>
        <td style="text-align:center;">5</td>
        <td style="text-align:center;">I-LOC</td>
        <td style="text-align:center;"><strong>B-LOC</strong></td>
        <td style="text-align:center;"><strong>S-LOC</strong></td>
        <td>สถานที่ที่มีความยาว 1 คำโดดๆ (Single)</td>
    </tr>
</table>

<h2>5.3 การประเมินผลประสิทธิภาพ NER (Strict Span-Level Evaluation — กดเครื่องคิดเลข!)</h2>
<div class="box-warning">
    <strong>⚠️ กฎเหล็ก:</strong> ห้ามวัดความแม่นยำด้วย Token-Level Accuracy เพราะคำส่วนใหญ่เป็นป้าย <code>O</code> ทำให้ค่าสูงเกินจริง ต้องวัดที่ <strong>Span-Level (ระดับขอบเขตของ Entity ที่สมบูรณ์)</strong>
</div>
<div class="box-formula">
    Precision = TP / (TP + FP) = จำนวน Entity ที่ทายถูกต้อง / จำนวน Entity ที่ระบบทายออกมาทั้งหมด
    Recall    = TP / (TP + FN) = จำนวน Entity ที่ทายถูกต้อง / จำนวน Entity ในเฉลยจริงทั้งหมด
    F1-score  = 2 * P * R / (P + R) = 2*TP / (2*TP + FP + FN)
</div>

<div class="box-calc">
    <strong>ตัวอย่างคำนวณจริงจาก Assignment 2 DIY 5:</strong><br>
    • <strong>Gold (เฉลย 5 ตัว):</strong> <code>(สมชาย, PER)</code>, <code>(เชียงใหม่, LOC)</code>, <code>(ปตท., ORG)</code>, <code>(กรุงเทพ, LOC)</code>, <code>(2026, DATE)</code><br>
    • <strong>Pred (ระบบทาย 4 ตัว):</strong> <code>(สมชาย, PER)</code>, <code>(เชียง, LOC)</code>, <code>(ปตท., ORG)</code>, <code>(กรุงเทพ, ORG)</code><br>
    <strong>ขั้นตอนนับ TP, FP, FN:</strong><br>
    1. <strong>TP (ตรง 100% ทั้งคำและประเภท):</strong> <code>(สมชาย, PER)</code>, <code>(ปตท., ORG)</code> $\implies$ <strong>TP = 2</strong><br>
    2. <strong>FP (ระบบทายมาแต่ผิด):</strong> <code>(เชียง, LOC)</code> [ขอบเขตผิด], <code>(กรุงเทพ, ORG)</code> [ประเภทผิด] $\implies$ <strong>FP = 2</strong><br>
    3. <strong>FN (ในเฉลยที่ระบบทายไม่ถูก):</strong> <code>(เชียงใหม่, LOC)</code> [ทายไม่ครบ], <code>(กรุงเทพ, LOC)</code> [ทายผิดประเภท], <code>(2026, DATE)</code> [หาไม่เจอ] $\implies$ <strong>FN = 3</strong><br>
    <strong>กดเครื่องคิดเลข:</strong><br>
    $$\text{Precision} = \frac{2}{2 + 2} = \frac{2}{4} = \mathbf{0.5000\text{ (50.00\%)}}$$<br>
    $$\text{Recall} = \frac{2}{2 + 3} = \frac{2}{5} = \mathbf{0.4000\text{ (40.00\%)}}$$<br>
    $$F_1\text{-score} = \frac{2 \times 0.5 \times 0.4}{0.5 + 0.4} = \frac{0.40}{0.90} \approx \mathbf{0.4444\text{ (44.44\%)}}$$<br>
    <em>วิเคราะห์:</em> Recall ต่ำกว่า Precision แสดงว่าระบบจับ Entity ตกหล่น และมีปัญหาเรื่องการตัดคำขอบเขตผิด (Boundary Error)
</div>

<!-- ========================================== PAGE 6 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 6: ข้อที่ 4 — Syntax and Parsing</span>
    <span class="pts">4 คะแนน</span>
</div>

<h2>6.1 Constituency Parsing vs Dependency Parsing (ตารางเปรียบเทียบ)</h2>
<table>
    <tr>
        <th style="width:25%">มิติเปรียบเทียบ</th>
        <th style="width:37%">Constituency Parsing</th>
        <th style="width:38%">Dependency Parsing</th>
    </tr>
    <tr>
        <td><strong>โครงสร้าง</strong></td>
        <td>วลีซ้อนวลี (Nested Phrases: S, NP, VP, PP)</td>
        <td>เส้นเชื่อมความสัมพันธ์ระหว่างคำต่อคำโดยตรง</td>
    </tr>
    <tr>
        <td><strong>Root ของต้นไม้</strong></td>
        <td>สัญลักษณ์ประโยค <strong>Sentence ($S$)</strong></td>
        <td><strong>คำกริยาหลักของประโยค (Main Verb / ROOT)</strong></td>
    </tr>
    <tr>
        <td><strong>จำนวน Node</strong></td>
        <td>จำนวนคำ + Non-terminal phrase nodes</td>
        <td><strong>เท่ากับจำนวนคำในประโยคพอดี (1 node ต่อ 1 คำ)</strong></td>
    </tr>
    <tr>
        <td><strong>สิ่งที่เข้ารหัส</strong></td>
        <td>การจัดกลุ่มคำระดับวลี (Phrase Grouping)</td>
        <td>หน้าที่ทางไวยากรณ์ (Subject, Object, Modifier)</td>
    </tr>
    <tr>
        <td><strong>ความสัมพันธ์หลัก</strong></td>
        <td>NP (Noun Phrase), VP (Verb Phrase), PP</td>
        <td><code>nsubj</code> (ประธาน), <code>dobj</code> (กรรมตรง), <code>det</code>, <code>amod</code>, <code>prep</code>, <code>pobj</code></td>
    </tr>
    <tr>
        <td><strong>เครื่องมือยอดนิยม</strong></td>
        <td>Stanford PCFG Parser, NLTK</td>
        <td><strong>spaCy</strong>, Universal Dependencies, Stanza</td>
    </tr>
</table>
<div class="box-info">
    <strong>💡 ทริคตรวจคำตอบในห้องสอบ:</strong> ถ้านับจำนวน Node แล้ว <strong>เท่ากับจำนวนคำในประโยคพอดี</strong> $\implies$ คือ <strong>Dependency Tree</strong> แต่ถ้ามี Node วลี S, NP, VP งอกออกมา $\implies$ คือ <strong>Constituency Tree</strong>
</div>

<h2>6.2 ความกำกวมเชิงโครงสร้าง (PP-Attachment Ambiguity)</h2>
<p>ประโยค: <code>"Students hate tests with errors"</code> หรือ <code>"I saw the man with the telescope"</code></p>
<ul>
    <li><strong>Tree 1 (PP ขยายคำนาม NP):</strong> <code>tests [with errors]</code> $\implies$ นักศึกษาเกลียดข้อสอบที่มีข้อผิดพลาด</li>
    <li><strong>Tree 2 (PP ขยายคำกริยา VP):</strong> <code>[hate tests] [with errors]</code> $\implies$ ทำการเกลียดอย่างผิดพลาด</li>
</ul>

<h2>6.3 Context-Free Grammar (CFG) และ Chomsky Normal Form (CNF)</h2>
<ul>
    <li><strong>CFG:</strong> กฎการเขียนแทน $A \to \beta$ (ขยาย Non-terminal โดยไม่ขึ้นกับบริบทรอบข้าง)</li>
    <li><strong>CNF (บังคับให้ทุกกฎอยู่ใน 2 รูปแบบเท่านั้น):</strong>
        <ol>
            <li>$A \to BC$ (แตกออกเป็น Non-terminal 2 ตัวเสมอ)</li>
            <li>$A \to w$ (แตกออกเป็นคำ Terminal 1 คำเสมอ)</li>
        </ol>
    </li>
</ul>

<h2>6.4 The CYK Algorithm (Bottom-Up Dynamic Programming)</h2>
<p>ใช้ตัดสินว่าประโยคความยาว $n$ สร้างจาก CFG ในรูป CNF ได้หรือไม่ โดยเติมตารางสามเหลี่ยม $n \times n$:</p>
<ol>
    <li><strong>แถวล่างสุด (Span = 1):</strong> ใส่ Non-terminal ที่แตกออกเป็นคำนั้นโดยตรงตามกฎ $A \to w_i$</li>
    <li><strong>แถวถัดไป (Span = 2 ถึง $n$):</strong> สแกนหาจุดตัดแยก $k$ ถ้ารวมคู่ $B$ และ $C$ แล้วมีกฎ $A \to BC$ ให้ใส่ $A$ ในเซลล์ $[i, j]$</li>
    <li><strong>ตรวจสอบ Root:</strong> ถ้าสัญลักษณ์เริ่มต้น <strong>$S$</strong> ปรากฏในช่องบนสุด $[1, n] \implies$ ประโยคถูกต้องตามไวยากรณ์ (Grammatically Valid)</li>
    <li><strong>Time Complexity:</strong> $\mathcal{O}(n^3 \cdot |G|)$</li>
</ol>

<h2>6.5 Probabilistic CFG (PCFG) — คำนวณความน่าจะเป็นของ Tree (กดเครื่องคิดเลข!)</h2>
<div class="box-formula">
    P(Parse Tree T) = ∏_{rule r ∈ T} P(rule_r)
</div>
<div class="box-calc">
    <strong>ตัวอย่างคำนวณ (จาก Assignment 3):</strong> สมมติ Tree 1 ใช้กฎดังต่อไปนี้:<br>
    $S \to NP\ VP\ [1.0]$ | $NP \to N\ [0.25]$ | $VP \to V\ NP\ [0.5]$ | $V \to \text{"hate"}\ [1.0]$ | $NP \to NP\ PP\ [0.25]$ | $NP \to N\ [0.25]$ | $PP \to P\ NP\ [1.0]$ | $P \to \text{"with"}\ [1.0]$ | $NP \to N\ [0.25]$<br>
    $$P(T_1) = 1.0 \times 0.25 \times 0.5 \times 1.0 \times 0.25 \times 0.25 \times 1.0 \times 1.0 \times 0.25 = \mathbf{0.001953}$$
    ต้นไม้ที่มีค่า $P(T)$ สูงสุดจะถูกเลือกเป็น <strong>Most Probable Parse Tree</strong> ผ่าน ViterbiParser
</div>

<!-- ========================================== PAGE 7 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 7: ข้อที่ 5 — Word Embedding</span>
    <span class="pts">3 คะแนน</span>
</div>

<h2>7.1 Symbolic vs Distributional Representation</h2>
<ul>
    <li><strong>Symbolic Representation (One-Hot Vector):</strong> มองคำเป็นสัญลักษณ์เดี่ยวที่เป็นอิสระต่อกัน (Orthogonal), มิติสูงเท่าขนาดพจนานุกรม $|V|$, สมาชิกส่วนใหญ่เป็น 0 (Sparse), <em>ข้อจำกัด:</em> ไม่รู้ความคล้ายคลึงของคำ (<code>cat</code> ห่างจาก <code>kitten</code> เท่ากับ <code>car</code>)</li>
    <li><strong>Distributional Representation:</strong> <em>"You shall know a word by the company it keeps"</em> (J.R. Firth, 1957) ความหมายของคำอนุมานได้จาก <strong>บริบทของคำที่ปรากฏร่วมกันบ่อยๆ</strong></li>
</ul>

<h2>7.2 Sparse Vector vs Dense Vector</h2>
<table>
    <tr>
        <th style="width:25%">มิติเปรียบเทียบ</th>
        <th style="width:37%">Sparse Vector (TF-IDF, Co-occurrence)</th>
        <th style="width:38%">Dense Vector (Word2Vec, GloVe)</th>
    </tr>
    <tr>
        <td><strong>ขนาดมิติ (Dimension)</strong></td>
        <td>มิติสูงมาก เท่ากับขนาด Vocabulary $|V|$ (~10,000–1,000,000)</td>
        <td>มิติต่ำ คงที่ (~100–300 มิติ)</td>
    </tr>
    <tr>
        <td><strong>ค่าในเวกเตอร์</strong></td>
        <td>สมาชิกส่วนใหญ่เป็น <strong>0</strong></td>
        <td>สมาชิกแทบทุกมิติเป็น <strong>ทศนิยมไม่เป็นศูนย์</strong></td>
    </tr>
    <tr>
        <td><strong>ความหมายของมิติ</strong></td>
        <td>แต่ละมิติแทนคำในคลังคำศัพท์โดยตรง</td>
        <td>เข้ารหัสความหมายแฝงเชิงนามธรรม (Latent Semantic Features)</td>
    </tr>
</table>

<h2>7.3 สูตรคำนวณ TF-IDF (กดเครื่องคิดเลข!)</h2>
<div class="box-formula">
    TF(t, d) = Count(t, d)                (ความถี่ของคำ t ในเอกสาร d)
    IDF(t)   = log10( N / DF(t) )         (N = จำนวนเอกสารทั้งหมด, DF = จำนวนเอกสารที่มีคำ t)
    TF-IDF   = TF(t, d) * IDF(t)
</div>
<div class="box-calc">
    <strong>เกร็ดคำนวณข้อสอบ:</strong> ถ้าคำปรากฏในทุกเอกสาร ($DF = N$) $\implies IDF = \log_{10}(1) = \mathbf{0} \implies TF\text{-}IDF = \mathbf{0}$
</div>

<h2>7.4 สูตรคำนวณ Cosine Similarity (กดเครื่องคิดเลข!)</h2>
<div class="box-formula">
    Cosine(u, v) = (u · v) / ( ||u|| * ||v|| ) = (∑ u_i * v_i) / [ √(∑ u_i^2) * √(∑ v_i^2) ]
</div>
<div class="box-calc">
    <strong>ตัวอย่างคำนวณ:</strong> สมมติเวกเตอร์ $u = [1, 2, 3]$ และ $v = [2, 0, 1]$<br>
    1. Dot product: $u \cdot v = (1)(2) + (2)(0) + (3)(1) = 2 + 0 + 3 = \mathbf{5}$<br>
    2. ขนาด $\|u\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14} \approx \mathbf{3.7417}$<br>
    3. ขนาด $\|v\| = \sqrt{2^2 + 0^2 + 1^2} = \sqrt{5} \approx \mathbf{2.2361}$<br>
    4. $\text{Cosine}(u, v) = \frac{5}{3.7417 \times 2.2361} = \frac{5}{8.3666} \approx \mathbf{0.5976}$
</div>

<h2>7.5 Word2Vec: Skip-gram vs CBOW และ GloVe</h2>
<ul>
    <li><strong>CBOW (Continuous Bag-of-Words):</strong> นำคำบริบทรอบข้างมารวมกันเพื่อ <strong>ทำนายคำตรงกลาง</strong> (เทรนเร็วกว่า, ดีกับคำพบบ่อย)</li>
    <li><strong>Skip-gram:</strong> นำคำเป้าหมายตรงกลางมา <strong>ทำนายคำบริบทรอบข้าง</strong> (ดีกับข้อมูลน้อย, เก็บความหมายของ <em>คำหายาก Rare words</em> ได้ดี)</li>
    <li><strong>Negative Sampling (SGNS):</strong> สุ่มคำลบ $k$ คำ (5-10 คำ) แปลงเป็น Binary Logistic Regression หลีกเลี่ยง Softmax เต็ม $|V|$</li>
    <li><strong>Semantic Vector Arithmetic:</strong> $\vec{v}(\text{king}) - \vec{v}(\text{man}) + \vec{v}(\text{woman}) \approx \vec{v}(\text{queen})$</li>
    <li><strong>GloVe (Global Vectors):</strong> เรียนรู้จากสถิติ Global Co-occurrence Matrix ทั้งคลังข้อความผ่าน Matrix Factorization</li>
</ul>

<h2>7.6 Contrastive Learning ยุคใหม่</h2>
<p><strong>หลักการ:</strong> ดึงคู่ที่เหมือนกัน (Positive pairs) ให้เข้าใกล้กัน และผลักคู่ที่ต่างกัน (Negative pairs) ให้ออกห่างกันในเวกเตอร์สเปซ</p>
<ul>
    <li><strong>MUSE:</strong> จัดวาง Word Embeddings หลายภาษาลงใน Shared Multilingual Space เดียวกัน</li>
    <li><strong>SimCSE:</strong> ทำ Sentence Embedding โดยใช้ Dropout Noise สร้าง Positive pair อย่างง่ายแต่ทรงพลัง</li>
    <li><strong>BGE:</strong> โมเดล Embedding สำหรับงานสืบค้นข้อความ (Dense Retrieval / Search)</li>
    <li><strong>CLIP:</strong> เทรน Image และ Text ร่วมกันจนได้ Joint Multimodal Space</li>
</ul>

<!-- ========================================== PAGE 8 ========================================== -->
<div class="page-break"></div>

<div class="section-header">
    <span>แผ่นที่ 8: กล่องสูตรด่วน & 5 กับดักข้อสอบ</span>
    <span class="pts">สำหรับจดสรุป</span>
</div>

<h2>🚨 สรุป 6 สูตรคำนวณที่ต้องใช้เครื่องคิดเลขในห้องสอบ</h2>
<div class="code-block">1. HMM Viterbi Recursion Cell:
   v_t(j) = max_i [ v_{t-1}(i) * a_ij ] * b_j(w_t)
   Log-space: v_t(j) = max_i [ v_{t-1}(i) + log(a_ij) ] + log(b_j(w_t))

2. NER Span-Level Metrics:
   Precision = TP / (TP + FP)
   Recall    = TP / (TP + FN)
   F1-score  = 2*P*R / (P + R) = 2*TP / (2*TP + FP + FN)

3. Bigram Probability:
   P(w_i | w_{i-1}) = Count(w_{i-1}, w_i) / Count(w_{i-1})
   P(Sequence)      = P(w_1) * ∏_{i=2}^k P(w_i | w_{i-1})

4. Probabilistic CFG (PCFG) Tree:
   P(Tree) = ∏_{rule ∈ Tree} P(rule)

5. TF-IDF Formula:
   IDF(t) = log10( N / DF(t) ),    TF-IDF = TF(t, d) * IDF(t)

6. Cosine Similarity:
   cos(u, v) = (u · v) / ( ||u|| * ||v|| ) = (∑ u_i*v_i) / [ √(∑ u_i^2) * √(∑ v_i^2) ]</div>

<h2>🎯 5 กับดักข้อสอบที่นักศึกษามักเสียคะแนน (Exam Pitfalls)</h2>
<div class="box-warning">
    <strong>1. NER ไม่คิดคะแนนที่ป้าย O:</strong> ในการตรวจนับ TP, FP, FN ให้นับเฉพาะกลุ่มคำที่เป็น Entity จริงเท่านั้น ป้าย <code>O</code> ห้ามนำมารวมในตารางคำนวณเด็ดขาด
</div>
<div class="box-warning">
    <strong>2. กฎ Strict Span Matching:</strong> ถ้าเฉลยคือ <code>(เชียงใหม่, LOC)</code> แต่ระบบทาย <code>(เชียง, LOC)</code> กรณีนี้ถือว่า <strong>ผิดทั้งคู่</strong> โดยนับเป็น <strong>1 FP</strong> (ทายขอบเขตผิด) และ <strong>1 FN</strong> (ตรวจจับตัวจริงไม่สำเร็จ)
</div>
<div class="box-warning">
    <strong>3. FMM vs BMM:</strong> FMM สแกนตัดคำยาวสุดจากซ้ายไปขวา ส่วน BMM สแกนตัดคำยาวสุดจากขวาไปซ้าย ถ้าเจอความกำกวม (เช่น <code>อากาศตากลม</code>) ผลลัพธ์มักจะ <strong>ไม่เท่ากัน (Disagree)</strong>
</div>
<div class="box-warning">
    <strong>4. ตรวจชนิดต้นไม้จากจำนวน Node:</strong> Dependency Tree จะต้องมี <strong>จำนวน Node เท่ากับจำนวนคำในประโยคพอดี (1 node ต่อ 1 คำ)</strong> ถ้ามี Node วลี $S, NP, VP$ เพิ่มเข้ามา แสดงว่าเผลอไปวาด Constituency Tree
</div>
<div class="box-warning">
    <strong>5. ค่า IDF เป็น 0:</strong> ถ้าคำปรากฏในทุกเอกสารในคลัง ($DF = N$) ค่า $IDF = \log(1) = 0$ ซึ่งส่งผลให้ $TF\text{-}IDF = 0$ เป็นเรื่องปกติทางสถิติของคำหยุด (Stop words)
</div>

<div style="margin-top:20px; text-align:center; color:#64748b; font-size:11px; border-top:1px solid #cbd5e1; padding-top:8px;">
    เอกสารสรุปเตรียมสอบ MIDTERM วิชา Natural Language Processing (1323404) | ขอให้โชคดีในการทำข้อสอบและคว้าคะแนนเต็ม 20 คะแนน! 💯
</div>

</body>
</html>
"""

def generate_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.abspath(os.path.join(script_dir, ".."))
    out_dir = os.path.join(workspace_root, "04_Exams_Review")
    os.makedirs(out_dir, exist_ok=True)

    html_path = os.path.join(out_dir, "MIDTERM_EXAM_CHEATSHEET.html")
    pdf_path = os.path.join(out_dir, "MIDTERM_EXAM_CHEATSHEET.pdf")

    # 1. Write HTML
    print(f"Writing HTML to: {html_path}")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    # 2. Convert to PDF using Headless Edge
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    browser_exe = None
    for p in edge_paths:
        if os.path.isfile(p):
            browser_exe = p
            break

    if not browser_exe:
        print("Error: No Chromium browser (Edge or Chrome) found.")
        sys.exit(1)

    print(f"Using browser: {browser_exe}")

    temp_dir = tempfile.gettempdir()
    temp_pdf = os.path.join(temp_dir, f"cheatsheet_{os.getpid()}.pdf")
    user_data_dir = os.path.join(temp_dir, f"edge_tmp_{os.getpid()}")

    file_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"

    cmd = [
        browser_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={user_data_dir}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={temp_pdf}",
        file_url
    ]

    print("Running headless PDF conversion...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if os.path.isfile(temp_pdf) and os.path.getsize(temp_pdf) > 0:
        import shutil
        shutil.copyfile(temp_pdf, pdf_path)
        try:
            os.remove(temp_pdf)
            shutil.rmtree(user_data_dir, ignore_errors=True)
        except Exception:
            pass
        print(f"SUCCESS: Generated PDF at {pdf_path} (Size: {os.path.getsize(pdf_path):,} bytes)")
    else:
        print(f"Failed to generate PDF. Edge stdout: {res.stdout}, stderr: {res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    generate_pdf()
