import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLPipeline:

    def open_spider(self, spider):
        host = os.getenv('MYSQL_HOST')
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')
        database = os.getenv('MYSQL_DATABASE')

        if not all([host, user, password, database]):
            spider.logger.error("Missing environment variables for MySQL connection.")
            return

        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            if self.connection.is_connected():
                spider.logger.info("Connected to MySQL database")
        except Error as e:
            spider.logger.error(f"Error connecting to MySQL: {e}")

    def close_spider(self, spider):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(""" 
                INSERT INTO movies (title, year, rating, director, genres, duration, votes, metascore, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                item['title'],
                item['year'],
                item['rating'],
                item['director'],
                ','.join(item['genres']),
                item['duration'],
                item['votes'],
                item['metascore'],
                item['description']
            ))
            self.connection.commit()
        except Error as e:
            spider.logger.error(f"Error inserting item into MySQL: {e}")
        return item
