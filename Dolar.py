import requests
from bs4 import BeautifulSoup
import time

while True:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    page = requests.get("https://www.google.com/search?q=dolar", headers=headers)
    # print(page.content) -> Mostra se está puxando a pag toda

    soup = BeautifulSoup(page.content, 'html.parser')

    atributos = {'class': 'g'}
    valor_dolar = soup.find_all("span", class_="DFlfde SwHCTb")[0]

    valor_dolar['data-value']

    dolar = float(valor_dolar['data-value']) * 1.10

    print('Valor Dólar com IOF:', dolar)

    #print(valor_dolar['data-value'])
    #print(valor_dolar.text)
    time.sleep(30)  # 30 segundos