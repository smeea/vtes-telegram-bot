import telebot
import time
import re
from search import get_by_name

# Get your bot api token from official telegram bot master: @BotFather
bot = telebot.TeleBot('1255263754:AAHv6DAy1tuyzAVvUPqf4rYIHx3YUPJ1OC4')

def show_card(message):
    imagename = './cards/' + cards[0][1] + '.jpg'
    img = open(imagename, 'rb')
    bot.send_photo(message.chat.id, img)


def choose_card(message):
    if message.text.isdigit() and int(message.text) <= len(cards) and int(
            message.text) > 0:
        card_id = int(message.text) - 1
        imagename = './cards/' + cards[card_id][1] + '.jpg'
        img = open(imagename, 'rb')
        bot.send_photo(message.chat.id, img)
    else:
        get_card_names(message)


@bot.message_handler()
def get_card_names(message):
    global cards
    if re.match('[0-9A-Za-z]+', message.text):
        cards = get_by_name(message.text)
        print(cards)
        if len(cards) == 1:
            show_card(message)
        elif len(cards) > 1:
            cardnames = []
            counter = 0
            for i in cards:
                counter += 1
                option = str(counter) + ') ' + i[0]
                cardnames.append(option)

            options = '\n'.join(cardnames)
            bot.send_message(message.chat.id, options)
            bot.register_next_step_handler(message, choose_card)

# bot.polling()
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)
