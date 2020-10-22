from fnmatch import fnmatch
from os import listdir
from os.path import isfile, join

DATA_DIR = "/home/data"


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def get_all_files():
    files = [
        f
        for f in listdir(DATA_DIR)
        if isfile(join(DATA_DIR, f)) and fnmatch(f, "*.txt")
    ]
    print(files)
