import json
import re
import unicodedata


def letters_to_ascii(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn')


with open("cardbase_crypt.json", "r") as crypt_file, open("cardbase_crypt_playtest.json", "r") as crypt_playtest_file:
    crypt_db = json.load(crypt_file)
    crypt = list(crypt_db.values())

with open("cardbase_lib.json", "r") as library_file, open("cardbase_lib_playtest.json", "r") as library_playtest_file:
    library_db = json.load(library_file)
    library = list(library_db.values())

def get_by_name(cardname):
    cards = []
    cardname = cardname.lower()
    for card in crypt:
        if cardname in card['name'].lower() or cardname in letters_to_ascii(
                card['name'].lower()):
            name = card['name']
            cardimagename = letters_to_ascii(re.sub('[\\W]', '', card['name'].lower())) + f"g{card['group']}"
            if card['new']:
                name += f" (G{card['group']})"

            if card['adv'] and card['adv'][0]:
                cardimagename += 'adv'
                name += ' (ADV)'

            cards.append([name, cardimagename])

    for card in library:
        if cardname in card['name'].lower() or cardname in letters_to_ascii(
                card['name'].lower()):
            cardimagename = letters_to_ascii(
                    re.sub('[\\W]', '', card['name'].lower()))
            cards.append([card['name'], cardimagename])

    return cards
