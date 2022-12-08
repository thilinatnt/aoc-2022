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
    print("Day 6: Tuning Trouble")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    buffer = list(puzzle_input)

    for idx, signal in enumerate(buffer):
        if signal and idx > 2:
            signals = set(buffer[(idx - 3):idx + 1])
            if len(signals) == 4:
                return idx + 1

    return 0


def resolve_part2(puzzle_input: str) -> int:
    buffer = list(puzzle_input)

    for idx, signal in enumerate(buffer):
        if signal and idx > 12:
            signals = set(buffer[(idx - 13):idx + 1])
            if len(signals) == 14:
                return idx + 1

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
