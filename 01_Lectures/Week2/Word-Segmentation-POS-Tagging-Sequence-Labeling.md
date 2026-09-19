---
tags: [nlp, week2, word-segmentation, pos-tagging, sequence-labeling, crf, ner]
course: 1323404
week: 2
date: 2026-09-19
---

# การตัดคำ, การกำกับชนิดคำ และ Sequence Labeling (Word Segmentation, POS Tagging & Sequence Labeling)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week2-MOC|MOC สัปดาห์ 2]] | ก่อนหน้า: [[Tokenization|สัปดาห์ที่ 1: Tokenization]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Word Segmentation** — การระบุขอบเขตของคำในกระแสตัวอักษรต่อเนื่อง มีความสำคัญอย่างยิ่งในภาษาที่เขียนติดกันโดยไม่มีช่องว่าง เช่น ภาษาไทยและภาษาจีน
- **Part-of-Speech (POS) Tagging** — การกำกับหน้าที่และหมวดหมู่ทางไวยากรณ์ (เช่น NOUN, VERB, ADJ) ให้กับแต่ละคำตามบริบทในประโยค
- **Hidden Markov Model (HMM)** — โมเดลเชิงกำเนิด (Generative Model) ที่จำลองความน่าจะเป็นร่วม $P(\text{Words}, \text{Tags})$ และถอดรหัสลำดับ Tag ที่ดีที่สุดด้วยอัลกอริทึม Viterbi
- **Conditional Random Fields (CRF)** — โมเดลเชิงจำแนกแบบลูกโซ่เชิงเส้น (Linear-Chain Discriminative Model) ที่คำนวณ $P(\text{Tags} \mid \text{Words})$ โดยตรง ทำให้ใส่ Arbitrary Overlapping Features และ Word Shape ได้อย่างอิสระ
- **Sequence Labeling** — กรอบการทำงานสากลที่แมปอินพุตลำดับความยาว $N$ ไปสู่เอาต์พุตป้ายกำกับความยาว $N$ ที่เท่ากันเสมอ (ครอบคลุมทั้ง POS, NER, Word Segmentation, Chunking)
- **Named Entity Recognition (NER)** — งานค้นหาและระบุขอบเขตของชื่อเฉพาะ (Person, Organization, Location, GPE) ผ่านรูปแบบการติดป้าย BIO / BIOES

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. การตัดคำ (Word Segmentation)

ในภาษาอังกฤษ ขอบเขตของคำถูกระบุไว้อย่างชัดเจนด้วยช่องว่าง (Whitespace) เช่น `"I go to school"` ในขณะที่ภาษาอย่างไทย จีน และญี่ปุ่น เขียนติดกันต่อเนื่องโดยไม่มีช่องว่าง เช่น `"ฉันไปโรงเรียน"` ระบบจึงจำเป็นต้องอนุมานขอบเขตคำขึ้นมาเอง

`ผมชอบเรียนภาษา` $\to$ `ผม | ชอบ | เรียน | ภาษา`

#### ความท้าทายหลักของการตัดคำภาษาไทย
1. **ไม่มีตัวคั่นคำ (No Whitespace Delimiter):** การไม่เว้นวรรคทำให้ขอบเขตคำไม่ตายตัว
2. **ความกำกวมของขอบเขตคำ (Boundary Ambiguity):** ตัวอักษรชุดเดียวกันอาจตัดแบ่งได้หลายรูปแบบตามบริบท เช่น:
   - `"ตากลม"` $\to$ `"ตาก-ลม"` (นั่งตากลม) หรือ `"ตา-กลม"` (เด็กตากลมโต)
   - `"ไปหามเหสี"` $\to$ `"ไป-หา-มเหสี"` หรือ `"ไป-หาม-เหสี"`

