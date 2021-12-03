import utils

def part_one(input):
    gamma_rate = ""
    epsilon_rate = ""
    input_len = len(input)
    input_sums = [sum(i) for i in zip(*input)]
    for input_sum in input_sums:
        if input_sum > input_len / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def part_two(input):
    return input


input = utils.read_input_split_int(3)

print(part_one(input))
print(part_two(input))
