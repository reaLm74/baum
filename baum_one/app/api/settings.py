import os

from dotenv import load_dotenv

load_dotenv()

driver = os.getenv('ONE_DRIVER')
user = os.getenv('ONE_USER')
password = os.getenv('ONE_PASSWORD')
host = os.getenv('ONE_HOST')
port = os.getenv('ONE_PORT')
db_name = os.getenv('ONE_DB_NAME')

DATABASE_URL = f"{driver}://{user}:{password}@{host}:{port}/{db_name}"
