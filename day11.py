#!/usr/bin/env python3
import sys

from util import get_puzzle_input


def day(puzzle_no: str, token: object) -> None:
    puzzle_input = get_puzzle_input(puzzle_no, token)

    print("-------------------------\n")
    print("Day 11: Monkey in the Middle")

    print(f"\tAnswer Part1: {resolve_part1(puzzle_input)}")
    # run_time(lambda: resolve_part1(puzzle_input))
    print(f"\tAnswer Part2: {resolve_part2(puzzle_input)}")
    # run_time(lambda: resolve_part2(puzzle_input))


def ops(index: int, old: int) -> int:
    match index:
        case 0:
            return old * 13
        case 1:
            return old + 3
        case 2:
            return old * old
        case 3:
            return old + 5
        case 4:
            return old + 7
        case 5:
            return old + 4
        case 6:
            return old * 19
        case 7:
            return old + 2


def resolve_part1(puzzle_input: str) -> int:
    monkeys = [
        {'items': [52, 78, 79, 63, 51, 94], 'index': 0, 'divide': 5, 'testTrue': 1, 'testFalse': 6, 'inspections': 0},
        {'items': [77, 94, 70, 83, 53], 'index': 1, 'divide': 7, 'testTrue': 5, 'testFalse': 3, 'inspections': 0},
        {'items': [98, 50, 76], 'index': 2, 'divide': 13, 'testTrue': 0, 'testFalse': 6, 'inspections': 0},
        {'items': [92, 91, 61, 75, 99, 63, 84, 69], 'index': 3, 'divide': 11, 'testTrue': 5, 'testFalse': 7,
         'inspections': 0},
        {'items': [51, 53, 83, 52], 'index': 4, 'divide': 3, 'testTrue': 2, 'testFalse': 0, 'inspections': 0},
        {'items': [76, 76], 'index': 5, 'divide': 2, 'testTrue': 4, 'testFalse': 7, 'inspections': 0},
        {'items': [75, 59, 93, 69, 76, 96, 65], 'index': 6, 'divide': 17, 'testTrue': 1, 'testFalse': 3,
         'inspections': 0},
        {'items': [89], 'index': 7, 'divide': 19, 'testTrue': 2, 'testFalse': 4, 'inspections': 0}
    ]

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey['items'].copy():
                worry_level = ops(monkey['index'], item) // 3
                remainder = worry_level % monkey['divide']
                monkey['inspections'] += 1
                monkey['items'].pop(0)
                if remainder == 0:
                    monkeys[monkey['testTrue']]['items'].append(worry_level)
                else:
                    monkeys[monkey['testFalse']]['items'].append(worry_level)

    print(f"\tInspections: {[d['inspections'] for d in monkeys]}")


def resolve_part2(puzzle_input: str) -> None:
    monkeys = [
        {'items': [52, 78, 79, 63, 51, 94], 'index': 0, 'divide': 5, 'testTrue': 1, 'testFalse': 6, 'inspections': 0},
        {'items': [77, 94, 70, 83, 53], 'index': 1, 'divide': 7, 'testTrue': 5, 'testFalse': 3, 'inspections': 0},
        {'items': [98, 50, 76], 'index': 2, 'divide': 13, 'testTrue': 0, 'testFalse': 6, 'inspections': 0},
        {'items': [92, 91, 61, 75, 99, 63, 84, 69], 'index': 3, 'divide': 11, 'testTrue': 5, 'testFalse': 7,
         'inspections': 0},
        {'items': [51, 53, 83, 52], 'index': 4, 'divide': 3, 'testTrue': 2, 'testFalse': 0, 'inspections': 0},
        {'items': [76, 76], 'index': 5, 'divide': 2, 'testTrue': 4, 'testFalse': 7, 'inspections': 0},
        {'items': [75, 59, 93, 69, 76, 96, 65], 'index': 6, 'divide': 17, 'testTrue': 1, 'testFalse': 3,
         'inspections': 0},
        {'items': [89], 'index': 7, 'divide': 19, 'testTrue': 2, 'testFalse': 4, 'inspections': 0}
    ]

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey['items'].copy():
                worry_level = ops(monkey['index'], item)
                remainder = worry_level % monkey['divide']
                monkey['inspections'] += 1
                monkey['items'].pop(0)
                if remainder == 0:
                    monkeys[monkey['testTrue']]['items'].append(worry_level % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19))
                else:
                    monkeys[monkey['testFalse']]['items'].append(worry_level % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19))

    print(f"\tInspections: {[d['inspections'] for d in monkeys]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("must provide puzzle input url and session")

    day(sys.argv[1], sys.argv[2])
