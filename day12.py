#!/usr/bin/env python3
import sys

from util import get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 12: Hill Climbing Algorithm")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    # run_time(lambda: resolve_part1(puzzle_input))
    # print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    # run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    grid = []
    start = None
    target = None
    for line in puzzle_input.splitlines():
        row = list(line)
        grid.append(row)

        if 'S' in row:
            start = [row.index('S'), len(grid) - 1]
        if 'E' in row:
            target = [row.index('E'), len(grid) - 1]

    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in grid]))
    print(f"\tStart: {start}")
    print(f"\tTarget: {target}")
    return 5


# def resolve_part2(puzzle_input: str) -> None:
#
#     for line in puzzle_input.splitlines():


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
