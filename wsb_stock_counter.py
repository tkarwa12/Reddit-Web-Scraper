import pandas as pd
from pmaw import PushshiftAPI
from datetime import datetime
import csv

stock_ticker_list=[]
with open('nasdaq_stocks.csv') as csv_file:
    csv_reader=csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        print(row[0])


api = PushshiftAPI()
starttime=int(datetime(2021, 1, 30).timestamp())
beforetime=int(datetime(2021, 2, 2).timestamp())

submissions = api.search_submissions(after=starttime,before=beforetime,subreddit="wallstreetbets", filter=['title','created_utc'],limit=10)

df = pd.DataFrame(submissions)
#posts=df['title']
posts=df
for index,row in posts.iterrows():
    #print(row['title'])
    title=row['title']
    title=title.upper()
    print(title)
    break
#comments_df.to_csv('wallstreetbets.csv', header=True, index=False)