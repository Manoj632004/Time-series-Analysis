from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=330)

#keywords = ["Meta Quest", "Meta Quest 3", "Meta Quest Pro", "Oculus Quest", "Meta AR glasses"]
keywords = [
    "Meta AI",
    "Meta AI app",
    "Llama 4",
    "LlamaCon",
    "Meta Motivo",
]

pytrends.build_payload(kw_list=keywords, timeframe='2023-01-01 2025-01-01')

data = pytrends.interest_over_time()
data = data.drop(columns=['isPartial'])

print(data.head())
data.to_csv("Dataset/meta_arvr_trends.csv")
