# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 03:52:52 2017

@author: Arafat
"""

import pandas as pd
import tweepy
from textblob import TextBlob

consumer_key = '_'
consumer_secret = '_'

access_token = '_'
access_token_secret = '_'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('USA')

textList = list()
sentimentList = list()

for tweet in public_tweets:
    txt = tweet.text
    textList.append(txt)
    analysis = TextBlob(txt)
    pol = analysis.sentiment.polarity
    if(pol < 0):
        sentimentList.append('Positive')
    else:
        sentimentList.append('Negative')
    
dataFrame = pd.DataFrame({'Tweet':textList, 'Sentiment':sentimentList})
dataFrame.to_csv('sentiment.csv', sep=',', encoding='utf-8')