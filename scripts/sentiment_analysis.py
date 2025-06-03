import os
import pandas as pd
import tweepy
from textblob import TextBlob


def fetch_tweets(query: str, max_results: int = 100):
    """Fetch recent tweets matching a query using Tweepy."""
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        raise EnvironmentError("TWITTER_BEARER_TOKEN environment variable not set")

    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    tweets = []
    for tweet in tweepy.Paginator(
        client.search_recent_tweets,
        query=query,
        tweet_fields=["created_at", "lang"],
        max_results=100,
    ).flatten(limit=max_results):
        if tweet.lang == "en":
            tweets.append(tweet.text)
    return tweets


def classify_sentiment(text: str) -> str:
    """Classify sentiment of a tweet using TextBlob polarity."""
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    if polarity < -0.1:
        return "negative"
    return "neutral"


if __name__ == "__main__":
    query = "bitcoin OR ethereum OR crypto -is:retweet lang:en"
    tweets = fetch_tweets(query, max_results=200)

    sentiments = [classify_sentiment(t) for t in tweets]
    df = pd.DataFrame({"tweet": tweets, "sentiment": sentiments})

    counts = df["sentiment"].value_counts().to_dict()
    print("Aggregated sentiment counts:", counts)

    output_path = os.path.join("..", "data", "tweet_sentiment.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved detailed results to {output_path}")
