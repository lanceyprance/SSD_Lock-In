# Handoff: building the next subject's Lock-In repo

For the next Claude Code session. Read all of this before you touch anything.

You are building **one more cram repo for one more subject**, the same way `lanceyprance/SSD_Lock-In` (EEEN20070 Solid State Devices) and `lanceyprance/mathlockin` (MATH20290) were built. Later all four subjects get joined into one hub site, so **follow the formats below exactly**: the hub reads them.

**Use `lanceyprance/SSD_Lock-In` as the template.** It's the newest and most complete (final-exam version, past papers, mocks). `mathlockin` is the same design with no formula sheet in its exam.

---

## 1. Who the user is and how they work

- A UCD engineering student cramming for finals in **Nov–Dec 2026**, roughly 70% understanding fast, with no lectures attended.
- **Dyslexia-friendly writing everywhere:** one idea per line, short sentences, big equations on their own line, lots of space, few brackets, little italics, no long bullet points. Plain words, no waffle.
- They send material **5 files at a time** and say when they're done. **Don't start building until they say "that's all".** After each batch, reply in a few lines: what you got, what's still missing.
- Ask your questions **once, early, in a numbered list** (see §3). Then work without stopping to ask.
- Keep chat replies short. Findings go in the repo, not in chat.
- Never tick a topic ✅ in `TOPICS.md` unless the user says it's done. Log every confusion question they ask in `questions-asked.md` under its topic (short answer + link to the notes §). Don't edit the notes for it unless they ask.

---

## 2. Set up

1. Clone the template read-only: `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/lanceyprance/SSD_Lock-In ~/ref/SSD_Lock-In` (use the add_repo tool first if the session says so).
2. Your own repo is whatever the session gives you. If it's empty, copy from the template: `site/`, `index.html`, `.nojekyll`, `tools/`, `periodic-table.md` only if relevant, and the **structure** (not the content) of every md file.
3. Tools you'll need: `pdftoppm`, `pdftotext`, `soffice` (pptx → pdf), Pillow, Node. `pip install sympy` if you want it (it isn't installed by default).
4. Put every upload and every rendered page in the **scratchpad**, never in the repo. Only cropped snippets go in `img/`.

---

## 3. Questions to ask the user (once, before building)

1. Subject name and module code. Final exam **date**, **length**, and **layout** (number of questions, marks each, choice or answer-all).
2. Is a **formula sheet** given? If yes, get a copy (past papers usually print it). That decides every "Learn by heart" list.
3. Do they have **past papers with answers**? Which years? (These were the most valuable thing for SSD.)
4. Tutorials: which chapters, and do the answers exist?
5. Is there an existing repo for this subject to redo, or start from scratch?
6. Rough study hours per day, for `PLAN.md`.
7. Where their GitHub Pages will live (it should be `https://lanceyprance.github.io/<Repo>/`).

Don't ask about anything you can find in the files.

---

## 4. Building it, in order

### 4.1 Extract the material

```bash
soffice --headless --convert-to pdf deck.pptx            # slides → PDF (slide count can differ by hidden slides)
pdftoppm -r 100 -png deck.pdf sl/s                        # pages → sl/s-01.png ...
pdftotext -layout file.pdf out.txt                        # text, if the PDF has any
python3 tools/contact_sheet.py sl sheet.png 1 16          # 4×4 grid of slides with numbers, to find diagrams
```

