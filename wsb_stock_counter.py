import pandas as pd
from pmaw import PushshiftAPI
from datetime import datetime
import csv
from gensim.parsing.preprocessing import remove_stopwords

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stock_count={}

stock_ticker_list=[]
with open('nasdaq_stocks.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(row[0])
        stock_ticker_list.append(row[0])       

api = PushshiftAPI()
starttime=int(datetime(2021, 1, 30).timestamp())
beforetime=int(datetime(2021, 2, 2).timestamp())

submissions = api.search_submissions(after=starttime,before=beforetime,subreddit="wallstreetbets", 
                                                        filter=['title','created_utc'],limit=3000)

df = pd.DataFrame(submissions)
#posts=df['title']
posts=df

for index,row in posts.iterrows():
    #print(row['title'])
    title=row['title']
    title=title.lower()
    #print(title)
    for char in title: #remove punctuation
        if char=="'":
            char=''
        elif char in punctuation:
            title=title.replace(char, '')
    title=remove_stopwords(title)
    title=title.upper()
    title_words=title.split()
    #print(title_words)
    for symbol in title_words:
        if symbol in stock_ticker_list:
            if symbol in stock_count:
                stock_count[symbol]+=1
            elif symbol not in stock_count:
                stock_count[symbol]=1
df_stock_count=pd.DataFrame(list(stock_count.items()),columns=['stock','count']).sort_values('count', ascending=False)

#print(df_stock_count)
df_stock_count.to_csv('wallstreetbets.csv', header=True, index=True)