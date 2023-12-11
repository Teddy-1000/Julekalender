

with open("input", "r") as file:
    time = list(map(lambda x: int(x), file.readline().strip().split(":")[1].split()))
    dist = list(map(lambda x: int(x), file.readline().strip().split(":")[1].split()))


winning_runs = 1


def get_number_of_winning_races(race_time, race_dist):
    record_breaks = 0
    for j in range(1, race_time):
        race_distance = (race_time-j)*j
        if race_distance > race_dist:
            record_breaks += 1

    return record_breaks


for i, race_time in enumerate(time):
    record_breaks = get_number_of_winning_races(race_time, dist[i])
    winning_runs *= record_breaks

print(f"Number of winning runs multiplied {winning_runs}")

time = int("".join([str(i) for i in time]))
dist = int("".join([str(i) for i in dist]))


winning_runs = get_number_of_winning_races(time, dist)


print(f"Number of winning runs in long race {winning_runs}")
