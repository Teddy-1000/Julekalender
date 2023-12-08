

with open("input", "r") as file:
    inpt = file.read().splitlines()


def part_one(inpt):
    tot_score = 0
    for line in inpt:
        card_score = 0
        card, game = line.strip().split(":")
        draws, winning = list(map(lambda x: x.split(), game.split("|")))
        for i in draws:
            if i in winning:
                card_score += 1
        if card_score > 0:
            tot_score += 2**(card_score-1)
    return tot_score


def part_two(inpt):
    tot_scratch_card = 0
    game_board = {}
    org_cards = {}
    for line in inpt:
        card, game = line.strip().split(":")
        card = card.split()[-1]
        game_board[int(card)] = 1
        org_cards[int(card)] = game
        tot_scratch_card += 1

    # Generate all cards
    for cards in game_board:
        for card in range(game_board[cards]):
            card_score = 0
            draws, winning = list(map(lambda x: x.split(), org_cards[cards].split("|")))
            for i in draws:
                if i in winning:
                    card_score += 1
            for i in range(cards+1, cards+card_score+1):
                game_board[i] += 1

    print(game_board[10])

    return sum(list(map(lambda x: x[1], game_board.items())))


print("Part one ", part_one(inpt))
print("Part two ", part_two(inpt))
