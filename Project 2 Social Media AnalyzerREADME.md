# EC601
Social Media Analyzer 

My app called TweeterFreezer is a Social Media Analyzer that searches positive facts/news related to Boston from the twitter account @OnlyInBoston via the Twitter API v2. This twitter account usually tweets news/facts related to Boston which may not always be positive. As someone who uses social media quite a bit, it could be draining seeing negative news frequently. This app tries to mitigate this issue by tweeting one postive boston related tweet per day.

The app also tweets Boston's weather forecast after tweeting a positive fact. As someone who constantly forgets to check the weather before I leave the house but always remembers to check twitter, this would be extremely helpful. :)

HOW THE APP WORKS/BASIC ARCHITECTURE
The app uses the twitter API v2 to create a client object by using the necessary keys assigned in the developer portal on twitter. Through this client object, you can request tweets from a specific user account and state how many tweets you would like to collect each round (This app requests 100 tweets). As a tweet is collected, it is added to a list so that each tweet can be cleaned (unnecessary spaces, @'s, website links or symbols removed). After the tweets are cleaned, the built in twitter NLP is used to collect the polarity value of each tweet. This value describes the sentiment of the tweet, the is, how negative or positive it is on a scale from -1 to 1. My app chooses tweets with a polarity greater than zero and adds them to a data frame. A random number between and including 0 to the length of the data frame - 1 is generated and then that number determines the tweet to be sent out.

The app also uses the OpenWeatherMap API to create an object with the needed API key and request the current weather conditions in Boston from the OpenWeatherMap website. The parameters collected are temperature, humidity and weather description.

ERROR HANDLING
Twitter API v2:
The create tweet method are surrounded by try except blocks to account for twitter server errors, attempts to send duplicate tweets or tweets that are too long. If any of these occur, a message related to the error is printed. Other than that, the tweet is successfully sent and a message is printed confirming this.

OpenWeatherMap API
If a 404 error is caught, a message is printed stating that the chosen city has not been found or the input URL is incorrect.
