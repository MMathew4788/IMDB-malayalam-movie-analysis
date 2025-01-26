import scrapy
from imdb_scraper.items import ImdbScraperItem

class ImdbMalayalamSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://m.imdb.com/search/title/?primary_language=ml']

    def parse(self, response):
        # Iterate over each movie block
        for movie, metadata, ratingGroup in zip(
            response.css('.ipc-title-link-wrapper'),
            response.css('.dli-title-metadata'),
            response.css('.ratingGroup--imdb-rating')
        ):
            # Create a new item instance for each movie
            item = ImdbScraperItem()

            # Extract title
            title = movie.css('h3::text').get()
            if title:
                item['title'] = title.strip()
            else:
                item['title'] = None
                self.log("Title not found")

            # Extract the year and duration from the metadata
            spans = metadata.css('span::text').getall()
            if spans:
                item['year'] = spans[0].strip() if len(spans) > 0 else None
                item['duration'] = spans[1].strip() if len(spans) > 1 else None
            else:
                item['year'] = None
                item['duration'] = None
                self.log("Year or duration not found")

            # Extract rating
            rating = ratingGroup.css('.ipc-rating-star--rating::text').get()
            if rating:
                item['rating'] = rating.strip()
            else:
                item['rating'] = None
                self.log("Rating not found")

            # Extract vote count and clean the unwanted HTML
           # Extract vote count (including comments within the span tag)
            votes = ratingGroup.xpath('.//span[@class="ipc-rating-star--voteCount"]/text()').getall()

            if votes:
            # Clean up unwanted whitespaces and extract meaningful text
                item['votes'] = ''.join([vote.strip() for vote in votes if vote.strip()])
            else:
                item['votes'] = None
            self.log("Votes not found")

            # Yield the item
            yield item
