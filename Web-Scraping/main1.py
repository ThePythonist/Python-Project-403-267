import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)
