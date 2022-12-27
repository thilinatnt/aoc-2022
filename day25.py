#!/usr/bin/env python3
import sys

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 25: Full of Hot Air")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    # print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    # run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> str:
    total = 0
    for line in puzzle_input.splitlines():
        number = 0
        digits = reversed(list(line))

        for idx, digit in enumerate(digits):
            number += 5 ** idx * get_digit(digit)

        total += number

    return ''.join(get_snafu(total, []))


def get_digit(val: str) -> int:
    match val:
        case '2':
            return 2
        case '1':
            return 1
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2


def get_snafu(number: int, snafu: list) -> list[str]:
    total = 0
    y = 0
    x = -1
    while total < number:
        x += 1
        total += 5 ** x
        if total >= number:
            y = 1
        else:
            total += 5 ** x
            y = 2

    snafu.append(str(y))
    snafu = get_snafu1(x - 1, (5 ** x) * y - number, snafu)
    return snafu


def get_snafu1(x: int, remainder: int, snafu: list) -> list[str]:
    if x < 0:
        return snafu

    y = -2
    y_char = '='
    min_gap = abs((5 ** x) * -2 + remainder)

    if abs((5 ** x) * -1 + remainder) < min_gap:
        min_gap = abs((5 ** x) * -1 + remainder)
        y = -1
        y_char = '-'

    if abs((5 ** x) * 0 + remainder) < min_gap:
        min_gap = abs((5 ** x) * 0 + remainder)
        y = 0
        y_char = '0'

    if abs((5 ** x) * 1 + remainder) < min_gap:
        min_gap = abs((5 ** x) * 1 + remainder)
        y = 1
        y_char = '1'

    if abs((5 ** x) * 2 + remainder) < min_gap:
        min_gap = abs((5 ** x) * 2 + remainder)
        y = 2
        y_char = '2'

    snafu.append(y_char)
    snafu = get_snafu1(x - 1, remainder + (5 ** x) * y, snafu)
    return snafu


# def resolve_part2(puzzle_input: str) -> None:
#
#     for line in puzzle_input.splitlines():


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
