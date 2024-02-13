import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch_title(url, session):
    try:
        # Realiza la solicitud GET de forma asincrónica.
        async with session.get(url) as response:
            # Espera y recoge el texto de la respuesta.
            html = await response.text()

            # Usa BeautifulSoup para parsear el HTML.
            soup = BeautifulSoup(html, 'html.parser')
            return soup.title.string  # Retorna el título de la página.
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


async def main(urls):
    async with aiohttp.ClientSession() as session:  # Crea una sesión asincrónica.
        # Prepara las tareas asincrónicas.
        tasks = [fetch_title(url, session) for url in urls]
        # Ejecuta las tareas de forma concurrente.
        titles = await asyncio.gather(*tasks)
        for title in titles:
            print(title)  # Imprime los títulos recogidos.

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://en.wikipedia.org/wiki/Main_Page"
    ]

    asyncio.run(main(urls))
