import random



cards = [{"term": "list", "definition": "an ordered, changeable sequence"},
         {"term": "dict", "definition": "key-value pairs looked up by key"},
         {"term": "set", "definition": "unordered, no duplicates"},
         {"term": "tuple", "definition": "a list, but immutable"}]


if not cards:
    print("No cards in deck")
else:
    print("There are", len(cards) ,"cards in the deck")
    score = 0
    cards_reviewed = []
    for card in range(len(cards)):
        shuffled_deck = random.sample(cards, k=len(cards))
        card = random.choice(shuffled_deck)

        while card["term"] in cards_reviewed:
            card = random.choice(shuffled_deck)

        print("The definition is:", card["definition"])
        if input("What is your answer?: ") == card["term"]:
            print("You got it right")
            score += 1
        else:
            print("You got it wrong, the correct answer was", card["term"])

        cards_reviewed.append(card["term"])

    print("Done! You got:", score, "right out of", len(cards))

    
