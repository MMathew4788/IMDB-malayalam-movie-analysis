# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    director = scrapy.Field()
    genres = scrapy.Field()
    duration = scrapy.Field()
    votes = scrapy.Field()
    metascore = scrapy.Field()
    description = scrapy.Field()

