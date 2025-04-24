from flask import Flask, request
import telepot
import urllib3
from mytoken import mytoken

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "bot"
bot = telepot.Bot(mytoken)
bot.setWebhook("https://thepythonist3.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == "/start":
            keyboard = [
                ['سکه بهار آزادی', 'سکه امامی', 'ربع سکه', 'نیم سکه'],
                ["قیمت طلا", "قیمت دلار", "شاخص بورس تهران", "قیمت بیت کوین"]
            ]
            reply_markup = {'keyboard': keyboard, 'one_time_keyboard': False}
            reply = "Hello {} welcome to the Price Bot!".format(
                msg['from']['first_name'])

            bot.sendMessage(chat_id, reply, reply_markup=reply_markup)
        else:
            reply = "XXXX"
            bot.sendMessage(chat_id, reply)
    else:
        bot.sendMessage(chat_id, "Only text is allowed for translation")


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update["message"])
    return "OK"
