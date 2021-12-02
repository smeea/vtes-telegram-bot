import json
import re
import unicodedata


def letters_to_ascii(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')


with open("vtescrypt.json", "r") as crypt_file:
    crypt = json.load(crypt_file)

with open("vteslib.json", "r") as library_file:
    library = json.load(library_file)


def get_by_name(cardname):
    cards = []
    cardname = cardname.lower()
    for card in crypt:
        if cardname in card['Name'].lower() or cardname in letters_to_ascii(
                card['Name'].lower()):
            name = card['Name']
            cardimagename = letters_to_ascii(re.sub('[\\W]', '', card['Name'].lower()))
            if card['New']:
                cardimagename += f"g{card['Group']}"
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
