#!/usr/bin/env python3
import sys
import requests
import time


def day(puzzle_no: str, token: object) -> None:
    input_path: str = f"https://adventofcode.com/2022/day/{puzzle_no}/input"
    cookies = {
        'session': token
    }

    print("Day 1: Calorie Counting")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    start_time = time.time()
    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    print("--- %s seconds ---\n\n" % round(time.time() - start_time, 5))


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
