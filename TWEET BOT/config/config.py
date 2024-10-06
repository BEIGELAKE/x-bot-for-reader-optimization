import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        # Twitter API settings
        self.twitter_api_key = os.getenv('TWITTER_API_KEY')
        self.twitter_api_secret = os.getenv('TWITTER_API_SECRET')
        self.twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')

        # Cohere API settings
        self.cohere_api_key = os.getenv('COHERE_API_KEY')

        # Set API rate limits (in requests per 15 minutes)
        self.twitter_rate_limit = int(os.getenv('TWITTER_RATE_LIMIT', 300))  # Defaults to 300 requests/15 min

# Ensure no sensitive data is exposed by storing them securely
config = Config()
