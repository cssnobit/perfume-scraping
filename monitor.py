import json
from scraper import get_product_data
from datetime import datetime

HISTORY_FILE = "files/history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
    
def monitor(urls):
    history = load_history()

    for url in urls:
        try:
            product = get_product_data(url)
        except Exception as e:
            print(f"Erro ao consultar {url}: {e}")
            continue

        last_price = history.get(url, {}).get("last_price")
        product_name = product["name"]
        now_price = product["price"]
        now_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        #print("--------------")
        #print(f'{product["name"]}')
        #print(f'URL: {url}')
        #print(f'Preço atual: {now_price}')

        if last_price:
            print(f"Preço anterior: {last_price}")

            if now_price < last_price:
                diff = last_price - now_price
    
                percent = (diff / last_price) * 100
                print(f"🔥 CORRE QUE O PREÇO CAIU!!! De R${last_price:.2f} para R${now_price:.2f}. {percent:.2f}% de DESCONTO! 🫨")

            elif now_price > last_price:
                diff = now_price - last_price

                percent = (diff / last_price) * 100
                print(f"📈 SUBIDA NOS PREÇOS!!! De R${last_price:.2f} para R${now_price:.2f}. {percent:.2f}% de ACRÉSCIMO! 😫")


        history[url] = {
            "title": product_name,
            "last_price": now_price,
            "date": now_date
        }
        save_history(history)
        print(f"Produto {product_name} salvo com sucesso!")
