"""
Generate the datasets used throughout the course.

Run once (the dev container does this automatically):

    python data/make_data.py

Everything is seeded, so every student gets byte-identical files.
Files are written to data/generated/ (ignored by git).
"""
from __future__ import annotations

import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

OUT = Path(__file__).parent / "generated"
OUT.mkdir(exist_ok=True)
random.seed(606315)

FIRST = ["Ahmad", "Sara", "Omar", "Lina", "Khaled", "Noor", "Yousef", "Dana",
         "Hamza", "Rana", "Tariq", "Maya", "Faris", "Layla", "Zain", "Hala",
         "Bilal", "Nadia", "Sami", "Reem"]
LAST = ["Haddad", "Khalil", "Nasser", "Saleh", "Qasem", "Odeh", "Zaid",
        "Mansour", "Jaber", "Barakat", "Awad", "Hamdan"]
MAJORS = ["Data Science", "Computer Science", "Cybersecurity", "AI", "Software Eng"]
COURSES = {"606315": "Programming for DS", "606272": "Data Structures",
           "606271": "OOP", "606410": "Big Data", "606320": "Machine Learning"}
CITIES = ["Amman", "Irbid", "Zarqa", "Aqaba", "Salt", "Madaba"]


def students(n: int = 200) -> list[dict]:
    rows = []
    for i in range(n):
        gpa = round(min(4.0, max(1.5, random.gauss(2.9, 0.5))), 2)
        row = {
            "student_id": 20230000 + i + 1,
            "name": f"{random.choice(FIRST)} {random.choice(LAST)}",
            "major": random.choice(MAJORS),
            "city": random.choice(CITIES),
            "year": random.choice([1, 2, 3, 4]),
            "gpa": gpa,
            "credits": random.randint(12, 132),
            "email": "",
        }
        row["email"] = row["name"].lower().replace(" ", ".") + f"{i:03d}@std.uop.edu.jo"
        # inject realistic dirt for the cleaning lesson
        r = random.random()
        if r < 0.04:
            row["gpa"] = ""              # missing
        elif r < 0.06:
            row["gpa"] = "unknown"       # bad token (pandas will NOT auto-detect this one)
        if random.random() < 0.03:
            row["city"] = row["city"].upper()   # inconsistent case
        if random.random() < 0.03:
            row["major"] = " " + row["major"] + " "  # stray whitespace
        rows.append(row)
    # a few exact duplicates
    rows += random.sample(rows, 5)
    random.shuffle(rows)
    return rows


def enrollments(student_rows: list[dict]) -> list[dict]:
    rows = []
    for s in student_rows:
        for code in random.sample(list(COURSES), k=random.randint(1, 4)):
            rows.append({
                "student_id": s["student_id"],
                "course_code": code,
                "semester": random.choice(["2024-1", "2024-2", "2025-1", "2025-2"]),
                "grade": random.choice([None, *range(45, 101)]),
            })
    return rows


def sales(days: int = 365) -> list[dict]:
    start = date(2025, 1, 1)
    products = {"Laptop": 850, "Phone": 420, "Tablet": 300, "Headphones": 60, "Monitor": 210}
    rows = []
    for d in range(days):
        day = start + timedelta(days=d)
        weekend = day.weekday() >= 5
        for p, base in products.items():
            n = max(0, int(random.gauss(8 if not weekend else 12, 3)))
            if n:
                rows.append({
                    "date": day.isoformat(),
                    "product": p,
                    "city": random.choice(CITIES),
                    "units": n,
                    "unit_price": round(base * random.uniform(0.9, 1.1), 2),
                })
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    st = students()
    write_csv(OUT / "students.csv", st)
    write_csv(OUT / "enrollments.csv", enrollments(st))
    write_csv(OUT / "sales_2025.csv", sales())
    (OUT / "courses.json").write_text(json.dumps(
        [{"code": c, "title": t, "credits": 3} for c, t in COURSES.items()], indent=2))
    # a tiny messy text log for the advanced-python week
    with (OUT / "server.log").open("w") as f:
        levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]
        for i in range(500):
            t = (date(2025, 9, 1) + timedelta(minutes=7 * i)).isoformat()
            f.write(f"{t} {random.choice(levels)} user={random.randint(1, 40)} "
                    f"latency_ms={random.randint(20, 900)}\n")
    print("Wrote:", *sorted(p.name for p in OUT.iterdir()))
