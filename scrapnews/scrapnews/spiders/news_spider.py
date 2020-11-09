import scrapy
from pygooglenews import GoogleNews


class NewsSpider(scrapy.Spider):
    name = 'news'
    # Получение списка ссылок на новости при помощи модуля GoogleNews
    gn = GoogleNews(lang='en', country='US')
    s = gn.search('Russia', from_='2020-10-08', to_='2020-11-08')
    links = []
    for x in range(0, 100):
        links.append(s['entries'][x]['link'])

    start_urls = links

    def parse(self, response):
        with open('News.txt', 'a') as file:
            file.write(str(response.css('p::text').getall()))
