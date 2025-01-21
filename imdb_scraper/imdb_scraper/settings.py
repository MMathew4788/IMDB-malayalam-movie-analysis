# Scrapy settings for imdb_scraper project
BOT_NAME = 'imdb_scraper'

SPIDER_MODULES = ['imdb_scraper.spiders']
NEWSPIDER_MODULE = 'imdb_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 2

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Pipelines
ITEM_PIPELINES = {
    'imdb_scraper.pipelines.MySQLPipeline': 300,
}

