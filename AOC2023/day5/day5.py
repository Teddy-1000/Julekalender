from itertools import groupby
from multiprocessing import Pool, cpu_count


with open("input", "r") as file:
    data = file.read().splitlines()

sub_data = [list(g) for k, g in groupby(data, key=lambda x: x == '') if not k]

data = {}

# print(sub_data[1])

for i in sub_data:
    if len(i) == 1:
        i = i[0].split(":")
        data[i[0]] = list(map(lambda x: int(x), i[1].split()))
    else:
        data[i[0]] = list(map(lambda x:
                              list(map(lambda y: int(y), x.split())), i[1:])
                          )


seeds = data.pop("seeds")
seed_map = {}

for i in data:
    seed_map[i] = [[], []]
    for range_set in data[i]:
        seed_map[i][0].append((range_set[1], range_set[1]+range_set[2]+1))
        seed_map[i][1].append((range_set[0], range_set[0]+range_set[2]+1))

min_location = 10**10

# print(seed_map["seed-to-soil map:"])


def find_seed_location(seed):
    next_key = seed
    # print(f"Starting seed {seed}")
    for i in seed_map:
        source, dest = seed_map[i]
        for j, k in zip(source, dest):
            if j[0] <= next_key <= j[1]:
                next_key = k[0] + (next_key - j[0])
                break
        # print(f"\tCompleted {i}")
    return seed, next_key


with Pool(processes=len(seeds)) as pool:
    results = (pool.map(find_seed_location, seeds))
results = sorted(results, key=lambda x: x[1])
print(f"Part One: \n\tSeed {results[0][0]} has the lowest position at {results[0][1]}")


def part_two(seeds):
    min_loc = [0, 10*100]
    for i in range(seeds[0], seeds[0]+seeds[1]):
        tmp = find_seed_location(i)
        if tmp[1] < min_loc[1]:
            min_loc = tmp
    print(f"Completed seed range {seeds}")
    return min_loc


def part_two_list(seeds):
    min_loc = [0, 10*100]
    print(seeds)
    for i in seeds:
        tmp = find_seed_location(i)
        if tmp[1] < min_loc[1]:
            min_loc = tmp
    print(f"Completed seed range {seeds}")
    return min_loc


pair_seed = list(zip(seeds[::2], seeds[1::2]))

# with Pool(processes=len(pair_seed)) as pool:
#     results = pool.map(part_two, pair_seed)

with Pool(processes=cpu_count()) as pool:
    inter_results = []
    for i in pair_seed:
        iter_range = range(i[0], i[0]+i[1])
        inter_results.append(pool.map(part_two_list, iter_range,
                             chunksize=len(iter_range)/cpu_count()))

print(inter_results)

# results = sorted(results, key=lambda x: x[1])
# print(f"Part Two: \n\tSeed {results[0][0]} has the lowest position at {results[0][1]}")
