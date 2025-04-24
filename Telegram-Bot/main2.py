from flask import Flask, request
import telepot
import urllib3
from mytoken import mytoken

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "bot"
bot = telepot.Bot(mytoken)
bot.setWebhook("https://thepythonist3.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == "/start":
            bot.sendMessage(chat_id, "Hello {} welcome to our bot!".format(msg['from']['first_name']))
        else:
            bot.sendMessage(chat_id, "You said {}".format(msg['text']))
    else:
        bot.sendMessage(chat_id, "I dont understand that type of message")

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update["message"])
    return "OK"