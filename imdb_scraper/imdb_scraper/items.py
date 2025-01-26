import scrapy

class ImdbScraperItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    duration = scrapy.Field()
    votes = scrapy.Field()
