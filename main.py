import telegram
import logging
from telegram.ext import Updater,CommandHandler
from urllib3.exceptions import ProtocolError
import os
import tweet_scrape as ts
from dotenv import load_dotenv
import time

load_dotenv("keys.env")
API_TOKEN = str(os.getenv("TELEGRAM_BOT"))

def startbot():
    twitter_stream = ts.TweetBot()
    twitter_stream.fetch_tweets()


PORT = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    updater = Updater(token=API_TOKEN,use_context=True)
    dispatcher = updater.dispatcher
    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=API_TOKEN)
    updater.bot.setWebhook('https://twitter-tg-bot-server.herokuapp.com/' + API_TOKEN)
    updater.idle()
    while True:
        try:
            startbot()
            time.sleep(5)
        except ProtocolError:
            continue



# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.

