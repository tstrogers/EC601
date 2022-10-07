#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tsanirogers
"""
import config
import requests
import tweepy
import os

bearer_token = config.bearer_token
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret

#Connect to Twitter API    
#Source: Twitter API github github.com/tweepy

#Receiving most recent tweets related to music and saving their id, time created and language
client = tweepy.Client(bearer_token)
query = 'music -is:retweet'
file_name = 'tweetinfo.txt'


with open(file_name, 'a') as file:
    file.write('{a:^15}{b:^20}{c:^30}\n\n'.format(a='AUTHOR ID', b='TIME CREATED', c='LANGUAGE'))
    response = client.search_recent_tweets(query = query, max_results = 20, tweet_fields = ['created_at', 'lang'],expansions=['author_id'])

    for tweet in response.data:
        file.write ("{} {} {}\n".format(tweet.id, tweet.created_at, tweet.lang))
    file.close()
    
name = "botometer"
id = "2451308594"
#Get most recent 3200 tweets from botometer and writes them to a txt file
def get_most_recent_tweets():
    tweets = client.get_users_tweets(id)
    for tweet in tweets.data:
        file.write("{} \n\n".format(tweet))
  
file_name = "botometertweets.txt"
with open(file_name, 'a') as file:
    file.write("Botometer's most recent tweets:\n\n")
    get_most_recent_tweets()
    file.close()

#Gets the most recent mentions of a user and writes them to a file
def get_user_mentions():
    mentions = client.get_users_mentions(id)
    for tweet in mentions.data:
        file.write("{} \n\n".format(tweet))

file_name = "botometermentions.txt"
with open(file_name, 'a') as file:
    file.write("Botometer's most recent mentions:\n\n")
    get_user_mentions()
    file.close()

def get_user_likes():
    likes = client.get_liked_tweets(id)
    for tweet in likes.data:
        file.write("{} \n\n".format(tweet))
        
file_name = "botometerlikes.txt"
with open(file_name, 'a') as file:
    file.write("Botometer's most recent likes:\n\n")
    get_user_likes()
    file.close()
    