#### 3 แนวทางหลักในการตัดคำ
- **Dictionary-Based Matching:** จับคู่กับพจนานุกรมคำศัพท์ (Lexicon) ด้วยเทคนิค **Longest Matching** เช่น Forward Maximum Matching (FMM) และ Backward Maximum Matching (BMM) (รวดเร็ว แต่มีปัญหาคำนอกพจนานุกรม OOV)
- **Rule-Based Heuristics:** ใช้กฎไวยากรณ์และสัทศาสตร์ที่มนุษย์ร่างขึ้นเพื่อช่วยตัดสินใจเมื่อเกิดความกำกวม
- **Statistical & Machine Learning:** ใช้โมเดล Machine Learning (เช่น CRF หรือ Neural Networks เช่น DeepCut) ทำนายความน่าจะเป็นของตำแหน่งตัดคำระดับตัวอักษร

---

### 2. การกำกับชนิดของคำ (Part-of-Speech Tagging: POS)

**POS Tagging** คือการระบุหมวดคำทางไวยากรณ์ให้กับทุกคำในประโยคตามบทบาทหน้าที่ เช่น:

```text
Time     flies    like    an     arrow
NOUN     VERB     ADP     DET    NOUN
```

> [!warning] ปัญหาความกำกวมทางชนิดคำ (POS Ambiguity)
> คำรูปเดียวกันอาจทำหน้าที่ได้หลากหลายชนิดคำขึ้นอยู่กับบริบท เช่น คำว่า `"flies"`:
> - เป็น **VERB** (บิน): *"Time flies like an arrow"*
> - เป็น **NOUN** (แมลงวัน): *"Fruit flies like a banana"*

#### แนวทางที่ 1: Knowledge-Based & Rule-Based POS Tagging
- อาศัยการค้นหาจากพจนานุกรม (Lexicon Lookup) ร่วมกับกฎไวยากรณ์ที่มนุษย์เขียนขึ้น (Hand-crafted Disambiguation Rules) เช่น กำหนดว่าคำที่ตามหลัง Determiner (`"the"`, `"an"`) ต้องเป็น NOUN
- ใช้ร่องรอยทางสัณฐานวิทยา (Morphological Cues) เช่น คำลงท้าย `-ing`, `-ed`, `-ly`
- **Brill Transformation-Based Learning (TBL):** วิธีการแบบไฮบริดที่เริ่มต้นจากการกำหนด Tag พื้นฐานที่พบบ่อยที่สุด (Most Frequent Tag) ให้กับแต่ละคำ จากนั้นระบบจะเรียนรู้กฎการแปลง (Transformation Rules) จากข้อมูลฝึกสอนโดยอัตโนมัติอย่างวนซ้ำ เพื่อแก้ไข Tag ที่ผิดพลาดตามบริบทแวดล้อม

---

#### แนวทางที่ 2: Hidden Markov Model (HMM POS Tagger)
HMM เป็น **Generative Model** ที่มองว่า Tag คือ **Hidden State (สถานะซ่อนเร้น)** ที่มองไม่เห็นโดยตรง และคำที่ปรากฏคือ **Observation (สิ่งที่สังเกตได้)**

```mermaid
flowchart LR
    subgraph HiddenStates ["Hidden States (Tags: t)"]
        t1[t1: DET] -->|Transition P t2\|t1| t2[t2: NOUN]
        t2 -->|Transition P t3\|t2| t3[t3: VERB]
    end

    subgraph Observations ["Observations (Words: w)"]
        w1[w1: The]
        w2[w2: cat]
        w3[w3: sat]
    end

    t1 -->|Emission P w1\|t1| w1
    t2 -->|Emission P w2\|t2| w2
    t3 -->|Emission P w3\|t3| w3
```

1. **Transition Probability $P(t_i \mid t_{i-1})$:** ความน่าจะเป็นที่ Tag $t_i$ จะเกิดต่อจาก Tag $t_{i-1}$
2. **Emission Probability $P(w_i \mid t_i)$:** ความน่าจะเป็นที่ Tag $t_i$ จะปล่อยคำ $w_i$ ออกมา

เป้าหมายคือการหาลำดับ Tag $\hat{T} = (\hat{t}_1, \dots, \hat{t}_n)$ ที่ทำให้ความน่าจะเป็นร่วมสูงสุด:
$$\hat{T} = \arg\max_T \prod_{i=1}^n P(w_i \mid t_i) \cdot P(t_i \mid t_{i-1})$$

