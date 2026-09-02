import random



cards = [{"term": "list", "definition": "an ordered, changeable sequence"},{"term": "dict", "definition": "key-value pairs looked up by key"},{"term": "set", "definition": "unordered, no duplicates"},{"term": "tuple", "definition": "a list, but immutable"}]


nocards = False
if not cards:
    print ("No cards in deck")
    nocards = True
else:
    print("There are", len(cards) ,"cards in the deck")
    print(cards[-1]["term"], "->", cards[-1]["definition"])

    card = random.choice(cards)

    print("The term is:", card["term"])
    if input("What is your answer?: ") == card["definition"]:
        print("You got it right")
    else:
        print("You got it wrong, the correct answer was", card["definition"])



