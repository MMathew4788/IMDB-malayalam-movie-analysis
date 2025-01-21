# IMDb Scraper

This Scrapy project scrapes IMDb's top movies and stores the data in a MySQL database.

## Setup

1. Create a virtual environment and activate it:
    ```sh
    python -m venv scrapy_env
    source scrapy_env/bin/activate
    ```

2. Install the required packages:
    ```sh
    pip install scrapy mysql-connector-python python-dotenv
    ```

3. Set up your MySQL database using the `create_database.sql` script.

4. Create a `.env` file in the root directory with your MySQL credentials:
    ```ini
    MYSQL_HOST=your_mysql_host
    MYSQL_USER=your_mysql_user
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_DATABASE=your_mysql_database
    ```

5. Run the spider:
    ```sh
    scrapy crawl imdb_spider
    ```

## Files

- `items.py`: Defines the data structure.
- `pipelines.py`: Handles data storage in MySQL.
- `settings.py`: Configures Scrapy settings.
- `.env`: Stores environment variables.
- `.gitignore`: Specifies files to ignore in version control.
- `create_database.sql`: SQL script to set up the database.
- `README.md`: Project documentation.
