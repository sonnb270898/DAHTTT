import scrapy
from FilmCrawler.items import FilmcrawlerItem


class FilmCrawler(scrapy.Spider):
    name = 'filmCrawler'
    start_urls = ['http://www.phimmoi.net/phim-le/', 'http://www.phimmoi.net/phim-bo/']

    def parse(self, response):
        film_list = response.xpath('//ul[@class="list-movie"]/li')
        for film in film_list:
            href = film.xpath('.//a/@href').get()
            yield response.follow(href, callback=self.parse_film)

        next_page = response.xpath('//ul[@class="pagination pagination-lg"]//a/@href').getall()[-1]
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_film(self, response):
        items = FilmcrawlerItem()
        items['vname'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//span[@class="title-1"]//text()').get()
        items['ename'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//span[@class="title-2"]/text()').get()
        items['director'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//a[@class="director"]/text()').getall()
        items['country'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//a[@class="country"]/text()').getall()
        items['content'] = response.xpath('//div[@id="film-content"]//text()').get()
        items['tag'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//a[@class="category"]/text()').getall()
        items['url'] = response.xpath(
            '//div[@class="block-movie-info movie-info-box"]//a[@class="title-1"]/@href').get()
        yield items
