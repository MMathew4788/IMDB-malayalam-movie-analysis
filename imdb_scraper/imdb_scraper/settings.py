import os
from dotenv import load_dotenv

# Set a custom User-Agent to mimic a browser request
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

# Scrapy settings
BOT_NAME = 'imdb_scraper'

SPIDER_MODULES = ['imdb_scraper.spiders']
NEWSPIDER_MODULE = 'imdb_scraper.spiders'

# Configure item pipelines
ITEM_PIPELINES = {
    'imdb_scraper.pipelines.ImdbScraperPipeline': 1,
}

# Rate limit settings
DOWNLOAD_DELAY = 2  # Delay in seconds
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# MySQL connection settings
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

# Bypass robot.txt rules
ROBOTSTXT_OBEY = True

# Set additional headers to avoid detection
DEFAULT_REQUEST_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.imdb.com',
}
