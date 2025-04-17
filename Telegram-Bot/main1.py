import telepot
import time
import urllib3
from mytoken import mytoken
from pprint import pprint

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot(mytoken)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg)

    if content_type == 'text':
        if msg['text'] == "/start":
            bot.sendMessage(chat_id, "Hello {} welcome to our bot!".format(msg['from']['first_name']))
        else:
            bot.sendMessage(chat_id, "You said {}".format(msg['text']))
    else:
        bot.sendMessage(chat_id, "I dont understand that type of message")


bot.message_loop(handle)

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
