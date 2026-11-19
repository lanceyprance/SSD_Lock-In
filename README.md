# SSD Lock-In: EEEN20070 Solid State Devices (final exam)

Cram notes for the EEEN20070 final on **Wednesday 16 December**, built from the slides (SSD_1 to SSD_4), the booklet, the Ch1 to Ch3 tutorials with their answers, and the **2014 to 2018 finals with the official answers**.

**▶ Practice site: https://lanceyprance.github.io/SSD_Lock-In/** (tutorial and past-final drill, check-your-answer questions, timed past finals and mock finals). It reads the `questions/`, `papers/` and `mock/` md files directly, so editing them updates the site.

Start at **[TOPICS.md](TOPICS.md)** (progress tracker). Day-by-day plan to the exam: **[PLAN.md](PLAN.md)**.

- Formula sheet (given in the exam) + the things you **must** learn by heart: **[formula-sheet.md](formula-sheet.md)**
- Periodic table: **[periodic-table.md](periodic-table.md)**
- Confusing bits I asked about: **[questions-asked.md](questions-asked.md)**
- Past finals: **[2018](papers/2018.md)** · **[2017](papers/2017.md)** · **[2016](papers/2016.md)** · **[2015](papers/2015.md)** · **[2014](papers/2014.md)**
- Mock finals: **[Mock 1](mock/final-1.md)** · **[Mock 2](mock/final-2.md)** · **[Mock 3](mock/final-3.md)**

## The exam

- **3 questions. Answer all.** Q1 = 40% (10 or so short parts across the whole course). Q2 = 30%. Q3 = 30%.
- One of Q2/Q3 is nearly always the **BJT**, the other the **MOSFET** or the pn diode.
- A constants page and a formula page are given ([copy](formula-sheet.md)).
- The 2014 to 2018 papers are the only ones we have. Check the length of your own paper on the timetable; the mocks assume 2 hours.

## Reading style (dyslexia-friendly)

- One idea per line. Short sentences.
- Big equations on their own line.
- Lots of space between sections.
- Few brackets, little italics, no long bullet points.

## How each topic is built

- `notes/NN-topic.md`: a slide (or booklet / answer-sheet) diagram, then **"How to read this diagram"** in plain words, then a **🧠 check** question (answer hidden; try it first).
- **⭐ Learn by heart** list at the top of each topic: only the things that are **not** on the formula sheet.
- **📐 boxes** for every equation: a table of every symbol (meaning, units, value), what it means, **"use it when…"**, and whether it's on the formula sheet.
- **Worked examples** from real tutorial and past-final questions, with the **official answer** diagrams.
- A **drawing checklist** for every sketch the exam asks for, and a **method table** at the end: "You're asked for… / Use…".
- `questions/NN-topic.md`: end-of-topic test.
  - Part A: the tutorial questions **and the past-final questions** on that topic, with the official answers.
  - Part B: exam-style questions in other formats (true/false, multiple choice, calculate, sketch, explain).
- **Rule:** every answer cites the notes section (§) it comes from.

## Answers

- Tutorials Ch1 to Ch3 and the 2014 to 2018 finals: the official answers (with the examiners' comments on common mistakes).
- Exam-style questions and mocks: my own working, every number rechecked in Python (`tools/check_numbers.py`).
- Where an official answer has a slip, the notes say so and show the recomputed value.

## Constants trap

The tutorials, the booklet and the exam don't agree on ε_Si and ε_ox (11.8/3.9 vs 12/4 vs **11/4**). **In the exam, use the values on the paper.** Every past final gives ε_Si = 11 and ε_ox = 4.

## Folders

```
notes/       one file per topic (1–22)
questions/   end-of-topic tests
papers/      the 2014–2018 finals with official answers
mock/        mock finals and the Ch1 wrap-up
img/NN/      snippets: sN.png = slide N, bNN = booklet page, ans-* = official answers, pYYYY-* = past paper figures
site/        the practice site (index.html at the root)
tools/       scripts that cut the snippets and check the numbers
```