**Viterbi Decoding Algorithm:** อัลกอริทึมแบบ Dynamic Programming ที่ใช้คำนวณหาเส้นทาง Tag ที่ดีที่สุด (Best Path) บน Trellis Diagram โดยไม่ต้องค้นหาแบบ Exponential:
- ความซับซ้อนเชิงเวลา: $\mathcal{O}(N \times |T|^2)$ เมื่อ $N$ คือความยาวประโยค และ $|T|$ คือจำนวน Tag
- ลำดับขั้นตอน: **Initialization $\to$ Recursion $\to$ Termination $\to$ Backtrace**

---

#### แนวทางที่ 3: Linear-Chain Conditional Random Fields (CRF)

CRF ถูกเสนอโดย Lafferty, McCallum & Pereira (2001) เพื่อแก้จุดอ่อนของ HMM โดย CRF เป็น **Discriminative Model** ที่คำนวณ $P(T \mid W)$ โดยตรง:

$$P(T \mid W) = \frac{1}{Z(W)} \exp\left(\sum_{i=1}^n \sum_k w_k f_k(t_{i-1}, t_i, W, i)\right)$$

โดยที่:
- $w_k$ คือค่าน้ำหนัก (Weight) ของ Feature แต่ละตัวที่เรียนรู้จากการเทรน
- $Z(W)$ คือค่า Normalization Term เพื่อปรับผลรวมความน่าจะเป็นให้เท่ากับ 1
- $f_k(t_{i-1}, t_i, W, i)$ คือ **Feature Function** ที่ดึงคุณลักษณะรอบข้างได้อย่างอิสระ

#### ตัวอย่าง Feature Functions ใน CRF POS Tagger
สมมติประโยคคือ: `"Janet/NNP will/MD back/VB the/DT bill/NN"` เมื่อพิจารณาที่ตำแหน่งคำว่า $x_i = \text{"back"}$:
- $f_{3743}$: $y_i = \text{VB}$ และ $x_i = \text{"back"}$ $\implies$ **Active (= 1)**
- $f_{156}$: $y_i = \text{VB}$ และ $y_{i-1} = \text{MD}$ $\implies$ **Active (= 1)**
- $f_{99732}$: $y_i = \text{VB}$ และ $x_{i-1} = \text{"will"}$ และ $x_{i+2} = \text{"bill"}$ $\implies$ **Active (= 1)**

#### การจัดการกับคำที่ไม่เคยเห็นมาก่อน (Unknown Words Handling)
CRF โดดเด่นอย่างมากในการทายคำที่ไม่เคยเห็นในคลังคำศัพท์ เพราะสามารถผสาน Feature เหล่านี้ได้พร้อมกัน:
- **Word Shape:** แปลงตัวอักษรเป็นรหัส เช่น พิมพ์เล็ก $\to x$, พิมพ์ใหญ่ $\to X$, ตัวเลข $\to d$
  - เช่น `"I.M.F."` $\to$ `X.X.X.` (เดาได้ทันทีว่าเป็นชื่อย่อองค์กร/คำเฉพาะ)
  - เช่น `"DC10-30"` $\to$ `XXdd-dd` (รูปแบบรหัสสินค้า/เที่ยวบิน)
- **Prefix / Suffix Features:** สกัดส่วนนำหน้าและส่วนต่อท้ายความยาว 2-3 ตัวอักษร เช่น คำลงท้าย `"-ing"`, `"-ly"`, `"-tion"` หรือขึ้นต้นด้วย `"un-"`

---

### 3. ตารางสรุปเปรียบเทียบ: Rule-Based vs HMM vs CRF

