import telebot
import time
import re
import os
from dotenv import load_dotenv
from search import get_by_name

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# Get your bot api token from official telegram bot master: @BotFather
API_KEY = os.environ.get("API_KEY") or "mysecretkey1234567890"

bot = telebot.TeleBot(API_KEY)


def show_ruling(rulings, chatid):
    list = []
    for i in rulings:
        list.append(f"- {i['text']}")

    options = "\n".join(list)
    bot.send_message(chatid, options)


def show_card(cardname, chatid):
    imagename = "./cards/" + cardname + ".jpg"
    img = open(imagename, "rb")
    bot.send_photo(chatid, img)


def choose_card(message):
    if (
        message.text.isdigit()
        and int(message.text) <= len(cards)
        and int(message.text) > 0
    ):
        card_id = int(message.text) - 1
        cardname = cards[card_id][1]
        show_card(cardname, message.chat.id)
    else:
        get_card_names(message)


@bot.message_handler()
def get_card_names(message):
    global cards
    if re.match("[!0-9A-Za-z]{3,}", message.text):
        is_rulings = message.text.startswith("!")
        text = message.text.removeprefix("!")

        cards = get_by_name(text)
        print(cards[0][0], cards[0][1])
        if len(cards) == 1:
            cardname = cards[0][1]
            show_card(cardname, message.chat.id)
            if is_rulings:
                show_ruling(cards[0][2], message.chat.id)
        elif len(cards) > 1:
            cardnames = []
            counter = 0
            for i in cards:
                counter += 1
                option = str(counter) + ") " + i[0]
                cardnames.append(option)

            options = "\n".join(cardnames)
            bot.send_message(message.chat.id, options)
            bot.register_next_step_handler(message, choose_card)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)
