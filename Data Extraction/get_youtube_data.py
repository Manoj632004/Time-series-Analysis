from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pandas as pd
import time

# 🔐 Add your API key here
API_KEY = 'AIzaSyBkBJmzi2rddV31e0ct_4qJw02Zy9vqY14'#'AIzaSyDbUC-Kr361dS4z2pFUXREuOp2_XzNAgK0'

# Initialize API client
youtube = build('youtube', 'v3', developerKey=API_KEY)
# Parameters
query = "Meta AI"
start_date = datetime(2023, 11, 4)
end_date = datetime(2024, 1, 6)
results = []

# Loop weekly
current = start_date
while current < end_date:
    next_week = current + timedelta(days=7)
    published_after = current.isoformat("T") + "Z"
    published_before = next_week.isoformat("T") + "Z"

    total_count = 0
    next_page_token = None

    while True:
        try:
            request = youtube.search().list(
                q=query,
                part="id",
                type="video",
                publishedAfter=published_after,
                publishedBefore=published_before,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            items = response.get('items', [])
            total_count += len(items)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
            time.sleep(0.2)  # brief pause between pages to respect rate limits

        except Exception as e:
            print(f"Error during pagination on {current.date()} — {e}")
            break

    print(f"{current.date()} to {next_week.date()} — {total_count} videos")
    results.append({
        "week": f"{current.date()} to {next_week.date()}",
        "youtube_mentions": total_count
    })

    current = next_week
    time.sleep(0.5)  # pause between weeks to respect quota

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("Dataset/meta_ai_youtube_mentions_5_2.csv", index=False)
print("\n✅ Done! Sample output:")
print(df.head())