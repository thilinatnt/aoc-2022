#!/usr/bin/env python3
import sys
import requests
import time


def day(puzzle_no: str, token: object) -> None:
    input_path: str = f"https://adventofcode.com/2022/day/{puzzle_no}/input"
    cookies = {
        'session': token
    }

    print("Day 4: Camp Cleanup")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    start_time = time.time()
    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    print("--- %s seconds ---\n\n" % round((time.time() - start_time), 5))


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
