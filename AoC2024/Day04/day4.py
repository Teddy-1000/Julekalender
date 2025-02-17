import numpy as np

inpt = []

with open("input.txt", "r") as file:
    for line in file:
        inpt.append(np.array([i for i in line.strip()]))

xmas_counter = 0

inpt = np.array(inpt)

target_word = np.array(["X", "M", "A", "S"])


def find_xmas(subset):
    sub_counter = 0
    if all(subset[0:4, 0:4].diagonal()[::-1] == target_word):
        sub_counter += 1
    if all(subset[3:, 3:].diagonal() == target_word):
        sub_counter += 1
    if all(subset[:4, 3:][::1][::-1].diagonal()[::-1] == target_word):
        sub_counter += 1
    if all(subset[:4][::-1].diagonal() == target_word):
        sub_counter += 1
    if all(subset[3, 3:] == target_word):
        sub_counter += 1
    if all(subset[3, :4][::-1] == target_word):
        sub_counter += 1
    if all(subset[:4, 3][::-1] == target_word):
        sub_counter += 1
    if all(subset[3:, 3] == target_word):
        sub_counter += 1
    return sub_counter


input_pad = np.pad(inpt, 3, mode="empty")

for x, _ in enumerate(input_pad):
    for y, letter in enumerate(_):
        if letter == "X":
            try:
                xmas_counter += find_xmas(input_pad[x - 3 : x + 4, y - 3 : y + 4])
            except IndexError:
                print(f"Got error at {x},{y}")
                pass

print(f"The number of xmas is {xmas_counter}")
