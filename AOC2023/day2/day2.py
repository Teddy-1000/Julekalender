import numpy as np


with open("input", "r") as file:
    inpt = file.read().splitlines()

# r g b
# 0 1 2


def map_rgb(string):
    string = string.replace("red", "0")
    string = string.replace("green", "1")
    string = string.replace("blue", "2")
    return string


def parse_games(game):
    game_nr, draws = game.split(":")
    draws = list(map(lambda x: x.split(","), draws.split(";")))
    rn = np.zeros([len(draws), 3])
    for i, j in enumerate(draws):
        for k in j:
            k = k[1:].split(" ")
            rn[i][int(k[-1])] = int(k[0])
    return int(game_nr.split(" ")[-1]), rn


games = np.empty(len(inpt)+1, dtype=np.ndarray)
inpt = list(map(map_rgb, inpt))

for i in inpt:
    indx, game = parse_games(i)
    games[indx] = game

games[0] = np.array([0, 0, 0])
true_cubes = [12, 13, 14]

is_possible = list(map(lambda x: np.less_equal(x, true_cubes), games))
print("Part One: ", sum(sum(np.where(list(map(lambda x: np.all(x), is_possible))))))
print("Part two: ", int(sum(map(lambda x: np.prod(np.max(x, axis=0)), games))))
