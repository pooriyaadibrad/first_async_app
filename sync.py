import requests
from bs4 import BeautifulSoup


def get_html(course_id: int):
    url = f'https://toplearn.com/c/{course_id}/'
    response = requests.get(url)
    return response.text

def get_title(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('.right-side h1')
    if title is None:
        return 'there is no course'
    return title.text

for i in range(6000,6050):
    html_top = get_html(i)
    title_course = get_title(html_top)
    print(title_course)