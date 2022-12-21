#!/usr/bin/env python3
import sys

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)
    print("-------------------------\n")
    print("Day 6: Tuning Trouble")

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
