import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("env/.env")

# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")

print(f"Using database: {database}")
