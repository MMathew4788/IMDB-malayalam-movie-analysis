import scrapy
from imdb_scraper.items import MovieItem

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        movies = response.css('td.titleColumn')
        for movie in movies:
            item = MovieItem()
            item['title'] = movie.css('a::text').get()
            item['year'] = movie.css('span.secondaryInfo::text').get().strip('()')
            item['rating'] = movie.xpath('following-sibling::td/strong/text()').get()
            movie_url = movie.css('a::attr(href)').get()
            yield response.follow(movie_url, self.parse_movie, meta={'item': item})

    def parse_movie(self, response):
        item = response.meta['item']
        item['director'] = response.css('div.credit_summary_item a::text').get()
        item['genres'] = response.css('div.subtext a[href*="/search/title?genres="]::text').getall()
        item['duration'] = response.css('time::text').get().strip()
        item['votes'] = response.css('span[itemprop="ratingCount"]::text').get()
        item['metascore'] = response.css('div.metascore span::text').get()
        item['description'] = response.css('div.summary_text::text').get().strip()
        yield item
