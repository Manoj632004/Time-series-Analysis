from ntscraper import Nitter
from datetime import datetime, timedelta
import pandas as pd
import time

scraper = Nitter()

# Search settings
query = "MetaAI"
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 1, 1)
current = start_date

data = scraper.get_tweets(
            query,
            mode="hashtag"
        )

print(data)
"""

results = []


while current < end_date:
    next_week = current + timedelta(days=7)

    try:
        data = scraper.get_tweets(
            query,
            mode="hashtag",
            since=current.strftime('%Y-%m-%d'),
            until=next_week.strftime('%Y-%m-%d'),
            number=100  # max number of tweets to check
        )
        count = len(data['tweets'])

        print(f"{current.date()} to {next_week.date()} — {count} tweets")
        results.append({
            "week": f"{current.date()} to {next_week.date()}",
            "tweet_mentions": count
        })

    except Exception as e:
        print(f"Error on {current.date()} — {e}")
        results.append({
            "week": f"{current.date()} to {next_week.date()}",
            "tweet_mentions": 0
        })

    current = next_week
    time.sleep(0.5)  # to avoid rate-limiting

# Save results
df = pd.DataFrame(results)
df.to_csv("meta_ai_twitter_mentions_weekly.csv", index=False)
print("\n✅ Done! Sample:")
print(df.head())
"""
