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
    print("Day 8: Treetop Tree House")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    columns, rows = get_rows_columns(puzzle_input)

    result = 0
    for rx, row in enumerate(rows):
        for ry, col in enumerate(row):
            if 0 < ry < len(row) - 1 and 0 < rx < len(rows) - 1:
                left_items = row[0:ry]
                right_items = row[ry + 1::]
                top_items = columns[ry][0:rx]
                bottom_items = columns[ry][rx + 1::]

                if min([max(left_items, default=0), max(right_items, default=0), max(top_items, default=0),
                        max(bottom_items, default=0)]) < col:
                    result += 1

    result += (2 * len(rows)) + (2 * len(columns)) - 4
    return result


def resolve_part2(puzzle_input: str) -> int:
    columns, rows = get_rows_columns(puzzle_input)

    result = 0
    for rx, row in enumerate(rows):
        for ry, col in enumerate(row):
            if 0 < ry < len(row) - 1 and 0 < rx < len(rows) - 1:
                left_items = row[0:ry]
                right_items = row[ry + 1::]
                top_items = columns[ry][0:rx]
                bottom_items = columns[ry][rx + 1::]

                res = get_first_match(col, left_items[::-1]) * get_first_match(col, right_items) * get_first_match(
                    col, top_items[::-1]) * get_first_match(col, bottom_items)
                result = res if res > result else result

    return result


def get_first_match(col, items):
    for i, j in enumerate(items):
        if j >= col:
            return i + 1
    return len(items)


def get_rows_columns(puzzle_input):
    rows = []
    columns = []
    for idx, line in enumerate(puzzle_input.splitlines()):
        row = [int(c) for c in line]
        rows.append(row)

        for idy, row_item in enumerate(row):
            if len(columns) > idy:
                columns[idy].append(row_item)
            else:
                columns.append([row_item])
    return columns, rows


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
