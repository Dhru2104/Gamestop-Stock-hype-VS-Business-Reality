import requests
import pandas as pd

headers = {'User-Agent': 'YourName YourEmail@example.com'}  # replace with your own name/email
url = "https://data.sec.gov/api/xbrl/companyconcept/CIK0001326380/us-gaap/Revenues.json"

response = requests.get(url, headers=headers)
data = response.json()

records = data['units']['USD']
df = pd.DataFrame(records)
df.to_csv("gamestop_sec_revenue_history.csv", index=False)
print(df.head(20))
print(f"\nTotal records: {len(df)}")