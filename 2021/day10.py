from queue import LifoQueue

open_close_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
char_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
char_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def read_input(day):
    with open(f'inputs/day{day}.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
    return lines

def part_one(input):
    score = 0
    for line in input:
        q = LifoQueue()
        for char in line:
            if char in open_close_chars.keys():
                q.put(char)
            elif char in open_close_chars.values():
                if q.empty():
                    score += char_scores[char]
                    break
                if char != open_close_chars[q.get()]:
                    score += char_scores[char]
                    break

    return score

def part_two(input):
    scores = []
    for line in input:
        q = LifoQueue()
        is_corrupted = False
        score = 0
        for char in line:
            if char in open_close_chars.keys():
                q.put(char)
            elif char in open_close_chars.values():
                if q.empty():
                    is_corrupted = True
                    break
                if char != open_close_chars[q.get()]:
                    is_corrupted = True
                    break
        if not is_corrupted:
            while not q.empty():
                score *= 5
                score += char_values[open_close_chars[q.get()]]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]

input = read_input(10)

print(part_one(input))
print(part_two(input))
