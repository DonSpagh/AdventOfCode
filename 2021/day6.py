def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        return [int(x) for x in f.read().rstrip().split(',')]

def compute(input, days):
    fish_counts = [input.count(i) for i in range(0, 9)]
    for i in range(0, days):
        births = fish_counts.pop(0)
        fish_counts[6] += births
        fish_counts.append(births)
    return sum(fish_counts)

def part_one(input):
    return compute(input, 80)

def part_two(input):
    return compute(input, 256)

input = read_input(6)

print(part_one(input))
print(part_two(input))
