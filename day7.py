#!/usr/bin/env python3
import sys
from collections import defaultdict

from util import run_time, get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 7: No Space Left On Device")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    run_time(lambda: resolve_part2(puzzle_input))


def resolve_part1(puzzle_input: str) -> int:
    result = 0
    folders = get_folders(puzzle_input)

    for value in filter(lambda score: score <= 100000, folders.values()):
        result += value

    return result


def resolve_part2(puzzle_input: str) -> int:
    folders = get_folders(puzzle_input)

    total_size = folders["/"]
    need_space = 70000000 - total_size
    free_up_space = 30000000 - need_space

    return sorted(x for x in folders.values() if x >= free_up_space)[0]


def process_folder_end(children, folders, parent_folders):
    key = '.'.join(parent_folders)
    total_size = 0
    for child in children[key]:
        total_size += folders[child]

    total_size += folders[key]

    folders[key] = total_size
    parent_folders.pop()


def get_folders(puzzle_input):
    folders = defaultdict(int)
    children = defaultdict(list)
    parent_folders = []

    for line in puzzle_input.splitlines():
        if line and line.startswith('dir'):
            key = '.'.join(parent_folders)
            child_key = '.'.join([key, line.split(' ')[1]])
            children[key].append(child_key)

        if line and line[0].isdigit():
            key = '.'.join(parent_folders)
            folders[key] += int(line.split(' ')[0])

        if line and line.startswith('$ cd ..'):
            process_folder_end(children, folders, parent_folders)

        else:
            if line and line.startswith('$ cd'):
                parent_folders.append(line.split(' ')[2])

    for _ in parent_folders.copy():
        process_folder_end(children, folders, parent_folders)
    return folders


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
