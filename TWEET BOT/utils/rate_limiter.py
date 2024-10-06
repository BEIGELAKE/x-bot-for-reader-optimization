import time
from config.config import config


class RateLimiter:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit  # Max requests per period
        self.period = 15 * 60  # Twitter's window period (15 minutes in seconds)
        self.requests = 0
        self.start_time = time.time()

    def check_limit(self):
        current_time = time.time()
        if current_time - self.start_time > self.period:
            # Reset the counter after the period has passed
            self.requests = 0
            self.start_time = current_time
        elif self.requests >= self.rate_limit:
            # If limit reached, wait until the period resets
            time_left = self.period - (current_time - self.start_time)
            time.sleep(time_left)
            self.requests = 0
            self.start_time = time.time()

    def increment(self):
        self.requests += 1


# Usage
rate_limiter = RateLimiter(rate_limit=config.twitter_rate_limit)