| แนวทาง | ประเภทโมเดล | จุดเด่น (Strengths) | ข้อจำกัด (Limitations) |
| :--- | :--- | :--- | :--- |
| **Rule-Based<br>(+ Brill TBL)** | Knowledge-Based / Hybrid | • อธิบายเหตุผลได้ชัดเจน (Interpretable)<br>• ไม่ต้องใช้ชุดข้อมูลขนาดใหญ่มาก | • ต้องใช้ผู้เชี่ยวชาญภาษาเขียนกฎ<br>• ปรับขยายขนาด (Scale) ให้ครอบคลุมทุกบริบทได้ยาก |
| **Hidden Markov Model<br>(HMM)** | **Generative Model**<br>(สร้าง $P(W, T)$) | • คำนวณรวดเร็ว<br>• ถอดรหัสได้ง่ายด้วย Viterbi Dynamic Programming | • สมมติฐานความเป็นอิสระ (Independence Assumption) เข้มงวดเกินจริง<br>• เพิ่ม Feature พิเศษที่ซ้อนทับกันได้ยาก |
| **Conditional Random Field<br>(CRF)** | **Discriminative Model**<br>(สร้าง $P(T \mid W)$ ตรง) | • **ใส่ Feature ได้อิสระและซ้อนทับกันได้** (Overlapping Features)<br>• แม่นยำกว่า HMM มากในโจทย์จริง | • ใช้เวลาฝึกสอน (Training) นานกว่า<br>• ต้องการข้อมูลที่กำกับป้าย (Labeled Data) มากพอ |

---

### 4. กรอบแนวคิดงาน Sequence Labeling (Sequence Labeling General Task)

**นิยาม:** งานที่กำหนดป้ายกำกับ (Label) $y_i$ ให้กับทุกๆ สัญลักษณ์อินพุต $x_i$ ในลำดับ $X = (x_1, \dots, x_n)$ โดยผลลัพธ์ $Y = (y_1, \dots, y_n)$ มีความยาวเท่ากับอินพุตเสมอ:

$$\text{Input: } x_1, x_2, \dots, x_n \implies \text{Labels: } y_1, y_2, \dots, y_n$$

| งานใน NLP (Task) | สิ่งที่แทนในแต่ละ $x_i$ (Input Unit) | ความหมายของ $y_i$ (Label Unit) | เครื่องมือที่ใช้แก้ปัญหา |
| :--- | :--- | :--- | :--- |
| **POS Tagging** | คำ (Word) | หมวดคำทางไวยากรณ์ (`NNP`, `VB`, `ADJ`) | HMM, CRF, BiLSTM, Transformer |
| **Named Entity Recognition (NER)** | คำ / โทเค็น (Token) | ประเภท Entity (`B-PER`, `I-PER`, `O`) | CRF, BiLSTM-CRF, BERT/RoBERTa |
| **Word Segmentation** | ตัวอักษร (Character) | ตำแหน่งขอบเขตคำ (`B` = เริ่มคำ, `I` = ในคำ) | CRF, CNN, BiLSTM (เช่น DeepCut) |
| **Chunking / Shallow Parsing** | คำ (Word) | ส่วนของวลี (`B-NP`, `I-NP`, `B-VP`) | CRF, Structured Perceptron |

---

### 5. การรู้จำเอนทิตีที่มีชื่อ (Named Entity Recognition: NER)

**NER** คืองานค้นหาและจำแนก "กลุ่มคำ" (Span) ที่อ้างถึงชื่อเฉพาะในข้อความออกเป็นหมวดหมู่มาตรฐาน:

| ประเภท Entity | คำอธิบาย | ตัวอย่างสากล | ตัวอย่างภาษาไทย |
| :--- | :--- | :--- | :--- |
| **PER (Person)** | ชื่อบุคคล | *Marie Curie, Steve Jobs* | *สมชาย, ลิซ่า* |
| **ORG (Organization)** | ชื่อองค์กร บริษัท มหาวิทยาลัย | *Google, United Nations* | *ปัญญาภิวัฒน์, ปตท.* |
| **LOC (Location)** | สถานที่ทางภูมิศาสตร์ แม่น้ำ ภูเขา | *Sunshine Canyon, Mount Fuji* | *แม่น้ำเจ้าพระยา, ดอยอินทนนท์* |
| **GPE (Geo-Political)** | ประเทศ รัฐ เมือง เขตการปกครอง | *Bangkok, Palo Alto, Thailand* | *กรุงเทพมหานคร, เชียงใหม่* |

