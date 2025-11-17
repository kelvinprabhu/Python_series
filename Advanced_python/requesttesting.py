import requests
import csv
import pandas as pd
response = requests.get("https://mp1a2a22a04d8c5c30fe.free.beeceptor.com/data")
# print("Status Code:", response.status_code)
# print("Response Body:", response.text)
# print("Response Headers:", response.headers)
# print("Response Json:", response.json)

data = response.json()
for item in data:
    print("Age:", item['age'])
    print("Name:", item['name'])
    print("---")
with open("response.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data[0].keys())
    for item in data:
        writer.writerow(item.values())

df = pd.DataFrame(data)
df.to_csv("response_pandas.csv",index=False)

