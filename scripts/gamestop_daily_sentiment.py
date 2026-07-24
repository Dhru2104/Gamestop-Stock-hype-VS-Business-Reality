"""
This script takes the raw Reddit WallStreetBets dataset, filters it down to only posts 
that mention GameStop/GME, scores each post's sentiment,
and creates a clean DAILY summary (post count + average sentiment per day).

Requires: pandas, vaderSentiment
Install with: py -3.12 -m pip install pandas vaderSentiment
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# VADER is a pre-built sentiment tool - it reads text and gives a score
# from -1 (very negative) to +1 (very positive), 0 = neutral
analyzer = SentimentIntensityAnalyzer()

# 1. LOAD THE RAW REDDIT DATA
df = pd.read_csv("reddit_wsb.csv")

print("Total posts in dataset:", len(df))
print("Columns:", df.columns.tolist())

# Some posts have no body text (just a title) - fillna('') replaces
# those missing values with an empty string so we don't get errors later
df['body'] = df['body'].fillna('')

# Combine title + body into one "full_text" column
# We search across both, since a post might mention GME only in the body
df['full_text'] = df['title'].astype(str) + " " + df['body'].astype(str)

# 2. FILTER FOR ONLY GAMESTOP-RELATED POSTS
# .str.lower() makes the search case-insensitive (catches "GME", "gme", "Gme")
# .str.contains('gme|gamestop') checks if EITHER keyword appears anywhere
keywords = ['gme', 'gamestop']
mask = df['full_text'].str.lower().str.contains('|'.join(keywords), na=False)
gme_posts = df[mask].copy()

print(f"\nTotal GameStop-related posts found: {len(gme_posts)}")

# 3. RUN SENTIMENT ANALYSIS ON EACH POST
if len(gme_posts) == 0:
    print("No GME posts found - check column names or dataset content.")
else:
    # .apply() runs the sentiment analyzer on every single post's text
    # polarity_scores() returns 4 scores (neg, neu, pos, compound) -
    # we only keep 'compound', which is the single overall sentiment score
    gme_posts['sentiment'] = gme_posts['full_text'].apply(
        lambda x: analyzer.polarity_scores(x)['compound']
    )

    # Convert the full timestamp (with time) into just a plain date
    # This lets us group multiple posts from the same day together
    gme_posts['date'] = pd.to_datetime(gme_posts['timestamp']).dt.date

    # Save the full scored dataset (every post + its sentiment score)
    # This is the "raw working file" - not usually needed for charts directly
    gme_posts.to_csv("gamestop_reddit_sentiment.csv", index=False)

    print("\nSample of sentiment-scored posts:")
    print(gme_posts[['date', 'title', 'sentiment']].head(10))

    # 4. CREATE THE DAILY SUMMARY (this is the file used for charts)
    # .groupby('date') groups all posts from the same day together
    # .agg() then calculates, for each day:
    #   - post_count: how many posts that day (count)
    #   - avg_sentiment: the average sentiment score that day (mean)
    daily_summary = gme_posts.groupby('date').agg(
        post_count=('sentiment', 'count'),
        avg_sentiment=('sentiment', 'mean')
    ).reset_index()

    daily_summary.to_csv("gamestop_daily_sentiment_summary.csv", index=False)

    print("\nDaily summary saved to gamestop_daily_sentiment_summary.csv")
    print(daily_summary.head(10))