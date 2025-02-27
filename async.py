import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_html(course_id):
    url = f'https://toplearn.com/c/{course_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select_one('.right-side h1')
    if title is None:
        return 'there is no course'
    return title.text


async def get_courses():
    tasks = []
    for course_id in range(6130, 6141):
        tasks.append(asyncio.create_task(get_html(course_id)))

    for item in tasks:
        html = await item
        title = parse_html(html)
        print(title)


def main():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(get_courses())


if __name__ == '__main__':
    main()
