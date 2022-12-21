#!/usr/bin/env python3
import sys

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 5: Supply Stacks")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> str:
    stacks = [[], [], [], [], [], [], [], [], []]

    for line in puzzle_input.splitlines():
        if line and line.startswith('['):
            line_items = line.replace('    ', ' ').replace('[', '').replace(']', '').split(' ')
            for idx, line_item in enumerate(line_items):
                if line_item:
                    if stacks[idx]:
                        stacks[idx].insert(0, line_item)
                    else:
                        stacks[idx] = [line_item]

        if line and line.startswith('move'):
            instruction = line.split()

            no_move = int(instruction[1])
            from_col = int(instruction[3]) - 1
            to_col = int(instruction[5]) - 1

            stacks[to_col].extend(stacks[from_col][:-no_move - 1:-1])
            stacks[from_col] = stacks[from_col][:-no_move]

    result = ''
    for i in range(len(stacks)):
        result += stacks[i][-1]

    return result


def resolve_part2(puzzle_input: str) -> str:
    stacks = [[], [], [], [], [], [], [], [], []]

    for line in puzzle_input.splitlines():
        if line and line.startswith('['):
            line_items = line.replace('    ', ' ').replace('[', '').replace(']', '').split(' ')
            for idx, line_item in enumerate(line_items):
                if line_item:
                    if stacks[idx]:
                        stacks[idx].insert(0, line_item)
                    else:
                        stacks[idx] = [line_item]

        if line and line.startswith('move'):
            instruction = line.split()

            no_move = int(instruction[1])
            from_col = int(instruction[3]) - 1
            to_col = int(instruction[5]) - 1

            stacks[to_col].extend(stacks[from_col][-no_move:])
            stacks[from_col] = stacks[from_col][:-no_move]

    result = ''
    for i in range(len(stacks)):
        result += stacks[i][-1]

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
