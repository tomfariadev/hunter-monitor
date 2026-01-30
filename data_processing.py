import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def execute_scraping(term: str, places: list) -> pd.DataFrame:
    df = []
    
    # rodar em segundo plano
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    
    # Mercado livre
    if "Mercado Livre" in places:
        url = f"https://lista.mercadolivre.com.br/{term.replace(" ", "-")}"
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # busca do item
        items = soup.find_all("div", {"class": "ui-search-result__wrapper"})
        for i in items:            
            title = i.find("h2") or i.find("h3")
            price = i.select_one(".andes-money-amount__fraction")
            link = i.find("a", href=True)

            if title and price:
                df.append({
                    "produto": title.text,
                    "preco": price.text,
                    "link": link['href'] if link else "",
                    "fonte": "Mercado Livre"
                })

    driver.quit()

    return pd.DataFrame(df)