> [!important] ความกำกวมของประเภทเอนทิตี (Type Ambiguity)
> คำเดียวกันอาจเป็น Entity ต่างประเภทกันได้ขึ้นอยู่กับบริบท เช่น คำว่า `"Washington"`:
> - เป็น **PER:** *"George Washington was the first president."*
> - เป็น **ORG:** *"Washington defeated New York in the playoffs."* (ทีมกีฬา)
> - เป็น **GPE / LOC:** *"The conference was held in Washington."* (เมืองหลวง/มลรัฐ)

---

### 6. รูปแบบการติดป้ายกำกับ: เปรียบเทียบ IO vs BIO vs BIOES

เนื่องจากชื่อเฉพาะอาจมีความยาวหลาย Token (เช่น *"Steve Jobs"* หรือ *"United Airlines Holding"*) จึงต้องใช้ Tagging Scheme เพื่อระบุขอบเขตคำ:

- **IO Tagging:** มีแค่ `I` (Inside) และ `O` (Outside) — มีจุดอ่อนคือไม่สามารถแยก Entity ชนิดเดียวกันที่อยู่ติดกันได้
- **BIO Tagging (IOB):** เพิ่ม `B` (Begin) เพื่อระบุจุดเริ่มต้นของ Entity (จำนวน Tag ทั้งหมด = $2n + 1$ เมื่อ $n$ คือจำนวนประเภท Entity)
- **BIOES Tagging (BILOU):** เพิ่ม `E` (End) เพื่อระบุจุดสิ้นสุด และ `S` (Single) สำหรับ Entity ที่มีความยาวเพียง 1 Token โดดๆ

#### ตัวอย่างการเปรียบเทียบ Tagging Schemes จากสไลด์
ประโยค: *"Jane Villanueva of United Airlines Holding discussed the Chicago route"*

| Token | IO Scheme | BIO Scheme | BIOES Scheme | คำอธิบายความหมายเชิงลึก |
| :--- | :---: | :---: | :---: | :--- |
| **Jane** | I-PER | **B-PER** | **B-PER** | จุดเริ่มต้นชื่อบุคคล |
| **Villanueva** | I-PER | **I-PER** | **E-PER** | จุดสิ้นสุดชื่อบุคคล (End) |
| **of** | O | **O** | **O** | ไม่ใช่เอนทิตี |
| **United** | I-ORG | **B-ORG** | **B-ORG** | จุดเริ่มต้นชื่อองค์กร |
| **Airlines** | I-ORG | **I-ORG** | **I-ORG** | ส่วนต่อเนื่องภายในชื่อองค์กร |
| **Holding** | I-ORG | **I-ORG** | **E-ORG** | จุดสิ้นสุดชื่อองค์กร (End) |
| **discussed** | O | **O** | **O** | ไม่ใช่เอนทิตี |
| **the** | O | **O** | **O** | ไม่ใช่เอนทิตี |
| **Chicago** | I-LOC | **B-LOC** | **S-LOC** | สถานที่ซึ่งมีความยาวเพียง 1 คำเดี่ยว (Single) |
| **route** | O | **O** | **O** | ไม่ใช่เอนทิตี |

---

### 7. ตัวอย่างการทำ NER บนประโยคภาษาไทย (Thai NER Worked Example)

ประโยคทดสอบ: `"นายสมชายเรียนที่ซอฟแวร์ปาร์คในกรุงเทพ"`

> [!important] กฎสำคัญ: ต้องตัดคำก่อนทำ NER เสมอ
> เนื่องจากภาษาไทยไม่มีช่องว่าง ระบบจึงต้องผ่านขั้นตอน **Word Segmentation** ก่อน แล้วจึงนำ Token แต่ละตัวมาทำ Sequence Labeling:

```text
นาย    สมชาย    เรียน    ที่    ซอฟแวร์    ปาร์ค    ใน    กรุงเทพ
 O     B-PER     O      O     B-ORG     I-ORG    O     B-LOC
```

