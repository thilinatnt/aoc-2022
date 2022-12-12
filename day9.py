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
    print("Day 9: Rope Bridge")
    with requests.get(input_path, cookies=cookies) as f:
        puzzle_input: str = f.text

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    visited = set()
    xh, yh = 0, 0
    xt, yt = 0, 0
    visited.add('0,0')

    for line in puzzle_input.splitlines():
        [direction, steps] = line.split(' ')
        match direction:
            case 'L':
                xh, xt, yt, _ = move_horizontally(steps, visited, xh, xt, yh, yt, False, [])
            case 'R':
                xh, xt, yt, _ = move_horizontally(steps, visited, xh, xt, yh, yt, True, [])
            case 'U':
                xt, yh, yt, _ = move_vertically(steps, visited, xh, xt, yh, yt, True, [])
            case 'D':
                xt, yh, yt, _ = move_vertically(steps, visited, xh, xt, yh, yt, False, [])

    return len(visited)


def move_vertically(steps, visited, xh, xt, yh, yt, increment, tail_steps):
    for _ in range(int(steps)):
        yh = yh + 1 if increment else yh - 1
        x_gap = abs(xh - xt)
        y_gap = abs(yh - yt)
        if y_gap > 1:
            yt = yt + 1 if increment else yt - 1
            if x_gap == 0:
                tail_steps.append(' '.join(['U' if increment else 'D', str(1)]))
            if x_gap == 1:
                if xh > xt:
                    xt += 1
                    tail_steps.append(' '.join(['UR' if increment else 'DR', str(1)]))
                else:
                    xt -= 1
                    tail_steps.append(' '.join(['UL' if increment else 'DL', str(1)]))
            visited.add(','.join([str(xt), str(yt)]))
    return xt, yh, yt, tail_steps


def move_horizontally(steps, visited, xh, xt, yh, yt, increment, tail_steps):
    for _ in range(int(steps)):
        xh = xh + 1 if increment else xh - 1
        x_gap = abs(xh - xt)
        y_gap = abs(yh - yt)
        if x_gap > 1:
            xt = xt + 1 if increment else xt - 1
            if y_gap == 0:
                tail_steps.append(' '.join(['R' if increment else 'L', str(1)]))
            if y_gap == 1:
                if yh > yt:
                    yt += 1
                    tail_steps.append(' '.join(['UR' if increment else 'UL', str(1)]))
                else:
                    yt -= 1
                    tail_steps.append(' '.join(['DR' if increment else 'DL', str(1)]))
            visited.add(','.join([str(xt), str(yt)]))
    return xh, xt, yt, tail_steps


def resolve_part2(puzzle_input: str) -> int:
    prev_tail_steps = puzzle_input.splitlines()

    for _ in range(9):
        visited = set()
        visited.add('0,0')
        xh, yh = 0, 0
        xt, yt = 0, 0
        tail_steps = []
        for line in prev_tail_steps:
            [direction, steps] = line.split(' ')
            match direction:
                case 'L':
                    xh, xt, yt, tail_steps = move_horizontally(steps, visited, xh, xt, yh, yt, False, tail_steps)
                case 'R':
                    xh, xt, yt, tail_steps = move_horizontally(steps, visited, xh, xt, yh, yt, True, tail_steps)
                case 'U':
                    xt, yh, yt, tail_steps = move_vertically(steps, visited, xh, xt, yh, yt, True, tail_steps)
                case 'D':
                    xt, yh, yt, tail_steps = move_vertically(steps, visited, xh, xt, yh, yt, False, tail_steps)
                case 'UR':
                    xh += 1
                    yh += 1
                    x_gap = abs(xh - xt)
                    y_gap = abs(yh - yt)
                    if x_gap > 1 or y_gap > 1:
                        if x_gap == 0:
                            yt += 1
                            tail_steps.append('U 1')
                        elif y_gap == 0:
                            xt += 1
                            tail_steps.append('R 1')
                        else:
                            xt += 1
                            yt += 1
                            tail_steps.append('UR 1')
                        visited.add(','.join([str(xt), str(yt)]))
                case 'UL':
                    xh -= 1
                    yh += 1
                    x_gap = abs(xh - xt)
                    y_gap = abs(yh - yt)
                    if x_gap > 1 or y_gap > 1:
                        if x_gap == 0:
                            yt += 1
                            tail_steps.append('U 1')
                        elif y_gap == 0:
                            xt -= 1
                            tail_steps.append('L 1')
                        else:
                            xt -= 1
                            yt += 1
                            tail_steps.append('UL 1')
                        visited.add(','.join([str(xt), str(yt)]))
                case 'DR':
                    xh += 1
                    yh -= 1
                    x_gap = abs(xh - xt)
                    y_gap = abs(yh - yt)
                    if x_gap > 1 or y_gap > 1:
                        if x_gap == 0:
                            yt -= 1
                            tail_steps.append('D 1')
                        elif y_gap == 0:
                            xt += 1
                            tail_steps.append('R 1')
                        else:
                            xt += 1
                            yt -= 1
                            tail_steps.append('DR 1')
                        visited.add(','.join([str(xt), str(yt)]))
                case 'DL':
                    xh -= 1
                    yh -= 1
                    x_gap = abs(xh - xt)
                    y_gap = abs(yh - yt)
                    if x_gap > 1 or y_gap > 1:
                        if x_gap == 0:
                            yt -= 1
                            tail_steps.append('D 1')
                        elif y_gap == 0:
                            xt -= 1
                            tail_steps.append('L 1')
                        else:
                            xt -= 1
                            yt -= 1
                            tail_steps.append('DL 1')
                        visited.add(','.join([str(xt), str(yt)]))

        prev_tail_steps = tail_steps.copy()

    return len(visited)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
