# Week 6 · Multithreading and Parallelism

| File | What it is | Time |
|---|---|---|
| `01_tutorial.ipynb` | Concurrency vs parallelism, the GIL measured, start methods and the `__main__` guard, the `Process` class and `Queue`, process pools (`apply` vs `apply_async`, `map`, `starmap`, `imap`, the context manager, errors in workers), `concurrent.futures` thread and process pools, `Lock` and `Queue` for threads, and **parallel loading of CSV files with Pandas** | ~2.5 h |
| `02_exercises.ipynb` | 10 exercises with self-check cells | ~2 h |
| `solutions/02_solutions.ipynb` | Reference answers | — |
| `workers.py` | The worker functions that child processes run (imported by the notebooks; see tutorial Section 4) | — |
| `figures/` | Diagrams used in the tutorial (`make_figures.py` redraws them) | — |

**Learning outcomes.** Tell CPU-bound from I/O-bound work and choose threads or processes accordingly; explain what the GIL does and measure its effect; start, join and communicate with processes (`Process`, `Queue`); run independent tasks in a pool with `apply_async`, `map` and `starmap`, collect results and handle errors from workers; use `ThreadPoolExecutor` and `ProcessPoolExecutor`; protect shared data with a `Lock` and distribute work with a `Queue`; parallelise loading several CSV files and judge, by measuring, whether it pays off.

**Works on every OS.** Functions that run in a child process live in `workers.py`. In this Codespace (Linux, Python 3.12) notebook-defined functions would also work, but on Windows and macOS, and on Linux from Python 3.14, they cannot be found by the child process; the tutorial shows why.

**Syllabus:** Topic 4 — Multithreading and Parallelism: threading module, `ProcessPoolExecutor`, the GIL, concurrent data processing, `Queue` and `Lock` (see [Syllabus alignment](../README.md#syllabus-alignment)). Task: *parallelize a data loading task* → feeds into **Project Stage 2** (due Week 9), which needs multithreaded or parallel data fetching or processing.
