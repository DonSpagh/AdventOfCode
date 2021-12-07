def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        return [int(x) for x in f.read().rstrip().split(',')]

def compute_median(input):
    input.sort()
    mid = len(input) // 2
    if len(input) % 2 == 0:
        median = (input[mid] + input[mid-1]) / 2
    else:
        median = input[mid]
    return int(median)

def part_one(input):
    median = compute_median(input)
    return sum([abs(i - median) for i in input])

def part_two(input):
    mean = round(sum(input) / len(input))
    distance_to_mean = [abs(i - mean) for i in input]
    return sum([sum(i) for i in [range(0, int(i+1)) for i in distance_to_mean]])

input = read_input(7)

print(part_one(input))
print(part_two(input))
