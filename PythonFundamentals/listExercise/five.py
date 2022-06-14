deck = input().split(' ')
number_of_shuffles = int(input())
old_deck = deck.copy()
new_deck = list()

for shuf in range(number_of_shuffles):
    cards = len(deck)
    new_deck.insert(0, deck[0])
 #    deck.pop(0)
    new_deck.insert(1, deck[cards - 1])
#     deck.pop()

    for card in range(1, cards - 1):
        if card % 2 == 0:
            new_deck.insert(card,old_deck[card - 1])
        else:
            new_deck.insert(card,old_deck[card + 1])
    old_deck.clear()
    old_deck = new_deck.copy()
    new_deck.clear()

print(old_deck)



