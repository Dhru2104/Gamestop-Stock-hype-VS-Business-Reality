"""
Problem: The daily sentiment file has ~200 individual days, which makes
the chart too cluttered - many small bars/points become hard to see.

Fix: Group the data by WEEK instead of by day. This reduces ~200 data
points down to about 25-30 weekly points, each with a clear, visible
value - while still showing the exact same spike-then-decay story.
"""
import pandas as pd

# Load the daily summary (date, post_count, avg_sentiment)
df = pd.read_csv("gamestop_daily_sentiment_summary.csv")

# Convert the 'date' column into an actual datetime type
# (needed so pandas can group it correctly by week)
df['date'] = pd.to_datetime(df['date'])

# Create a new column that represents "which week does this date belong to"
# .dt.to_period('W') groups every date into its containing week
# Example: Jan 27, 28, 29, 30 (all in the same week) all get the same week label
df['week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)

# Now group by week and combine the daily numbers into one weekly number:
#post_count: SUM (total posts that week)
#avg_sentiment: MEAN (average sentiment across that week)
weekly_summary = df.groupby('week').agg(
    total_posts=('post_count', 'sum'),
    avg_sentiment=('avg_sentiment', 'mean')
).reset_index()

# Round sentiment to 3 decimal places for readability
weekly_summary['avg_sentiment'] = weekly_summary['avg_sentiment'].round(3)

# Save the clean weekly file
weekly_summary.to_csv("gamestop_weekly_sentiment_summary.csv", index=False)

print("Weekly summary created successfully!")
print(f"Reduced from {len(df)} daily rows to {len(weekly_summary)} weekly rows.\n")
print(weekly_summary)