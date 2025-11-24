import os
import json

FILENAME = "flashcards.json"

def load_cards():
    if not os.path.exists(FILENAME):
        return []

    try:
        f = open(FILENAME, "r")
        data = json.load(f)
        f.close()

        if type(data) == list:
            return data
        else:
            return []
    except:
        print("Could not load flashcards. Starting with empty list.")
        return []

def save_cards(cards):
    f = open(FILENAME, "w")
    json.dump(cards, f)
    f.close()
