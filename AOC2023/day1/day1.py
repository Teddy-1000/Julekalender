import re


inpt = []


def replace_string_number(string):
    replacement = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r",
                   "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

    # first_appearance = re.findall("|".join(replacement.keys()), string)
    for i in replacement:
        string = string.replace(i, replacement[i])
    return string


def get_number(string):
    numbers = re.findall(r"[0-9]", string)
    return int("".join([numbers[0], numbers[-1]]))


with open("input", "r") as file:
    for line in file:
        inpt.append(get_number(replace_string_number(line.strip())))


print(f"Sum of calibration {sum(inpt)}")


def test():
    f = open('input', 'r')
    a = f.readlines()
    real = []

    translation = {'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
                   'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    for line in a:
        for key, value in translation.items():
            line = line.replace(key, value)
            nums = [int(j) for j in [*line] if j.isdigit()]
            real.append(int(''.join([str(nums[0]), str(nums[-1])])))
    code = sum(real)
    print(code)


test()
