import timeit
from statistics import median

import requests


def get_puzzle_input(puzzle_no, token):
    input_path: str = f"https://adventofcode.com/2022/day/{puzzle_no}/input"
    cookies = {
        'session': token
    }
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text
    return puzzle_input


def run_time(code: any):
    n = 100
    durations = timeit.Timer(code).repeat(repeat=n, number=1)
    print("\t--- %s ms ---\n" % round(median(durations) * 1000, 3))
