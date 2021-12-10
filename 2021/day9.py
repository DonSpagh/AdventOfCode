def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
    heights = []
    line_length = len(lines[0])
    for line in lines:
        heights += [int(i) for i in line]
    return heights, line_length

def find_basin(basin, index):
    if heights[index] == 9:
        return [len(set(basin))]
    basin.append(index)
    to_visit = []
    if 0 <= index-line_length < len(heights) and index-line_length not in basin:
        to_visit.append(index-line_length)
    if index % (line_length) != 0 and index-1 >= 0 and index-1 not in basin:
        to_visit.append(index-1)
    if (index+1) % line_length != 0 and index+1 < len(heights) and index+1 not in basin:
        to_visit.append(index+1)
    if 0 <= index+line_length < len(heights) and index+line_length not in basin:
        to_visit.append(index+line_length)
    return sum([find_basin(basin, x) for x in to_visit], [])

def find_low_points(heights, line_length, part_two=False):
    low_points = []
    heights_length = len(heights)
    for i in range(heights_length):
        neighbours = []
        if 0 <= i-line_length < heights_length:
            neighbours.append(heights[i-line_length])
        if 0 <= i-1 < heights_length:
            neighbours.append(heights[i-1])
        if 0 <= i+1 < heights_length:
            neighbours.append(heights[i+1])
        if 0 <= i+line_length < heights_length:
            neighbours.append(heights[i+line_length])
        if heights[i] < min(neighbours):
            if part_two:
                low_points.append(i)
            else:
                low_points.append(heights[i])
    return low_points

def part_one():
    low_points = find_low_points(heights, line_length)
    return sum(low_points) + len(low_points)

def part_two():
    low_points_indices = find_low_points(heights, line_length, True)
    basins_lengths = sorted([max(b) for b in [find_basin([], x) for x in low_points_indices]])
    return basins_lengths[-1] * basins_lengths[-2] * basins_lengths[-3]

heights, line_length = read_input(9)

print(part_one())
print(part_two())