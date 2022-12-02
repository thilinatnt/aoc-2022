#!/usr/bin/env python3
import sys
import requests

cookies = {
    'session': sys.argv[2]
}


def day(path: str) -> None:
    print("Day 1: Calorie Counting")
    with requests.get(path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer: {resolve(puzzle_input)}")


def resolve(puzzle_input: str) -> int:
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1])
