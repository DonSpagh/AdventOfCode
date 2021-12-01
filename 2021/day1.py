import utils

def part_one(input):
    return sum([1 for i in range(0, len(input) - 1) if input[i+1] > input[i]])
    

def part_two(input):
    return sum([1 for i in range(0, len(input) - 3) if input[i+3] > input[i]])


input = utils.read_input_int(1)

print(part_one(input))
print(part_two(input))