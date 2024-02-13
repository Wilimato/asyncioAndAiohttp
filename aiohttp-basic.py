import aiohttp
import asyncio
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


async def fetch(session, url, page):

    async with session.get(url) as response:

        url_principal = 'https://www.comprasparaguai.com.br'
        respuesta_url = await response.text()
        containerProductos = SoupStrainer(
            "div", attrs={
                "class": "container-flex wrap justify-content-around ct-card-js container-card-produtos-categ-lojas container-card-produtos-categ-lojas-column container-resultados-busca"})
        soup = BeautifulSoup(respuesta_url, 'html.parser',
                             parse_only=containerProductos)
        soup = soup.find_all('div', {"class": "promocao-produtos-item-text"})
        total = 0
        for item in soup:
            total += 1
            imagen = item.find(
                'div', {"class": "promocao-item-img"}).find('img').get('data-src')
            imagen = url_principal + imagen
            print(imagen)
        print(f"total de links: {total}, Número de página: {page}")


async def main(lista):
    async with aiohttp.ClientSession() as session:

        # Modifica el recorrido para incluir el número de página
        recorrido = [fetch(session, lista[i], i+1)
                     for i in range(len(lista))]
        await asyncio.gather(*recorrido)


# Python 3.7+
if __name__ == '__main__':
    urls = [
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=1',
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=2',
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=3',
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=4',
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=5',
        'https://www.comprasparaguai.com.br/busca/?loja=nissei&page=6',
    ]

    asyncio.run(main(urls))
