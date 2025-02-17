import numpy as np

input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append([int(i) for i in line.split()])


def is_safe(report: np.ndarray) -> bool:
    if (all(report < 0) or all(report > 0)) and all(np.abs(report) <= 3):
        return True
    return False


n_safe_reports = 0

for i in [np.diff(i) for i in input]:
    if is_safe(i):
        n_safe_reports += 1


# Part1 solution
print(f"Part1:\n\tThere is {n_safe_reports} safe reports")


n_safe_reports = 0


def test_sub_arrays(report):
    for j in range(len(report)):
        mask = np.ones(len(report), dtype=bool)
        mask[j] = False
        if is_safe(report[mask]):
            return True
    return False


for i, j in zip([np.diff(i) for i in input], [np.diff(i[::-1]) for i in input]):
    if (is_safe(i) and is_safe(j)) or (test_sub_arrays(i) and test_sub_arrays(j)):
        n_safe_reports += 1


print(f"Part2:\n\tThere is {n_safe_reports} safe reports")
