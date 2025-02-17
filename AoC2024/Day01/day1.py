import numpy as np


left, right = [], []


with open("input.txt", "r") as f:
    for line in f:
        a, b = line.split()

        left.append(int(a))
        right.append(int(b))

s_left = np.array(sorted(left, reverse=True))
s_right = np.array(sorted(right, reverse=True))

# Solution part 1
diff = np.abs(np.array(s_left) - np.array(s_right)) * [
    sum(s_right[s_right == i]) for i in s_left
]

print(f"Part1:\n\tThe sum of all diffs are {np.sum(diff)}")

# Solution part 2

part2 = sum(s_left * [sum(s_right == i) for i in s_left])

print(f"Part2:\n\tThe sum and product of all diffs are {np.sum(part2)}")
