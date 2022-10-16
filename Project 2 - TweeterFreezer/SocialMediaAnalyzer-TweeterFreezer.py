#Author: Tsani Rogers
import config
import pyowm
import requests, json
import tweepy
import pandas as pd
import re
from textblob import TextBlob
import random

#Twitter tokens/keys
bearer_token = config.bearer_token
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

#OnWeatherMap key and setup
APIKEY = config.owm_api_key
owm = pyowm.OWM(APIKEY)
reg = owm.city_id_registry()
city_name = "Boston"

#Connect to Twitter API via client object
#Source: Twitter API github github.com/tweepy
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

#Initializing needed variables
df = pd.DataFrame(columns=['Tweets'])
listoftweets = []
cleantweets = []
polarity = []
subjectivity = []
results = []
weather = ""

#Clean tweets
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+','',text) #Removes @mentions
    text = re.sub(r'#', '', text) #Removes hastag
    text = re.sub(r'RT[\s]+','',text) #Removing RT
    text = re.sub(r'https?:\/\/\S+', '', text) #Remove hyper link
    
    return text
    
#Extracts 100 tweets from twitter account @OnlyInBOS
account_id = client.get_user(username="OnlyInBOS").data.id
def get_most_recent_tweets():
    tweets = client.get_users_tweets(account_id,max_results = 100,tweet_fields="text")
    for tweet in tweets.data:
        listoftweets.append(tweet.text)
    

#Sentiment analysis (determines if a tweet is positive or negative)
def get_polarity(text):
    return TextBlob(text).sentiment.polarity

#100 Tweets collected and saved in list 
get_most_recent_tweets()

#List of tweets cleaned (Unnecessary symbols etc removed)
def get_clean_tweets():
    for x in listoftweets:
        cleantxt = cleanTxt(x)
        cleantweets.append(cleantxt)

get_clean_tweets()  

#Polarity of each tweet collected and stored in list
def get_polarity_tweets():
    for x in cleantweets:
        polarity.append(get_polarity(x))

get_polarity_tweets()
    
#DataFrame of clean tweets and their respective polarities created
df = pd.DataFrame(list(zip(cleantweets,polarity)))
#DataFrame of only positive tweets collected
posdf = df[df.iloc[:,1] > 0]
#Indices reset to 0 to N-1
posdf2=posdf.reset_index(drop=True)
bottweetlist = posdf2.iloc[:,0]
list = list(bottweetlist)
N = len(list)
i = random.randint(0, N-1)


#Accessing OnWeatherMap
#Credit: geeksforgeeks.org

base_url = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + 'appid=' + APIKEY + '&q=' + city_name

#Gets Boston related weather info from OnWeatherMap website
response = requests.get(complete_url)
x = response.json()

#Accounts for any 404 errors
if x["cod"] != "404":
    y = x["main"]
    current_temp = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    weather = (" Temperature = " +
                    str(str(round(1.8*(current_temp-273)+32)) + "F")+ 
          "\n humidity = " +
                    str(str(current_humidity)+"%") +
          "\n description = " +
                    str(weather_description))
else:
    print("City not found or incorrect URL")

#Sends positive tweets and weather info to twitter account
try: 
    client.create_tweet(text=bottweetlist.iloc[i] +  "\n\n Credit: Only In Boston" )
    client.create_tweet(text= "Current weather in Boston: \n" + weather +  "\n\n Have a Nice Day :)" )
except tweepy.Forbidden:
    print(tweepy.Forbidden)
    print("A duplicate tweet is being sent :((")
except tweepy.TwitterServerError:
    print("Twitter is experiencing issues at the moment :((")
except tweepy.BadRequest:
    print("The tweet text is too long :((")
else:
    print("Tweet successfully sent :))")

