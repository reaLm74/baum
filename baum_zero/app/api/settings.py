import os

from dotenv import load_dotenv

load_dotenv()

driver = os.getenv('ZERO_DRIVER')
user = os.getenv('ZERO_USER')
password = os.getenv('ZERO_PASSWORD')
host = os.getenv('ZERO_HOST')
port = os.getenv('ZERO_PORT')
db_name = os.getenv('ZERO_DB_NAME')

DATABASE_URL = f"{driver}://{user}:{password}@{host}:{port}/{db_name}"
