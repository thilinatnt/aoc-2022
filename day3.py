#!/usr/bin/env python3
import sys
import requests
import time


def day(puzzle_no: str, token: object) -> None:
    input_path: str = f"https://adventofcode.com/2022/day/{puzzle_no}/input"
    cookies = {
        'session': token
    }

    print("Day 3: Rucksack Reorganization")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    start_time = time.time()
    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    print("--- %s seconds ---\n\n" % round((time.time() - start_time), 5))


def resolve_part1(puzzle_input: str) -> int:
    priorities_sum: int = 0

    for line in puzzle_input.splitlines():
        if line:
            first_compartment, second_compartment = line[:len(line) // 2], line[len(line) // 2:]
            common_item = list(set(first_compartment) & set(second_compartment))

            priority = ord(common_item[0]) - 96
            if priority < 0:
                priority = ord(common_item[0]) - 38

            priorities_sum += priority

    return priorities_sum


def resolve_part2(puzzle_input: str) -> int:
    priorities_sum: int = 0
    lines = puzzle_input.splitlines()

    for idx, line in enumerate(lines):
        if (idx + 1) % 3 == 0:
            common_item = list(set(lines[idx - 2]) & set(lines[idx - 1]) & set(lines[idx]))

            priority = ord(common_item[0]) - 96
            if priority < 0:
                priority = ord(common_item[0]) - 38

            priorities_sum += priority

    return priorities_sum


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
