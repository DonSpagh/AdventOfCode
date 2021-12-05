def read_input(day, input_type="str"):
    with open(f'inputs/day{day}.txt', 'r') as f:
        file_content = f.readlines()
        if input_type == "int":
            return [int(value) for value in file_content]
        if input_type == "split_int":
            res = []
            for value in file_content:
                split_value = list(value.rstrip())
                res.append([int(v) for v in split_value])
            return res

def read_input_int(day):
    return read_input(day, "int")

def read_input_split_int(day):
    return read_input(day, "split_int")
