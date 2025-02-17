from collections import Counter

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

cards_hex = ['E', 'D', 'C', 'B', 'A', '9', '8', '7', '6', '5', '4', '3', '2']

with open("input", "r") as file:
    hands = {}
    for line in file:
        line = line.split()
        line = list(map(lambda x: x.strip(), line))
        for i, j in zip(cards, cards_hex):
            if i in line[0]:
                line[0] = line[0].replace(i, j)
        hands[line[0]] = line[1]


all_hands = list(hands.keys())


counted_hands = list(map(lambda x: Counter(x), all_hands))

# print(counted_hands)


sorted_hands = [i for _, i in sorted(zip(counted_hands, hands), key=lambda x: tuple(
    sorted(list(x[0].values()), reverse=True)
    + sorted(list(map(lambda y: ord(y), x[0].keys())), reverse=False)),
    reverse=False)]


total_winnings = 0
print(sorted_hands)

for i, j in enumerate(sorted_hands):
    tmp = (i+1)*int(hands[j])
    total_winnings += tmp
    # print(i+1, hands[j], tmp, total_winnings)


print(total_winnings)
