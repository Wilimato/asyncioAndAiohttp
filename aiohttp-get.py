import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://httpbin.org/get')
        print(html)

# Python 3.7+
if __name__ == '__main__':
    asyncio.run(main())
