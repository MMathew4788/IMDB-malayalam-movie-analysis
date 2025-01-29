import scrapy
from imdb_scraper.items import ImdbScraperItem
from datetime import datetime, timedelta

class ImdbMalayalamSpider(scrapy.Spider):
    name = 'imdb_spider'

    def start_requests(self):
        # Define the start date and end date
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2024, 12, 31)

        # Generate URLs for each 10-day period
        current_date = start_date
        while current_date < end_date:
            next_date = current_date + timedelta(days=2)
            url = f'https://m.imdb.com/search/title/?release_date={current_date.strftime("%Y-%m-%d")},{next_date.strftime("%Y-%m-%d")}&primary_language=ml'
            yield scrapy.Request(url=url, callback=self.parse)
            current_date = next_date

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
            item['title'] = title.strip() if title else None
            if not title:
                self.log("Title not found")

            # Extract the year and duration from the metadata
            spans = metadata.css('span::text').getall()
            item['year'] = spans[0].strip() if len(spans) > 0 else None
            item['duration'] = spans[1].strip() if len(spans) > 1 else None
            
            if not item['year'] or not item['duration']:
                self.log("Year or duration not found")

            # Extract rating
            rating = ratingGroup.css('.ipc-rating-star--rating::text').get()
            item['rating'] = rating.strip() if rating else None
            if not rating:
                self.log("Rating not found")

            # Extract vote count
            votes = ratingGroup.xpath('.//span[@class="ipc-rating-star--voteCount"]/text()').getall()
            item['votes'] = ''.join([vote.strip() for vote in votes if vote.strip()]) if votes else None
            
            if not item['votes']:
                self.log("Votes not found")

            # Yield the item
            yield item
