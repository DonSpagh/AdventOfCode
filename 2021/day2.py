import utils

def part_one(input):
    distance = 0
    depth = 0

    for i in input:
        direction, value = i.split(' ')
        value = int(value)
        if direction == 'forward':
            distance += value
        elif direction == 'down':
            depth += value
        if direction == 'up':
            depth -= value

    return distance * depth

def part_two(input):
    distance = 0
    depth = 0
    aim = 0
    
    for i in input:
        direction, value = i.split(' ')
        value = int(value)
        if direction == 'forward':
            distance += value
            depth += value * aim
        elif direction == 'down':
            aim += value
        if direction == 'up':
            aim -= value

    return distance * depth


input = utils.read_input(2)

print(part_one(input))
print(part_two(input))
