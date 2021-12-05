import re
import sys

def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        file_content = f.read().split('\n\n')

    draw = map(int, file_content[0].split(','))
    boards = [[[[int(x), 0] for x in row.split()] for row in line.split('\n')] for line in file_content[1:]]
    return draw, boards

def mark_boards(boards, number):
    for board in boards:
        for line in board:
            for n in line:
                if n[0] == number:
                    n[1] = 1

def has_won(board):
    board_marks = [[el[1] for el in line] for line in board]
    for i, line in enumerate(board_marks):
        if sum(line) == 5 or sum([line[i] for line in board_marks]) == 5:
            return True
    return False

def part_one(draw, boards):
    for number in draw:
        mark_boards(boards, number)

        for board in boards:
            if has_won(board):
                return number * sum(map(sum, [[el[0] for el in line if el[1] == 0] for line in board]))


def part_two(draw, boards):
    for number in draw:
        mark_boards(boards, number)

        for board in boards:
            if has_won(board):
                boards.remove(board)

        if len(boards) == 0:
            return number * sum(map(sum, [[el[0] for el in line if el[1] == 0] for line in board]))


draw, boards = read_input(4)

print(part_one(draw, boards))
print(part_two(draw, boards))
