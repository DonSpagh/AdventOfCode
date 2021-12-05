import re
import sys

def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        file_content = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)\n', f.read())
        points = [[int(x) for x in line] for line in file_content]
    return points

def add_point(points_count, point):
    if point in points_count:
        points_count[point] += 1
    else:
        points_count[point] = 1

def build_points(points_count, x1, y1, x2, y2, diag=False): 
    if x1 == x2:
        for x in range(min(y1, y2), max(y1, y2)+1):
            add_point(points_count, str(x1) + ':' + str(x))
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            add_point(points_count, str(x) + ':' + str(y1))
    if diag and abs(y2 - y1) == abs(x2 - x1):
        incx = 1 if x1 < x2 else -1
        incy = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2+incx, incx):
            add_point(points_count, str(x) + ':' + str(y))
            y += incy

def part_one(input):
    points_count = {}
    for points in input:
        build_points(points_count, *points)
    return sum([1 for x in points_count.values() if x >= 2])


def part_two(input):
    points_count = {}
    for points in input:
        build_points(points_count, *points, True)
    return sum([1 for x in points_count.values() if x >= 2])


input = read_input(5)

print(part_one(input))
print(part_two(input))