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
    print("Day 10: Cathode-Ray Tube")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    strength = []
    x = [1]
    cycles = 0
    target_cycles = 20

    for line in puzzle_input.splitlines():
        params = line.split()
        signal = params[0]
        register = int(params[1]) if len(params) > 1 else 0
        cycles = cycles + 1 if signal == 'noop' else cycles + 2

        if cycles >= target_cycles:
            strength.append(target_cycles * sum(x))
            target_cycles += 40

        x.append(register)

        if target_cycles > 220:
            break

    return sum(strength)


def resolve_part2(puzzle_input: str) -> None:
    x = [1]
    screen = [[], [], [], [], [], []]
    current_row = 0
    row_index = 0

    for line in puzzle_input.splitlines():
        params = line.split()
        signal = params[0]
        register = int(params[1]) if len(params) > 1 else 0
        cycles = 1 if signal == 'noop' else 2

        for _ in range(cycles):
            if sum(x) - 1 <= row_index <= sum(x) + 1:
                screen[current_row].insert(row_index, '#')
            else:
                screen[current_row].insert(row_index, '.')

            row_index += 1

            if row_index == 40:
                current_row += 1
                row_index = 0
                if current_row > 5:
                    break

        x.append(register)

    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in screen]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
