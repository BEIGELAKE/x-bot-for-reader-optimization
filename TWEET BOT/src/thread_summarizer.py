import tweepy
from src.summarizer import summarize_text
from utils.logger import log_error


def fetch_thread(tweet_id):
    try:
        # Fetch the main tweet
        tweet = api.get_status(tweet_id, tweet_mode='extended')
        thread = [tweet.full_text]

        # Get replies in the thread
        replies = tweepy.Cursor(api.search_tweets, q=f'to:{tweet.user.screen_name}', since_id=tweet_id).items()
        for reply in replies:
            if reply.in_reply_to_status_id == tweet_id:
                thread.append(reply.full_text)

        return ' '.join(thread)

    except tweepy.TweepError as e:
        log_error(f"Error fetching thread: {e}")
        return None


def summarize_thread(tweet_id):
    try:
        thread_content = fetch_thread(tweet_id)
        if thread_content:
            return summarize_text(thread_content)
        return "Error summarizing the thread."
    except Exception as e:
        log_error(f"Error in thread summarization: {e}")
        return "Error summarizing the thread."
