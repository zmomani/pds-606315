"""
Draw the Week 6 diagrams as SVG files (original drawings for this course).

Re-run after editing:  python week06-parallelism/figures/make_figures.py
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent

NAVY, INK, MUTED = "#1f3a5f", "#1b1f24", "#7a8291"
BLUE_FILL, GREY_FILL, GREY_LINE = "#dbe7f5", "#f6f8fa", "#9fb0c3"
ORANGE_FILL, ORANGE_LINE = "#fbf1e3", "#c8862b"
GREEN_FILL, GREEN_LINE = "#e6f4ec", "#1e7f4f"
FONT = "Segoe UI, system-ui, -apple-system, Roboto, Arial, sans-serif"
MONO = "Consolas, Menlo, monospace"


def text(x, y, s, size=13, fill=INK, anchor="middle", family=FONT, weight="normal"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-family="{family}" font-weight="{weight}">{s}</text>')


def rect(x, y, w, h, fill, line, rx=4, dash=False, width=1.4):
    d = ' stroke-dasharray="5 3"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{line}" '
            f'stroke-width="{width}"{d}/>')


def arrow(x1, y1, x2, y2, color=NAVY, width=1.6):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" '
            f'marker-end="url(#a)"/>')


def svg_open(W, H, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc><rect width="{W}" height="{H}" fill="#ffffff"/>'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{NAVY}"/></marker></defs>')


def cook(x, y, label, fill=BLUE_FILL, line=NAVY):
    """A simple cook: a hat, a head and a body."""
    return (f'<rect x="{x - 9}" y="{y - 30}" width="18" height="10" rx="3" fill="#ffffff" stroke="{line}" stroke-width="1.2"/>'
            f'<circle cx="{x}" cy="{y - 12}" r="9" fill="{fill}" stroke="{line}" stroke-width="1.3"/>'
            f'<path d="M{x - 15} {y + 22} Q{x} {y - 6} {x + 15} {y + 22} Z" fill="{fill}" stroke="{line}" stroke-width="1.3"/>'
            + text(x, y + 38, label, size=11.5, fill=INK))


def knife(x, y, label="GIL"):
    return (f'<rect x="{x}" y="{y}" width="30" height="7" rx="3" fill="#cfd6df" stroke="{MUTED}" stroke-width="1"/>'
            f'<rect x="{x + 30}" y="{y - 1}" width="16" height="9" rx="2" fill="{ORANGE_LINE}"/>'
            + text(x + 23, y - 6, label, size=10.5, fill=ORANGE_LINE, weight="600"))


def kitchen_figure():
    W, H = 760, 380
    p = [svg_open(W, H, "Threads and processes as cooks and kitchens",
                  "Left: threading is one kitchen with three cooks sharing one pantry and one knife, the GIL, "
                  "so only one cook cuts at a time. Right: multiprocessing is two separate kitchens, each with "
                  "its own cook, pantry and knife; dishes pass between them through a hatch, the Queue.")]
    # ---- left: one kitchen, shared everything
    p.append(text(185, 28, "threading: one kitchen, several cooks", size=14, fill=NAVY, weight="600"))
    p.append(rect(20, 42, 330, 270, GREY_FILL, GREY_LINE, rx=12))
    p.append(rect(40, 60, 290, 46, GREEN_FILL, GREEN_LINE))
    p.append(text(185, 80, "one pantry = shared memory", size=12.5, fill=GREEN_LINE, weight="600"))
    p.append(text(185, 97, "every cook can reach every ingredient", size=11, fill=INK))
    for i, (x, lab) in enumerate(((85, "thread 1"), (185, "thread 2"), (285, "thread 3"))):
        hold = i == 0
        p.append(cook(x, 190, lab, fill=ORANGE_FILL if hold else BLUE_FILL, line=ORANGE_LINE if hold else NAVY))
    p.append(knife(100, 150))
    p.append(text(185, 262, "one knife (the GIL): only the cook holding it", size=11.5, fill=INK))
    p.append(text(185, 279, "can cut, so CPU work takes turns;", size=11.5, fill=INK))
    p.append(text(185, 296, "waiting (an oven, a delivery) can overlap", size=11.5, fill=INK))
    # ---- right: separate kitchens
    p.append(text(570, 28, "multiprocessing: separate kitchens", size=14, fill=NAVY, weight="600"))
    for k, x0 in enumerate((395, 590)):
        p.append(rect(x0, 42, 155, 270, GREY_FILL, GREY_LINE, rx=12))
        p.append(rect(x0 + 15, 60, 125, 46, GREEN_FILL, GREEN_LINE))
        p.append(text(x0 + 77, 80, "own pantry", size=12.5, fill=GREEN_LINE, weight="600"))
        p.append(text(x0 + 77, 97, "(own memory)", size=11, fill=INK))
        p.append(cook(x0 + 77, 190, f"process {k + 1}", fill=ORANGE_FILL, line=ORANGE_LINE))
        p.append(knife(x0 + 54, 150, "own GIL"))
        p.append(text(x0 + 77, 262, "cuts at the same", size=11.5, fill=INK))
        p.append(text(x0 + 77, 279, "time as the other", size=11.5, fill=INK))
    p.append(rect(551, 210, 38, 24, "#ffffff", NAVY, rx=3))
    p.append(f'<defs><marker id="b" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" '
             f'orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="{NAVY}"/></marker></defs>')
    p.append(f'<line x1="556" y1="222" x2="584" y2="222" stroke="{NAVY}" stroke-width="1.6" '
             f'marker-start="url(#b)" marker-end="url(#a)"/>')   # data can travel either way
    p.append(text(570, 330, "the hatch between kitchens: Queue / Pipe", size=12, fill=NAVY, weight="600"))
    p.append(text(570, 347, "(data is copied through it: pickled)", size=11.5, fill=INK))
    p.append(text(W / 2, H - 6, "One chef juggling dishes = concurrency.  Several chefs cooking at once = parallelism.",
                  size=12.5, fill=NAVY))
    p.append("</svg>")
    (OUT / "kitchen.svg").write_text("".join(p), encoding="utf-8")


def lane(y, label, segments, x0=150, scale=60, h=22):
    """segments: (start, end, kind) in seconds; kind: run | wait | idle."""
    out = [text(x0 - 12, y + h / 2 + 4, label, size=12, fill=INK, anchor="end", family=MONO)]
    for a, b, kind in segments:
        if kind == "run":
            out.append(rect(x0 + a * scale, y, (b - a) * scale, h, ORANGE_FILL, ORANGE_LINE, rx=3))
        elif kind == "wait":
            out.append(rect(x0 + a * scale, y, (b - a) * scale, h, GREY_FILL, GREY_LINE, rx=3, dash=True))
        else:
            out.append(f'<line x1="{x0 + a * scale}" y1="{y + h / 2}" x2="{x0 + b * scale}" y2="{y + h / 2}" '
                       f'stroke="{GREY_LINE}" stroke-width="1"/>')
    return "".join(out)


def gil_figure():
    W, H = 760, 420
    p = [svg_open(W, H, "The GIL on a timeline",
                  "Two CPU-bound threads take turns holding the GIL, so they finish no sooner than one after the "
                  "other. Two I/O-bound threads overlap their waiting, because waiting releases the GIL. Two "
                  "processes each have their own GIL and run at the same time on two cores.")]
    x0, sc = 150, 60
    # 1: CPU-bound threads
    p.append(text(20, 36, "1 · two threads, CPU-bound work: they take turns holding the GIL", size=13.5, fill=NAVY,
                  anchor="start", weight="600"))
    t1 = [(0, 1, "run"), (1, 2, "idle"), (2, 3, "run"), (3, 4, "idle"), (4, 5, "run"), (5, 6, "idle"), (6, 7, "run")]
    t2 = [(0, 1, "idle"), (1, 2, "run"), (2, 3, "idle"), (3, 4, "run"), (4, 5, "idle"), (5, 6, "run"), (6, 7, "idle"),
          (7, 8, "run")]
    p.append(lane(48, "thread 1", t1, x0, sc))
    p.append(lane(76, "thread 2", t2, x0, sc))
    p.append(text(x0, 122, "≈ the same total time as running them one after the other", size=11.5, fill=INK,
                  anchor="start"))
    # 2: I/O-bound threads
    p.append(text(20, 146, "2 · two threads, I/O-bound work: waiting releases the GIL, so the waits overlap",
                  size=13.5, fill=NAVY, anchor="start", weight="600"))
    p.append(lane(158, "thread 1", [(0, 0.5, "run"), (0.5, 3.5, "wait"), (3.5, 4, "run")], x0, sc))
    p.append(lane(186, "thread 2", [(0, 0.5, "idle"), (0.5, 1, "run"), (1, 4, "wait"), (4, 4.5, "run")], x0, sc))
    p.append(text(x0 + 4.5 * sc + 12, 190, "≈ half the time of one after the other", size=11.5, fill=INK, anchor="start"))
    # 3: processes
    p.append(text(20, 256, "3 · two processes: each has its own interpreter and GIL, on its own core",
                  size=13.5, fill=NAVY, anchor="start", weight="600"))
    p.append(lane(268, "process 1", [(0, 4, "run")], x0, sc))
    p.append(lane(296, "process 2", [(0, 4, "run")], x0, sc))
    p.append(text(x0 + 4 * sc + 12, 300, "true parallelism: ≈ half the time on 2 cores", size=11.5, fill=INK,
                  anchor="start"))
    # axis + legend
    p.append(f'<line x1="{x0}" y1="340" x2="{x0 + 9 * sc}" y2="340" stroke="{MUTED}" stroke-width="1"/>')
    p.append(text(x0 + 9 * sc, 356, "time →", size=11.5, fill=MUTED, anchor="end"))
    p.append(rect(150, 378, 16, 14, ORANGE_FILL, ORANGE_LINE, rx=2) + text(172, 390, "running Python code (holds the GIL)",
                                                                           size=11.5, anchor="start"))
    p.append(rect(420, 378, 16, 14, GREY_FILL, GREY_LINE, rx=2, dash=True) + text(442, 390,
                                                                                   "waiting for disk or network (GIL released)",
                                                                                   size=11.5, anchor="start"))
    p.append("</svg>")
    (OUT / "gil.svg").write_text("".join(p), encoding="utf-8")


def pool_figure():
    W, H = 760, 330
    p = [svg_open(W, H, "A process pool",
                  "Six tasks wait in a queue. A pool of two worker processes takes them one at a time; each "
                  "finished task's result is collected, and the results come back in the order of the tasks.")]
    p.append(text(95, 30, "tasks", size=14, fill=NAVY, weight="600"))
    for i in range(6):
        y = 46 + i * 38
        p.append(rect(45, y, 100, 28, BLUE_FILL, NAVY))
        p.append(text(95, y + 19, f"square({i + 1})", size=12, family=MONO))
    p.append(arrow(152, 160, 232, 160))
    p.append(text(192, 150, "submit", size=11.5, fill=NAVY))
    p.append(rect(240, 40, 260, 240, GREY_FILL, GREY_LINE, rx=14))
    p.append(text(370, 64, "Pool(processes=2)", size=13.5, fill=NAVY, family=MONO, weight="600"))
    for k, y in enumerate((95, 180)):
        p.append(rect(270, y, 200, 62, ORANGE_FILL, ORANGE_LINE, rx=8))
        p.append(text(370, y + 25, f"worker process {k + 1}", size=12.5, weight="600"))
        p.append(text(370, y + 45, "takes the next task when free", size=11, fill=INK))
    p.append(text(370, 268, "workers are created once and reused", size=11, fill=MUTED))
    p.append(arrow(508, 160, 588, 160))
    p.append(text(548, 150, "collect", size=11.5, fill=NAVY))
    p.append(text(665, 30, "results", size=14, fill=NAVY, weight="600"))
    for i in range(6):
        y = 46 + i * 38
        p.append(rect(615, y, 100, 28, GREEN_FILL, GREEN_LINE))
        p.append(text(665, y + 19, str((i + 1) ** 2), size=12, family=MONO))
    p.append(text(W / 2, H - 22, "Lifecycle: create Pool  →  submit tasks  →  close()  →  join().   "
                  "map() returns the list of results, in task order;", size=12.5, fill=NAVY))
    p.append(text(W / 2, H - 4, "apply_async() returns one AsyncResult per task (call .get()).   "
                  "With  with Pool(...) as pool:  collect every result inside the block.", size=12, fill=INK))
    p.append("</svg>")
    (OUT / "pool.svg").write_text("".join(p), encoding="utf-8")


def apply_figure():
    W, H = 760, 300
    p = [svg_open(W, H, "apply versus apply_async",
                  "With apply, task 2 starts only after task 1 has finished, so the total is about 5.5 seconds. "
                  "With apply_async, both tasks start at once on two workers, so the total is about 3 seconds.")]
    x0, sc = 210, 70
    p.append(text(20, 34, "pool.apply(): blocking, one task after the other", size=13.5, fill=NAVY, anchor="start",
                  weight="600"))
    p.append(lane(48, "count_total(5)", [(0, 2.5, "run")], x0, sc))
    p.append(lane(78, "count_total(6)", [(0, 2.5, "idle"), (2.5, 5.5, "run")], x0, sc))
    p.append(text(x0 + 5.5 * sc + 8, 96, "≈ 5.5 s", size=12, fill=INK, anchor="start", weight="600"))
    p.append(text(20, 150, "pool.apply_async(): non-blocking, both tasks at once", size=13.5, fill=NAVY,
                  anchor="start", weight="600"))
    p.append(lane(164, "count_total(5)", [(0, 2.5, "run")], x0, sc))
    p.append(lane(194, "count_total(6)", [(0, 3, "run")], x0, sc))
    p.append(text(x0 + 3 * sc + 8, 212, "≈ 3 s", size=12, fill=INK, anchor="start", weight="600"))
    p.append(f'<line x1="{x0}" y1="240" x2="{x0 + 6 * sc}" y2="240" stroke="{MUTED}" stroke-width="1"/>')
    for s in range(7):
        p.append(f'<line x1="{x0 + s * sc}" y1="236" x2="{x0 + s * sc}" y2="244" stroke="{MUTED}" stroke-width="1"/>')
        p.append(text(x0 + s * sc, 258, f"{s} s", size=11, fill=MUTED))
    p.append(text(W / 2, H - 10, "apply() waits for each result before the next call; apply_async() returns an "
                  "AsyncResult at once, and .get() waits later.", size=12, fill=NAVY))
    p.append("</svg>")
    (OUT / "apply.svg").write_text("".join(p), encoding="utf-8")


if __name__ == "__main__":
    kitchen_figure()
    gil_figure()
    pool_figure()
    apply_figure()
    print("wrote", ", ".join(sorted(f.name for f in OUT.glob("*.svg"))))
