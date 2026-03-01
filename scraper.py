import requests as rq
from bs4 import BeautifulSoup as bs
import re

# url = "https://www.anmyperfumes.com.br/stronger-with-you-intensely-eau-de-parfum-feminino-giorgio-armani"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def extract_with_regex(pattern, text, cast=str):
    match = re.search(pattern, text)
    if not match:
        return None
    return cast(match.group(1))

def get_product_data(url):
    response = rq.get(url, headers=HEADERS)

    html = response.text

    price = extract_with_regex(r"var produto_preco = ([\d\.]+);", html, float)

    name_match = re.search(r"<title>(.*?)</title>", html)
    name = name_match.group(1).strip() if name_match else None

    return {
        "name": name,
        "price": price,
        "url": url
    }