import aiohttp
import asyncio
import json


async def post2(session, url, data):
    async with session.post(url, json=data) as response:
        return await response.text()


async def post(session, url, data):
    async with session.post(url, json=data) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        data = {'key': 'value'}
        response = await post(session, 'http://httpbin.org/post', data)
        response2 = await post2(session, 'http://httpbin.org/post', data)
        print(response)
        print(response2)

if __name__ == '__main__':
    asyncio.run(main())
