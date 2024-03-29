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
        if cardname in card['Name'].lower() or cardname in letters_to_ascii(
                card['Name'].lower()):
            name = card['Name']
            cardimagename = letters_to_ascii(re.sub('[\\W]', '', card['Name'].lower())) + f"g{card['Group']}"
            if card['New']:
                name += f" (G{card['Group']})"

            if card['Adv'] and card['Adv'][0]:
                cardimagename += 'adv'
                name += ' (ADV)'

            cards.append([name, cardimagename])

    for card in library:
        if cardname in card['Name'].lower() or cardname in letters_to_ascii(
                card['Name'].lower()):
            cardimagename = letters_to_ascii(
                    re.sub('[\\W]', '', card['Name'].lower()))
            cards.append([card['Name'], cardimagename])

    return cards
