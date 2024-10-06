# Twitter AI Bot

## Overview

This project is a Twitter bot powered by the **Cohere API** for text summarization and the **Tweepy API** for interacting with Twitter. The bot responds to mentions by performing various actions, such as summarizing text, translating content, summarizing long Twitter threads, providing trending topics, and even fact-checking. 

Built with scalability, security, and error-handling in mind, the bot is future-proof for up to 5 years of usage without needing significant improvements.

## Features

- **Summarization**: Automatically summarizes the text content of tweets.
- **Thread Summarization**: Summarizes long Twitter threads into concise text.
- **Translation**: Detects and translates tweets into a chosen language.
- **Trending Topics**: Provides the latest trending topics from Twitter.
- **Fact-checking**: Verifies the credibility of content by connecting with fact-checking APIs.
- **Secure Token Handling**: Uses encryption for sensitive data like API keys and tokens.
- **Rate Limiting**: Manages API call limits to prevent overuse of Twitter API.
- **Logging**: Detailed logging system for tracking bot activity and error handling.

## File Structure

```bash
twitter_ai_bot/
│
├── config/
│   └── config.py                 # Configuration for API keys, rate limits, and error handling
│
├── src/
│   ├── bot.py                    # Core bot logic with improved error handling, rate limiting
│   ├── summarizer.py             # Summarizes text via Cohere API
│   ├── trends.py                 # Fetches and analyzes trending topics on Twitter
│   ├── fact_check.py             # Fact-checking module
│   ├── language_support.py       # Detects and translates tweets into different languages
│   └── thread_summarizer.py      # Summarizes long Twitter threads
│
├── utils/
│   ├── security.py               # Security utilities like token encryption
│   ├── logger.py                 # Logging for monitoring errors, usage, etc.
│   └── rate_limiter.py           # Rate-limiting logic for Twitter API requests
│
├── .env                          # Environment variables for API keys and tokens
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── main.py                       # Entry point for the bot