**บทวิเคราะห์การติดป้าย:**
1. คำว่า `"นาย"`: เป็นคำนำหน้านาม (Title) ไม่ถือเป็นส่วนหนึ่งของชื่อเฉพาะทางกฎเกณฑ์ จึงติดป้ายเป็น **`O`**
2. คำว่า `"สมชาย"`: เป็นจุดเริ่มต้นของชื่อบุคคล จึงติดป้ายเป็น **`B-PER`**
3. คำว่า `"ซอฟแวร์"` และ `"ปาร์ค"`: ชื่อองค์กรที่ตัดคำออกมาได้ 2 Token โดยคำแรกคือจุดเริ่มต้น (**`B-ORG`**) และคำหลังคือส่วนต่อเนื่อง (**`I-ORG`**)
4. คำว่า `"กรุงเทพ"`: สถานที่เดี่ยว ติดป้ายเป็น **`B-LOC`** (หรือ `S-LOC` ใน BIOES)

---

### 8. การประเมินผลประสิทธิภาพ NER (NER Evaluation Metrics)

ในการวัดประสิทธิภาพของระบบ NER จะ **ไม่วัดที่ความถูกต้องระดับ Token (Token-level Accuracy)** เพราะคำส่วนใหญ่ในประโยคเป็นป้าย `O` ซึ่งทำให้ค่าความแม่นยำสูงเกินจริง แต่จะวัดที่ **ระดับขอบเขตของ Entity ที่สมบูรณ์ (Span-Level / Entity-Level Evaluation)**:

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \quad (\text{ในบรรดา Entity ที่ระบบทำนายมาทั้งหมด ถูกต้องกี่เปอร์เซ็นต์})$$

$$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \quad (\text{ในบรรดา Entity ที่มีอยู่จริงทั้งหมด ระบบตรวจจับได้กี่เปอร์เซ็นต์})$$

$$F_1\text{-score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \quad (\text{ค่าเฉลี่ยฮาร์โมนิกระหว่าง Precision และ Recall})$$

> [!warning] กฎ Strict Span Matching
> หากประโยคมีชื่อจริงว่า *"Jane Villanueva"* แต่ระบบทายออกมาเพียง *"Villanueva"* กรณีนี้จะถือว่าระบบทายผิด (นับเป็น 1 False Positive จากการทายผิดขอบเขต และนับเป็น 1 False Negative จากการตรวจจับตัวจริงไม่ครบถ้วน)

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart TD
    Start((●)) --> InputText([รับข้อความดิบ: นายสมชายเรียนที่ซอฟแวร์ปาร์คในกรุงเทพ<br>Raw Text Input])
    
    subgraph Step1 ["ขั้นตอนที่ 1: Word Segmentation"]
        InputText --> SegDict([ตัดคำด้วย Dictionary & Graph Matcher: PyThaiNLP newmm<br>Token Boundary Inference])
        SegDict --> Tokens([ได้ลำดับคำ: นาย | สมชาย | เรียน | ที่ | ซอฟแวร์ | ปาร์ค | ใน | กรุงเทพ<br>Token Sequence])
    end

    subgraph Step2 ["ขั้นตอนที่ 2: Sequence Feature Extraction"]
        Tokens --> Feat([สกัด Features: คำแวดล้อม, Word Shape, Prefix/Suffix<br>Linear-Chain CRF Feature Extraction])
    end

    subgraph Step3 ["ขั้นตอนที่ 3: Sequence Labeling Inference"]
        Feat --> Viterbi([ถอดรหัสลำดับป้ายกำกับที่ดีที่สุดด้วย Viterbi Decoding<br>Optimal Path Decoding])
        Viterbi --> BioTags([กำหนดป้าย BIO: O, B-PER, O, O, B-ORG, I-ORG, O, B-LOC<br>BIO Tag Output])
    end

    subgraph Step4 ["ขั้นตอนที่ 4: Entity Chunk Extraction"]
        BioTags --> SpanGroup([รวมขอบเขตสแปน: สมชาย=PER, ซอฟแวร์ปาร์ค=ORG, กรุงเทพ=LOC<br>Span Formation & Output])
    end

    SpanGroup --> EndNode(((●)))
```

---

<span class="material-symbols-outlined">arrow_forward</span> กลับไปที่ [[Week2-MOC|MOC สัปดาห์ 2]]
