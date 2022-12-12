#!/usr/bin/env python3
import sys

import requests

from util import run_time


def day(puzzle_no: str, token: object) -> None:
    input_path: str = f"https://adventofcode.com/2022/day/{puzzle_no}/input"
    cookies = {
        'session': token
    }

    print("-------------------------\n")
    print("Day 12: Hill Climbing Algorithm")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    # run_time(lambda: resolve_part1(puzzle_input))
    # print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    # run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:

    # for line in puzzle_input.splitlines():

    return 5


# def resolve_part2(puzzle_input: str) -> None:
#
#     for line in puzzle_input.splitlines():


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
