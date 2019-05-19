# -*- coding: utf-8 -*-
"""
Created on Sat Feb  16 19:25:11 2019

@author: YASH
"""

import tweepy
from textblob import TextBlob
import pandas as pd
import re
import matplotlib.pyplot as plt

# Step 1 - Authenticate
def authenticate(): 
    consumer_key= 'CONSUMER_KEY'
    consumer_secret= 'CONSUMER_KEY_SECRET'
    access_token='ACCESS_TOKEN'
    access_token_secret='ACCESS_TOKEN_SECRET'
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except:
        print("Authentication Failed")

def preprocess_tweet(tweet): 
	return re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(http:\S+)|(RT)", '', tweet) 

def get_sentiment(score):
    if score>0:
        return 'Positive'
    elif score<0:
        return 'Negative'
    else:
        return 'Neutral'


def create_report(data):
    neg_tweets=0
    pos_tweets=0
    neu_tweets=0
    for index, row in data.iterrows():
        if row['Polarity']=='Positive':
            pos_tweets=pos_tweets+1
        elif row['Polarity']=='Negative':
            neg_tweets=neg_tweets+1
        else:
            neu_tweets=neu_tweets+1    
    summ_data = {'Class':['Positive','Negative', 'Neutral'],
                 'Count':[pos_tweets, neg_tweets,neu_tweets]}
    df = pd.DataFrame(summ_data)    
    plt.figure(figsize=(16,8))
    # plot chart
    ax1 = plt.subplot(121, aspect='equal')
    df.plot(kind='pie', ax=ax1, autopct='%1.1f%%', 
     startangle=90, shadow=False, labels=df['Class'], legend = False, fontsize=14, y='Count')
    plt.title("Sentiment Distribution Chart")
    plt.show()
        
#Take input from command line
api = authenticate()
#Step 3 - Retrieve Tweets
query=input("Please enter search term:")
public_tweets = api.search(q=query, count=20)
tweets =[]
polarity=[]
scores=[]
tweets_analysis=dict()
for tweet in public_tweets:
    #clean tweet
    tweet_txt=preprocess_tweet(tweet.text)
    tweets.append(tweet_txt)
    analysis= TextBlob(tweet.text)
    scores.append(analysis.sentiment.polarity)                    
    polarity.append(get_sentiment(analysis.sentiment.polarity))
tweets_analysis={'Tweet':tweets,'Score':scores, 'Polarity':polarity}
data =pd.DataFrame(tweets_analysis)
data.to_csv('report.csv',header=True, index=True)
create_report(data)    
