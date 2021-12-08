from itertools import *

def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        return f.readlines()

def part_one(input):
    count = 0
    for code in [l.split(' ') for l in [l.strip().split('|')[1] for l in input]]:
        count += len([char for char in code if len(char) in [2, 3, 4, 7]])
    return count

def part_two(input):
    score = 0
    possible_letters = "abcdefg"
    digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    sorted_digits = sorted(digits)
    for line in input:
        input_v, output_v = line.split(" | ")
        for perm in permutations(possible_letters):
            letters_mutation = {i: j for i, j in zip(perm, possible_letters)}
            input_mutation = ["".join(sorted(map(letters_mutation.get, word))) for word in input_v.split()]
            if sorted_digits == sorted(input_mutation):
                output_mutation = ["".join(sorted(map(letters_mutation.get, word))) for word in output_v.split()]
                score += int("".join(str(digits.index(word)) for word in output_mutation))
    return score

input = read_input(8)

print(part_one(input))
print(part_two(input))