- Past papers and handwritten answers are often **scanned**: pdftotext gives nothing. Render them (`-r 90` to read, `-r 130` to crop) and **read the images**.
- **Transcribe every past paper and its answers into a scratch file as you read them** (question text, marks, figure description, official answer, examiners' comments). You'll need them again for topics, papers and mocks, and re-reading images is slow.
- Map every tutorial and past-paper question to a topic **before** writing anything. The exam drives the topic list. Anything no question touches goes in a "Skip / skim" table.

### 4.2 Cut the snippets

```bash
python3 tools/grid.py grid.png page1.png page2.png         # overlays a 0.05 fraction grid on each page
python3 tools/crops.py jobs.txt                            # each line: src.png dst.png [x0 y0 x1 y1] (fractions)
```

- Read the crop box off the **grid overlay of that page alone**. Guessing fractions from a side-by-side preview of several pages went wrong several times on SSD.
- **Always look at your crops** (paste them into one check sheet and view it) before using them. Fix any that cut off an axis, a label or a caption.
- Names: `img/NN/sPAGE.png` (slide), `img/NN/bPAGE-figN.png` (booklet), `img/NN/ans-chX-qY.png` / `ans-YYYY-qZ.png` (official answers), `img/NN/pYYYY-...png` and `img/papers/...` (past-paper figures).

### 4.3 Write the files (the formats in §5 are fixed)

Order that worked:
1. `site/app.js` port (§6) and `index.html`.
2. `formula-sheet.md` (the exam's own sheet, plus a "Learn by heart (NOT on the sheet)" section at the top).
3. Topics, chapter by chapter: `notes/NN-slug.md` then `questions/NN-slug.md`. **Commit and push after every 2–3 topics.**
4. `TOPICS.md`, `README.md`, `PLAN.md`.
5. `papers/YYYY.md` for every past final.
6. `mock/final-1.md` … `final-3.md`.
7. `questions-asked.md` (one `## Topic N — Title` heading per topic, "(none yet)").
8. Checks (§7), then commit, push, and ask the user before merging to `main`.

---

## 5. File formats (the site parses these, don't improvise)

### `notes/NN-slug.md`

```
# Topic N: Title

Tutorial questions: Ch3 Q1, Q2 · Past finals: 2018 Q1a · 2016 Q3b

Slides: DECK, pages a to b. Booklet §x.y (pages p to q).

---

## The big idea
(3 to 8 short lines)

---

**How to use these notes:**
When you see 🧠, stop.
Answer it on paper first.
Then click to check.

---

## 🎯 In the final
(how this topic is actually asked, with years and marks)

---

## ⭐ Learn by heart from this topic
(only what is NOT on the formula sheet; a memory hook at the end)

---

## 1. Section title

![What it shows](../img/NN/s12.png)

**How to read this diagram:**
- plain-word bullets, one idea each

### 🧠 Check
Question.

<details><summary>Answer</summary>

Answer.

</details>

---

### 📐 Equation K: name (on / NOT on the formula sheet)
$$...$$
| Symbol | Means | Units / value |
**What it means:** … **Use it when:** … (and when not)

## Worked example: Tutorial ChX QY  (or Final YYYY QZ), with the official answer image
## Drawing checklist: ...   (numbered steps for every sketch the exam asks for)
## Method: ...              (table: "You're asked for | Use")

---

Next: [End-of-topic test](../questions/NN-slug.md)
```

- **Equation numbers are global across the repo** (SSD runs 1 to 37). The site links "Equation 18" to the right box.
- Every 📐 box says whether the equation is on the formula sheet.
- Any constant mismatch (tutorial vs booklet vs exam values) or slip in an official answer gets a ⚠️ note with the recomputed value.

### `questions/NN-slug.md`

```
# Topic N: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

(constants line)

---

## Part A: Tutorial and past-final questions

### Q5 (Tutorial Ch2 Q5)
question
<details><summary>Answer</summary>

answer (bold the final numbers)

From: §3, Equation 18

</details>

---

### F2016-3c (Final 2016 Q3c)
...

## Part B: Exam-style questions

### M1: True or false
1. statement
2. statement
<details><summary>Answer</summary>

1. **True.** why (§2)
2. **False.** why (§4)

</details>

### M2: Multiple choice
- A. option
- B. option
<details><summary>Answer</summary>

**B.** why

</details>

### M3: Calculate   ### M4: Sketch   ### M5: Explain   (### M6: Link, optional)
```

Rules the parser depends on:
- Heading IDs must match `^[A-Za-z]*\d+(-\d+[a-z]*)?[a-z]*`: so `Q5`, `Q11a`, `M3`, `F2016-3c`, `F2014-3biii`. **IDs must be unique within a file.** Use `FYYYY-…` for past-final questions.
- The bracket tag must start with `Tutorial` or `Final` for the question to count as a tutorial question and to sort in the drill (`Ch3 Q5`, `Final 2018 Q2c`).
- Every answer ends with a `From:` line naming § / Topic N § / Equation N / drawing checklist / Method. The site turns these into "📖 Read the notes" buttons.
- True/false and multiple-choice answers must use exactly the bold patterns above, or they render as plain open questions.

### `papers/YYYY.md` and `mock/final-N.md`

```
# Final 2018          (or: # Mock Final 1)

(intro: how to use it, constants)

---

## Questions

### Q1. Title — 40 marks
question parts with (marks)

---

### Q2. Title — 30 marks
...

---

## Answers

<details><summary>Q1 answers</summary>

... each part ends with "From: Topic N §M" ...

</details>
```

- The em dash and "N marks" in the `### Q` heading are parsed for the score.
- One `<details><summary>QN answers</summary>` per question.
- Images are relative to the file: `../img/...`.

### `TOPICS.md` (the site builds the whole home page from this)

```
## Chapter 1: Semiconductors (slides SSD_1)

| # | Topic | Slides | Tutorial and past-final Qs | Weight | Notes | Qs done |
|---|---|---|---|---|---|---|
| 1 | [Title](notes/01-slug.md) | 21–53 | [Ch1 Q1–Q3 · 2017 Q1a](questions/01-slug.md) | ●● | ☐ | ☐ |

### Chapter 1 wrap-up
| [Ch1 Wrap-up](mock/wrap-ch1.md) (note) | ☐ |

## Past finals
| [Final 2018](papers/2018.md) (what's in it) | ☐ |

## Mock finals
| [Mock Final 1](mock/final-1.md) | ☐ |
```

- Chapter headings must be `## Chapter N: Title`. The number of these sets the chapter groups.
- Paper and mock rows must start with `|`, and their link text must contain **Mock**, **Final** or **Wrap**. A wrap-up's link text must contain `Ch<N>` to show under that chapter.
- Weight: ●●● must know · ●● should know · ● skim · ✗ skip, based on how often the tutorials **and past finals** hit it.
- Keep a `## 🔁 Relearn` list at the top and a `**Progress:** k / N topics` line at the bottom.

### `PLAN.md`

Day-by-day tables from tomorrow to the exam, one row per day: date, links to topics/papers, hours, ☐. Topics first, then past finals timed, then mocks, then a light last day ("stop by 8 pm"). End with "If you fall behind, cut in this order". **Check weekdays with Python**, don't guess them.

---

## 6. Porting the site

Copy `site/` and `index.html` from SSD_Lock-In, then change only these in `site/app.js` and `index.html`:

| What | Where |
|---|---|
| `REPO_BLOB` | `https://github.com/lanceyprance/<Repo>/blob/main/` |
| **storage prefix** | `'ssd:'` → a **unique** short prefix for this subject (e.g. `'ce:'`). Replace every occurrence. The hub needs them all different. |
| `FALLBACK_TOPICS` | the new topic list `[n, title, slug, chapter]` |
| hero title and subtitle | in `viewHome` (subject name, exam date, layout, formula sheet or not) |
| drill subtitle | in `viewHome` ("All N tutorial and past-final questions …") |
| `tutOrder` | only if the tutorial tags aren't `ChN QN` / `Final YYYY QN` |
| default mock note and timer | `'2 hours, 100 marks'`, and the 120-minute timer, if the exam length differs |
| `REP_SEED` | the user's 🔁 Relearn question keys, or `[]` |
| `index.html` | `<title>`, description, logo letters, brand text; the Periodic table tab only if relevant |
| `site/scramble.js` | SSD's has "new numbers" generators keyed by `slug#QID`. For a new subject, start with the stub `window.SCRAMBLE = {}; window.SCRAMBLE_FMT = x => String(x);` |

Run `node --check site/app.js` after editing.

---

## 7. Checks before you finish

```bash
python3 tools/check_links.py            # every relative link/image exists, <details> balanced
node tools/check_site_parse.js .        # the site's own parsers over TOPICS, questions, papers, mocks: no NO ANSWER, no DUP
python3 tools/check_numbers.py          # rewrite this for the new subject: recompute EVERY number in notes, papers and mocks
grep -rni "midterm\|ssd\|EEEN20070" --include=*.md --include=*.js --include=*.html .   # leftovers from the template
```

- **Starting a local web server (`python3 -m http.server`) was blocked by the permission system in the SSD session.** Use `tools/check_site_parse.js` instead of a browser test, and tell the user you couldn't load the site in a browser.
- Recompute every number in Python before writing it. On SSD this caught a wrong power of ten in a mock answer and a slip in an official answer sheet.

---

## 8. Git and publishing

- Work on the branch the session names. Commit after each batch with a clear message, and push.
- **Ask the user before merging to `main`.** When they say yes: `git fetch origin main`, check `git merge-base --is-ancestor origin/main HEAD`, then `git push origin HEAD:main`.
- GitHub Pages: tell them to set Settings → Pages → branch `main`, folder `/ (root)`. You can't change that from the session.
- If the repo is **public**, warn once that it contains copyrighted slides and past papers.

---

## 9. Lessons from SSD (save yourself the time)

- **Past finals were the best material.** Put every past-final question into its topic's Part A with the official answer and the examiners' comments ("most common mistake: …"). Build mocks from them with new numbers and twists.
- Watch for **constant mismatches** between the tutorial, the booklet and the exam paper. Tell the student to use the paper's values.
- Watch the **units traps** the examiners mention: cm vs m, whole capacitance (pF) vs per area, µm conversions.
- Official answers sometimes contradict the question wording (SSD Ch3 Q4) or contain arithmetic slips (SSD 2016 Q3d). Show the official answer, then flag the issue and give the corrected value.
- When a subject has **no tutorial** for a chapter (SSD's BJT chapter), build its topics from the slides, the booklet and the past-final questions, and say so in `TOPICS.md`.
- Name the student's files neutrally (`questions-asked.md`), not after a person.

---

## 10. The hub (next step after all four subjects exist)

Not part of this job, but don't break it:

- All the Pages sites share one origin, `https://lanceyprance.github.io`, so a hub site can `fetch('/<Repo>/TOPICS.md')` and every subject's question files directly, with nothing copied.
- The hub needs from each repo: the `TOPICS.md` format above, a **unique storage prefix**, and the exam date written in the first lines of `TOPICS.md` (`**Exam:** Wednesday 16 December. …`).
- The user also wants one **combined day plan** across all four exams, giving the most time to the nearest exam.

Existing subjects:
- `lanceyprance/mathlockin`: MATH20290 Multivariable Calculus, exam Sat 5 Dec, prefix `m20290:`.
- `lanceyprance/SSD_Lock-In`: EEEN20070 Solid State Devices, exam Wed 16 Dec, prefix `ssd:`.
- Probably a Computer Engineering subject: the old SSD site linked to a CE site on albinjoby82's account. Ask the user whether they want their own copy.
- The fourth subject is unknown. Ask.
