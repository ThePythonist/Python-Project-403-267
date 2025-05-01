import requests
from bs4 import BeautifulSoup

symbols = {
    "قیمت دلار": "https://www.tgju.org/profile/price_dollar_rl",
    "سکه امامی": "https://www.tgju.org/profile/sekee",
    "سکه بهار آزادی": "https://www.tgju.org/profile/sekeb",
    "نیم سکه": "https://www.tgju.org/profile/nim",
    "ربع سکه": "https://www.tgju.org/profile/rob",
    "قیمت طلا": "https://www.tgju.org/profile/geram18",
}


def fetch(symbol):
    try:

        if symbol not in symbols:
            return {"error": "URL NOT FOUND"}

        URL = symbols[symbol]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        spans = soup.find_all("span", class_="value")
        span_value = str(spans[0]).split()[3]
        # price = span_value[-14:-7]
        price = span_value.split(">")[1].split("<")[0]
        return {"result": price}

    except Exception as error:
        return {"error": str(error)}
