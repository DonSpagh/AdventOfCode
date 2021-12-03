import utils

def part_one(input):
    gamma_rate = ''
    epsilon_rate = ''
    input_len = len(input)
    input_sums = [sum(i) for i in zip(*input)]
    for input_sum in input_sums:
        if input_sum > input_len / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def part_two(input):
    remaining_oxygen = input
    remaining_dioxygen = input

    i = 0
    while len(remaining_oxygen) > 1:
        input_len = len(remaining_oxygen)
        input_sums = [sum(i) for i in zip(*remaining_oxygen)]
        if input_sums[i] >= input_len / 2:
            remaining_oxygen = [value for value in remaining_oxygen if value[i] == 1]
        else:
            remaining_oxygen = [value for value in remaining_oxygen if value[i] == 0]
        i += 1

    i = 0
    while len(remaining_dioxygen) > 1:
        input_len = len(remaining_dioxygen)
        input_sums = [sum(i) for i in zip(*remaining_dioxygen)]
        if input_sums[i] < input_len / 2:
            remaining_dioxygen = [value for value in remaining_dioxygen if value[i] == 1]
        else:
            remaining_dioxygen = [value for value in remaining_dioxygen if value[i] == 0]
        i += 1

    return int(''.join(map(str, remaining_oxygen[0])), 2) * int(''.join(map(str, remaining_dioxygen[0])), 2)


input = utils.read_input_split_int(3)

print(part_one(input))
print(part_two(input))
