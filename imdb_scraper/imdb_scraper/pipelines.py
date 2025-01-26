import mysql.connector
from mysql.connector import Error
import os
from scrapy.exceptions import NotConfigured
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

class ImdbScraperPipeline:

    def open_spider(self, spider):
        try:
            self.connection = mysql.connector.connect(
                host= os.getenv('MYSQL_HOST'),
                database= os.getenv('MYSQL_DATABASE'),
                user= os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
            )
            self.cursor = self.connection.cursor()
            spider.logger.info("MySQL connection established")

        except Error as e:
            spider.logger.error(f"Error connecting to MySQL: {e}")
            raise NotConfigured("MySQL connection failed")

    def close_spider(self, spider):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            spider.logger.info("MYSQL connection closed")

    def process_item(self, item, spider):
        if not self.connection or not self.connection.is_connected():
            spider.logger.error("No active MySQL connection, skipping item")
            return item
        
        try:
            self.cursor.execute("""
                INSERT INTO movies (title, year, rating, duration, votes)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                item.get('title'), 
                item.get('year'), 
                item.get('rating'), 
                item.get('duration'), 
                item.get('votes')))
            self.connection.commit()
            spider.logger.info(f"Inserted item into database: {item['title']}")
        except Error as e:
            spider.logger.error(f"Error inserting data: {e}")
        return item
