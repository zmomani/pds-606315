# Programming for Data Science (606315)

**University of Petra · Faculty of Information Technology · Department of Data Science & AI**

Hands-on tutorials and graded exercises for the course, built to run in **VS Code** — in your browser via
GitHub Codespaces, or locally. Nothing to install: one click gives you Python 3.12, Jupyter, NumPy, Pandas
and the course datasets.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/zmomani/pds-606315?quickstart=1)

---

## Start here (students)

1. Click the **Open in GitHub Codespaces** badge above (sign in to GitHub if asked). The first launch takes
   about two minutes while the environment builds; later launches are instant.
2. VS Code opens in your browser. In the **Explorer** on the left, open `week01-02-advanced-python/01_tutorial.ipynb`.
3. Click inside the first code cell and press **Shift + Enter** to run it. If VS Code asks for a kernel,
   choose **Python 3.12** (`/usr/local/bin/python`).
4. Work through the tutorial, then open `02_exercises.ipynb`. Every exercise has a **check cell** beneath it —
   run it; a green ✓ means you got it right, an `AssertionError` tells you what to fix.
5. **Save your work**: Codespaces auto-saves files, but the codespace itself is deleted after a period of
   inactivity. Commit and push regularly (Source Control panel → message → **Commit** → **Sync**).

Prefer to work on your own machine? See [Running locally](#running-locally).

## Course map

| Weeks | Folder | Topics | Status |
|---|---|---|---|
| 1–2 | [`week01-02-advanced-python/`](week01-02-advanced-python) | Comprehensions · generators · `lambda`/`map`/`filter`/`sorted` · decorators · error handling · type hints & dataclasses · context managers | ✅ |
| 3 | [`week03-numpy/`](week03-numpy) | Arrays · dtypes & shape · views vs copies · boolean & fancy indexing · broadcasting · `axis` · `default_rng` · linear algebra | ✅ |
| 4–5 | [`week04-05-pandas/`](week04-05-pandas) | Series/DataFrame · selection · cleaning · missing values · groupby · merge · pivot · time series · plots · full EDA | ✅ |
| 5 | [`project/`](project) | **Project Stage 1** template — proposal & EDA notebook (due end of Week 5) | ✅ |
| 6 | `week06-parallelism/` | Threading, multiprocessing, the GIL | 🔜 |
| 7 | `week07-json/` | JSON parsing, nested data, APIs | 🔜 |
| 8–9 | `week08-09-scraping/` | requests, BeautifulSoup, Scrapy | 🔜 |
| 10–12 | `week10-12-django/` | Django MVT, ORM, forms, REST | 🔜 |
| 13 | `week13-sklearn/` | Scikit-learn pipelines | 🔜 |

Each week folder contains:

```
01_tutorial.ipynb        read, run, and modify — the lesson
02_exercises.ipynb       10 graded exercises with self-check cells
solutions/02_solutions.ipynb   reference answers (try first!)
```

## Datasets

All data is generated deterministically by [`data/make_data.py`](data/make_data.py) so every student has
identical files. The dev container runs it automatically; run `python data/make_data.py` yourself if
`data/generated/` is missing.

| File | Rows | Used for |
|---|---|---|
| `students.csv` | 205 | Deliberately dirty: duplicates, `unknown`/blank GPAs, whitespace, mixed case |
| `enrollments.csv` | 516 | One row per (student, course); joins to `students` |
| `courses.json` | 5 | Course catalogue |
| `sales_2025.csv` | 1 813 | Daily sales by product and city — time series |
| `server.log` | 500 | Text log for generator/parsing exercises |

## Running locally

```bash
git clone https://github.com/zmomani/pds-606315
cd pds-606315
python -m venv .venv
# Windows:   .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python data/make_data.py
code .          # then open any notebook and pick the .venv kernel
```

Requires Python 3.10+ and the VS Code **Python** and **Jupyter** extensions (VS Code will offer to install them).

## For instructors

* **Grading**: the check cells are deterministic. A student notebook can be executed headlessly with
  `jupyter nbconvert --execute --to notebook week03-numpy/02_exercises.ipynb`; a failing check raises and stops execution.
* **CI**: every push runs all tutorial and solution notebooks on GitHub Actions
  ([`.github/workflows/test-notebooks.yml`](.github/workflows/test-notebooks.yml)), so broken examples are caught before students see them.
* **GitHub Classroom**: use this repository as the template; the dev container travels with it. Verified teachers
  receive a Codespaces Education allowance; students get 180 core-hours/month with GitHub Education.
* **Changing the data**: edit `data/make_data.py`, keep the seed, and re-run the CI — the exercise checks were
  written against the current distributions.

## Syllabus alignment

Weeks 1–5 cover topics 1–3 of the 2025/2026 syllabus (Advanced Python Syntax, NumPy, Data Manipulation with
Pandas) and culminate in Project Stage 1. Textbook: VanderPlas, *Python Data Science Handbook*, 2nd ed., O'Reilly 2023.

---

*Course materials © University of Petra. Instructor: Dr. Zaid G. Momani.*
