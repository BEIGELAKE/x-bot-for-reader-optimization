import tweepy
from config.config import config  # Ensure correct import path
from utils.logger import log_error

# Twitter API authentication (replace with your appropriate authentication setup)
auth = tweepy.OAuth1UserHandler(
    config.twitter_api_key,
    config.twitter_api_secret,
    config.twitter_access_token,
    config.twitter_access_secret
)

api = tweepy.API(auth)


def fetch_trending_topics():
    try:
        trends = api.trends_place(1)  # 1 for global trends
        trending_topics = [trend['name'] for trend in trends[0]['trends']]
        return trending_topics
    except tweepy.TweepError as e:
        log_error(f"Error fetching trending topics: {e}")
