#!/usr/bin/env python3
import sys

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 1: Calorie Counting")
    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    calories: int = 0
    highest_calories: int = 0
    for line in puzzle_input.splitlines():
        if not line:
            if calories > highest_calories:
                highest_calories = calories
            calories = 0
        else:
            calories += int(line)

    return highest_calories


def resolve_part2(puzzle_input: str) -> int:
    calories: int = 0
    calories_list = []
    for line in puzzle_input.splitlines():
        if not line:
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line)
    calories_list.sort(reverse=True)
    return calories_list[0] + calories_list[1] + calories_list[2]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
