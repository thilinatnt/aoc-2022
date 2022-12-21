#!/usr/bin/env python3
import sys

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 4: Camp Cleanup")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    total: int = 0

    for line in puzzle_input.splitlines():
        if line:
            assignments = line.replace(',', '-').split('-')
            if (int(assignments[0]) <= int(assignments[2]) and int(assignments[1]) >= int(assignments[3])) or (int(
                    assignments[2]) <= int(assignments[0]) and int(assignments[3]) >= int(assignments[1])):
                total += 1

    return total


def resolve_part2(puzzle_input: str) -> int:
    total: int = 0

    for line in puzzle_input.splitlines():
        if line:
            assignments = line.replace(',', '-').split('-')
            if (int(assignments[2]) <= int(assignments[0]) <= int(assignments[3])) or (
                    int(assignments[2]) <= int(assignments[1]) <= int(assignments[3])) or (
                    int(assignments[0]) <= int(assignments[2]) <= int(assignments[1])) or (
                    int(assignments[0]) <= int(assignments[3]) <= int(assignments[1])):
                total += 1

    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
