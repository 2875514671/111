# -*- coding: utf-8 -*-


import urllib.request
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/70.0.3538.110 Safari/537.36"}


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_html(soup):
    movies_lists_soup = soup.find('ol', attrs={"class": "grid_view"})
    movies_list_soup = movies_lists_soup.find_all('li')
    for movies_soup in movies_list_soup:
        movie_name = movies_soup.find('span', attrs={"class": 'title'}).text
        movie_star = movies_soup.find('p').text
        print(movie_name, end=' ')
        print(movie_star)

        movies_pic = movies_soup.find('img')['src']
        print(movies_pic)
        urllib.request.urlretrieve(
            movies_pic,
            r"E:\Jetbrains\PycharmProjects\Reptile\Reptile\DouBanTop250\picture\\" + movie_name + '.jpg')


def main(page):
    url = "https://movie.douban.com/top250?start=" + str(page * 25) + "&filter="
    html = get_page(url)
    soup = BeautifulSoup(html, 'lxml')
    parse_html(soup)


if __name__ == '__main__':
    for i in range(10):
        main(i)
