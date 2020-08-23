#! /usr/bin/python3

import telegram
import logging


TOKEN = "TOKEN123"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -  %(message)s', level=logging.INFO)
logger = logging.getLogger('Bot')

def main():
    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me())
    #bot.send_message(chat_id=chat_id, text="Test.")
    updates = bot.get_updates()
    print([u.message.text for u in updates])
    chat_id = bot.get_updates()[-1].message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text="Test.")

if __name__ == '__main__':
    main()
