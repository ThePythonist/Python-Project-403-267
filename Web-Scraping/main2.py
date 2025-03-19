import requests
from bs4 import BeautifulSoup

symbols = {
    "dollar": "https://www.tgju.org/profile/price_dollar_rl",
    "imami": "https://www.tgju.org/profile/sekee",
    "nim": "https://www.tgju.org/profile/nim",
    "rob": "https://www.tgju.org/profile/rob",
    "tala18": "https://www.tgju.org/profile/geram18",
}


def fetch(symbol):
    URL = symbols[symbol]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    spans = soup.find_all("span", class_="value")
    span_value = str(spans[0]).split()[3]
    # price = span_value[-14:-7]
    price = span_value.split(">")[1].split("<")[0]
    print(price)


fetch("rob")
