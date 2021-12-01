def read_input(day, input_type="str"):
    with open(f'inputs/day{day}.txt') as f:
        file_content = f.readlines()
        if input_type == "int":
            return [int(value) for value in file_content]
        return file_content

def read_input_int(day):
    return read_input(day, "int")
