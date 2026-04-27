# HCIA-AI V4.0 Course Framework Analysis

## 1. Material Scope

All four required source PDF files were found under `source_pdf/`, and text was extracted to `extracted_text/`.

| File | Content Role | Main Use |
|---|---|---|
| `hcia-ai-v4.0-exam-outline.pdf` | Certification exam scope, question types, and knowledge-point percentages | Align course modules with exam priorities |
| `hcia-ai-v4.0-training-material.pdf` | Main course slides and teaching content | Build the teaching storyline and chapter-level analysis |
| `hcia-ai-v4.0-lab-guide.pdf` | Hands-on experiments and environment references | Support practical teaching; not analyzed in detail in this round |
| `hcia-ai-v4.0-version-instruction.pdf` | V4.0 release notes and changes from V3.5 | Identify updated teaching focus and removed/added modules |

Text extraction note: ordinary text extraction may miss visual details from diagrams, screenshots, architecture figures, and slide layouts. Diagram-heavy pages should be manually reviewed before final PPT production.

## 2. Course Positioning

HCIA-AI V4.0 is an associate-level Huawei AI certification course. According to the Lab Guide introduction, the certification is intended to train and certify engineers who can design, develop, and innovate AI products and solutions by using machine learning and deep learning algorithms.

The course targets learners who need a structured entry into AI concepts, machine learning, deep learning, foundation models, AI development frameworks, AI business processes, and cutting-edge AI applications. The Lab Guide assumes basic Python programming knowledge and basic math skills, including linear algebra and probability theory.

## 3. Overall Knowledge Framework

The Exam Outline defines six exam knowledge areas. The Training Material follows the same high-level structure.

| Module                                        | Content Description                                                                                     | Source Materials                                                    | Teaching Value                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- |
| AI Overview                                   | AI definition, AI history, AI technologies, DeepSeek, AI applications, debates, and future trends       | Training Material Chapter 1; Exam Outline; Version Instruction      | Builds conceptual foundation and motivates the rest of the course |
| Machine Learning Overview                     | Machine learning algorithms, classifications, process, core concepts, and common algorithms             | Training Material Chapter 2; Lab Guide machine learning experiments | Connects AI concepts to classical data-driven modeling            |
| Basics of Deep Learning and Foundation Models | Perceptron, fully-connected neural networks, CNN, RNN, Transformer, and foundation model infrastructure | Training Material Chapter 3; deep learning lab sections             | Core technical module and largest exam area                       |
| AI Development Framework                      | AI framework concepts, PyTorch basics, commonly used modules, and AI application development process    | Training Material Chapter 4; AI development framework labs          | Converts algorithms into implementation workflows                 |
| AI Business Process Overview                  | AI business process, large model business process, large model usage, and Prompt Engineering            | Training Material Chapter 5; model deployment/application labs      | Links technical knowledge with project and application delivery   |
| Cutting-edge AI Applications                  | Voice assistants, smart homes, intelligent vehicles, recommendation, intelligent robots, and AI4Science | Training Material Chapter 6; Exam Outline                           | Helps learners understand industry application patterns           |

## 4. Exam Weight Alignment

| Exam Area | Percentage | Corresponding Course Module |
|---|---:|---|
| AI Overview | 10% | Chapter 1: AI Overview |
| Machine Learning Overview | 20% | Chapter 2: Machine Learning Overview |
| Basics of Deep Learning and Foundation Models | 30% | Chapter 3: Basics of Deep Learning and Foundation Models |
| AI Development Framework | 20% | Chapter 4: AI Development Framework |
| AI Business Process Overview | 15% | Chapter 5: AI Business Process Overview |
| Cutting-edge AI Applications | 5% | Chapter 6: Cutting-edge AI Applications |

The Exam Outline states that the listed content is a general guide and that topics not explicitly mentioned may also appear in the exam. In teaching, the percentages should be treated as prioritization guidance rather than a strict boundary.

## 5. Version 4.0 Update Signals

| Change Area | V4.0 Signal | Teaching Impact |
|---|---|---|
| AI Overview | Optimized AI overview, AI technologies, applications; added foundation model basics | Chapter 1 should be taught as the entry point to foundation-model thinking, not only as AI history |
| Deep Learning and Foundation Models | Reconstructed deep learning overview; added Transformer and foundation model infrastructure | Chapter 3 becomes the most important technical module |
| AI Development Framework | Added PyTorch basics, common modules, and model deployment | Practical sessions should emphasize PyTorch literacy and deployment workflow |
| AI Platform | AI Platform content deleted | Avoid spending time on removed platform-specific material unless needed by local training goals |
| AI Business Process Overview | Newly added AI business process and large model business process | Add case-based teaching around project workflow, value realization, and Prompt Engineering |
| Cutting-edge AI Applications | Optimized scenarios; added voice assistant, smart home, intelligent vehicle, intelligent robot | Use current industry examples to make this lower-weight module concrete |

## 6. Course Content Hierarchy

| Level | Meaning |
|---|---|
| Chapter | One major course module aligned with exam knowledge areas |
| Section | A topic block inside a chapter, often shown in slide contents pages |
| Knowledge Point | A teachable concept, method, architecture, or application pattern |
| Lab | Hands-on experiment that reinforces algorithms, frameworks, or deployment |
| Exam Objective | Knowledge area listed in the Exam Outline |

## 7. Teaching Design Suggestions

Concept-first chapters: `AI Overview`, `Machine Learning Overview`, and `AI Business Process Overview` are suitable for concept explanation, terminology alignment, and case discussion.

Technical-depth chapters: `Basics of Deep Learning and Foundation Models` and `AI Development Framework` need more board work, architecture diagrams, code walkthroughs, and exercises.

Lab-supported chapters: Machine learning, deep learning, PyTorch, image classification, and model deployment should be connected to Lab Guide experiments. This round does not analyze lab steps in detail.

Exam-priority chapters: Deep learning/foundation models, machine learning, and AI development framework together account for 70% of the written exam and should receive the most structured review time.

