"""
Worker functions for Week 6 (multithreading and parallelism).

Why a separate file?  A child process must be able to *import* the function it runs.
On Windows and macOS (and on Linux from Python 3.14) new processes start fresh and
import functions by name, so a function defined only inside a notebook cannot be
found there.  Functions in this module work on every operating system.

The notebooks import it with:   import workers   (or: from workers import ...)
"""
from __future__ import annotations

import math
import multiprocessing
import sys
import time
from pathlib import Path


# --------------------------------------------------------------------------- slides 9, 11, 12
def count_numbers(nums):
    """Slide 9: print 0 .. nums-1, half a second apart."""
    for i in range(0, nums):
        print(i, "/", nums, flush=True)
        time.sleep(0.5)


def count_total(nums):
    """Slides 11-12: print the running total and return it."""
    total = 0
    for i in range(0, nums):
        print(total, flush=True)
        total += i
        time.sleep(0.5)
    return total


def count_total_quiet(nums, delay=0.2):
    """Like count_total, without printing (used in the exercises)."""
    total = 0
    for i in range(0, nums):
        total += i
        time.sleep(delay)
    return total


# --------------------------------------------------------------------------- authors' notebook 12
def square_numbers():
    for i in range(5):
        time.sleep(0.4)
        print(f"Square: {i * i}", flush=True)


def cube_numbers():
    for i in range(5):
        time.sleep(0.6)
        print(f"Cube: {i * i * i}", flush=True)


def square_number(number):
    time.sleep(0.5)
    return f"Square: {number * number}"


def compute_factorial(number):
    """Notebook 12, section 13.7 (CPU-bound): the factorial of a large number."""
    return math.factorial(number)


def factorial_digits(number):
    """How many decimal digits number! has."""
    sys.set_int_max_str_digits(0)          # allow converting very long integers to text
    return len(str(math.factorial(number)))


# --------------------------------------------------------------------------- small building blocks
def square(x):
    """Slide 18."""
    return x ** 2


def power(base, exponent):
    return base ** exponent


def reciprocal(x):
    """1 / x; raises ZeroDivisionError for 0 (used to practise error handling)."""
    return 1 / x


def whoami(x):
    """Return the value together with the name of the process that handled it."""
    return x, multiprocessing.current_process().name


def cpu_task(n):
    """A CPU-bound task: pure-Python arithmetic, no waiting."""
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


def fake_download(url, delay=0.3):
    """An I/O-bound task: waits as if for a server, then returns (url, size)."""
    time.sleep(delay)
    return url, len(url) * 100


def square_to_queue(n, queue):
    """Run in a child process: put (n, n squared) into a shared queue."""
    queue.put((n, n * n))


def append_to_list(values, x):
    """Try to change a list in a child process (it changes only the child's copy)."""
    values.append(x)
    print("inside the child:", values, flush=True)


# --------------------------------------------------------------------------- slide 14: parallel loading
def read_student(filename):
    """Slide 14 as written: read one row at a time and grow a DataFrame."""
    import pandas as pd      # imported here so that starting a worker process stays fast
    students = pd.DataFrame()
    df = pd.read_csv(filename, chunksize=1)
    for d in df:
        students = pd.concat([students, d], axis=0, ignore_index=True)
    return students


def read_csv_file(path):
    """The modern version: one call reads the whole file."""
    import pandas as pd
    return pd.read_csv(path)


def make_student_files(data_dir, n_files=4, out_name="week06"):
    """Split students.csv into n_files parts: students1.csv, students2.csv, ...

    Returns the list of paths. Safe to call again: existing files are overwritten.
    """
    import pandas as pd
    data_dir = Path(data_dir)
    out = data_dir / out_name
    out.mkdir(exist_ok=True)
    students = pd.read_csv(data_dir / "students.csv")
    size = math.ceil(len(students) / n_files)
    paths = []
    for k in range(n_files):
        part = students.iloc[k * size:(k + 1) * size]
        path = out / f"students{k + 1}.csv"
        part.to_csv(path, index=False)
        paths.append(path)
    return paths
