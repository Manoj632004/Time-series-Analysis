import praw
import pandas as pd
from datetime import datetime, timedelta

reddit = praw.Reddit(
    client_id='clientid',
    client_secret='secret',
    user_agent='meta-ai-mentions',
    #username='YOUR_REDDIT_USERNAME',
    #password='YOUR_PASSWORD'
)

query = "Meta AI"
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 1, 1)

results = {}
current_date = start_date

# Loop through each day
while current_date < end_date:
    next_day = current_date + timedelta(days=7)
    day_count = 0

    for submission in reddit.subreddit('all').search(query, sort='new', time_filter='all', limit=1000):
        post_time = datetime.fromtimestamp(submission.created_utc)
        if current_date <= post_time < next_day:
            day_count += 1

    results[current_date.date()] = day_count
    print(f"{current_date.date()} — {day_count} posts")
    current_date = next_day

df = pd.DataFrame(list(results.items()), columns=['date', 'reddit_mentions'])
df.to_csv("meta_ai_reddit_mentions.csv", index=False)
print("\n✅ Done! Sample output:")
print(df.head())
