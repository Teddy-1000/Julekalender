

with open("input", "r") as file:
    path = file.readline().strip()
    file.readline()
    network = {}
    for line in file:
        line = line.split("=")
        network[line[0].strip()] = [i.strip(" ()\n") for i in line[1].split(",")]


pos = network["AAA"]
steps = 0
len_path = len(path)
while True:
    direction = path[steps % len_path]
    steps += 1
    match direction:
        case "L":
            if pos[0] == "ZZZ":
                break
            pos = network[pos[0]]
        case "R":
            if pos[1] == "ZZZ":
                break
            pos = network[pos[1]]


def test_if_end(current_pos):
    tmp = list(map(lambda x: x.endswith("Z"), current_pos))
    return all(tmp)


pos = [network[i] for i in network if i.endswith("A")]
print(f"Starting on ", [i for i in network if i.endswith("A")])
pos2 = []
steps = 0
len_path = len(path)
while True:
    direction = path[steps % len_path]
    steps += 1
    match direction:
        case "L":
            for i in pos:
                pos2.append(i[0])
        case "R":
            for i in pos:
                pos2.append(i[1])
    if test_if_end(pos2):
        break
    pos = [network[i] for i in pos2]
    pos2 = []


print(f"Part one: Number of steps {steps}")
