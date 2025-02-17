import numpy as np


with open("input.txt", "r") as file:
    inpt = file.readlines()
    inpt = [list(i.strip()) for i in inpt]

moves = {
    "^": np.array([-1, 0]),
    ">": np.array([0, 1]),
    "<": np.array([0, -1]),
    "v": np.array([1, 0]),
}
rotate = {"^": ">", ">": "v", "v": "<", "<": "^"}
puzzle = np.array(inpt, dtype=str)


def is_inbound(array, pos):
    return (pos >= 0).all() and (pos < array.shape).all()


def solve_puzzle(inpt_array):
    possible_starts = [np.argwhere(inpt_array == i) for i in ["^", ">", "<", "v"]]
    for i in possible_starts:
        if i.size != 0:
            start = i[0]
            break

    current_pos = start
    visited_pos = np.zeros(inpt_array.shape)
    print(f"Start is {current_pos}")

    while True:
        try:
            if not is_inbound(inpt_array, current_pos):
                break
            new_pos = (new_move := moves[str(inpt_array[*current_pos])]) + current_pos
            new_move_sign = puzzle[*current_pos]
            if inpt_array[*new_pos] == "#":
                new_pos = (
                    new_move := moves[rotate[str(inpt_array[*current_pos])]]
                ) + current_pos
                new_move_sign = rotate[new_move_sign]
            inpt_array[*current_pos] = "."
            inpt_array[*new_pos] = new_move_sign

            visited_pos[*current_pos] = 1
            current_pos = new_pos
        except IndexError:
            break

    return visited_pos


print(sum(solve_puzzle(puzzle).ravel()))
