import re


with open("input.txt", "r") as file:
    input = file.read().replace("\n", "")


regex_ptrn = r"mul\(\d+,\d+\)"

all_mulls = re.findall(regex_ptrn, input)


def mul(x, y):
    return int(x) * int(y)


def interpret_muls(commands):
    return sum([eval(i) for i in commands])


print(f"Part1:\n\tThe sum of all the multiplications is {interpret_muls(all_mulls)}")


regex_ptrn = r"(don\'t\(\)|do\(\)|mul\(\d+,\d+\))"

all_commands = re.findall(regex_ptrn, input)

do = True
muls = []

for i in all_commands:
    if i == "do()":
        do = True
    elif i == "don't()":
        do = False
    elif do:
        muls.append(i)


print(f"Part2:\n\tThe sum of all the multiplications is {interpret_muls(muls)}")
