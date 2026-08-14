import os
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print(api_key)
print(db_url)