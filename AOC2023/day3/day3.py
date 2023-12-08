import numpy as np


def walk_to_numbers(data, number, x, y):
    try:
        if 48 <= ord(data[x][y+1]) <= 57:
            number.append(data[x][y+1])
            walk_pos(data, number, x, y+1)
    except IndexError:
        print(f"Index out of range at {x} {y}")
    try:
        if 48 <= ord(data[x][y-1]) <= 57:
            number.insert(0, data[x][y-1])
            walk_neg(data, number, x, y-1)
    except IndexError:
        print(f"Index out of range at {x} {y}")
    # print(number)
    return number


def walk_neg(data, number, x, y):
    try:
        if 48 <= ord(data[x][y-1]) <= 57:
            number.insert(0, data[x][y-1])
            walk_neg(data, number, x, y-1)
    except IndexError:
        print(f"Index out of range at {x} {y}")


def walk_pos(data, number, x, y):
    try:
        if 48 <= ord(data[x][y+1]) <= 57:
            number.append(data[x][y+1])
            walk_pos(data, number, x, y+1)
    except IndexError:
        print(f"Index out of range at {x} {y}")


with open("input", "r") as file:
    inpt = file.read().splitlines()


def part_one(inpt):
    solution = 0

    for i, j in enumerate(inpt):
        for k, l in enumerate(j):
            if l in "/#=$-@&*%+":
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if not a and not b:
                            continue
                        try:
                            c = inpt[i+a][k+b]
                            if 48 <= ord(c) <= 57:
                                tmp = int("".join(walk_to_numbers(inpt,
                                                                  [inpt[i+a][k+b]], i+a, k+b)))
                                solution += tmp
                                if (a == -1 or a == 1):
                                    if inpt[i+a][k] != ".":
                                        break
                            # input()
                        except IndexError:
                            print(f"Index out of range at {i+a} {k+b}")
                            pass
                        except Exception as e:
                            raise e
    return solution


def part_two(inpt):
    solution = 0
    n_neighbours = []
    for i, j in enumerate(inpt):
        for k, l in enumerate(j):
            if l in "*":
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if not a and not b:
                            continue
                        try:
                            c = inpt[i+a][k+b]
                            if 48 <= ord(c) <= 57:

                                n_neighbours.append(int("".join(walk_to_numbers(inpt,
                                                                                [inpt[i+a][k+b]], i+a, k+b))))
                                if (a == -1 or a == 1):
                                    if inpt[i+a][k] != ".":
                                        break
                            # input()
                        except IndexError:
                            print(f"Index out of range at {i+a} {k+b}")
                            pass
                        except Exception as e:
                            raise e
                if len(n_neighbours) == 2:
                    solution += np.prod(n_neighbours)
                n_neighbours = []
    return solution


print("Part one ", part_one(inpt))
print("Part two ", part_two(inpt))
