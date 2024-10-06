import tweepy
from config.config import config
from src.summarizer import summarize_text
from src.language_support import detect_language, translate_text
from src.trends import fetch_trending_topics
from src.thread_summarizer import summarize_thread
from src.fact_check import fact_check
from utils.logger import log_info, log_error
from utils.rate_limiter import rate_limiter

# Twitter API authentication
auth = tweepy.OAuth1UserHandler(
    config.twitter_api_key,
    config.twitter_api_secret,
    config.twitter_access_token,
    config.twitter_access_secret
)

api = tweepy.API(auth)


def handle_mentions():
    try:
        mentions = api.mentions_timeline(count=5)  # Fetch last 5 mentions
        for mention in mentions:
            rate_limiter.check_limit()
            tweet_text = mention.text
            user = mention.user.screen_name

            log_info(f'Received mention from {user}: {tweet_text}')

            # Summarization request
            if 'summarize' in tweet_text.lower():
                summary = summarize_text(tweet_text)
                api.update_status(f'@{user} Here’s your summary: {summary}', in_reply_to_status_id=mention.id)

            # Translation request
            elif 'translate' in tweet_text.lower():
                lang = detect_language(tweet_text)
                translated = translate_text(tweet_text, target_lang='en')
                api.update_status(f'@{user} Translation: {translated}', in_reply_to_status_id=mention.id)

            # Thread summarization request
            elif 'thread' in tweet_text.lower():
                thread_summary = summarize_thread(mention.id)
                api.update_status(f'@{user} Thread summary: {thread_summary}', in_reply_to_status_id=mention.id)

            # Trending topics request
            elif 'trending' in tweet_text.lower():
                trends = fetch_trending_topics()
                api.update_status(f'@{user} Current trending topics: {", ".join(trends)}',
                                  in_reply_to_status_id=mention.id)

            # Fact-check request
            elif 'fact check' in tweet_text.lower():
                fact_result = fact_check(tweet_text)
                api.update_status(f'@{user} Fact-check result: {fact_result}', in_reply_to_status_id=mention.id)

            # Increment API request count
            rate_limiter.increment()

    except tweepy.TooManyRequests as e:
        log_error(f"Too many requests: {e}")
    except tweepy.Forbidden as e:
        log_error(f"Forbidden error: {e}")
    except tweepy.NotFound as e:
        log_error(f"Not found error: {e}")
    except Exception as e:
        log_error(f"General error: {e}")


# Run the bot
if __name__ == '__main__':
    handle_mentions()
