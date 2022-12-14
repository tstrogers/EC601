# EC601
Social Media Analyzer 

My app called TweeterFreezer is a Social Media Analyzer that searches positive facts/news related to Boston from the twitter account @OnlyInBoston via the Twitter API v2. This twitter account usually tweets news/facts related to Boston which may not always be positive. As someone who uses social media quite a bit, it could be draining seeing negative news frequently. This app tries to mitigate this issue by tweeting one postive boston related tweet per day.

The app also tweets Boston's weather forecast after tweeting a positive fact. As someone who constantly forgets to check the weather before I leave the house but always remembers to check twitter, this would be extremely helpful. :)

HOW THE APP WORKS/BASIC ARCHITECTURE

The app uses the twitter API v2 to create a client object by using the necessary keys assigned in the developer portal on twitter. Through this client object, you can request tweets from a specific user account and state how many tweets you would like to collect each round (This app requests 100 tweets). As a tweet is collected, it is added to a list so that each tweet can be cleaned (unnecessary spaces, @'s, website links or symbols removed). After the tweets are cleaned, the built in twitter NLP is used to collect the polarity value of each tweet. This value describes the sentiment of the tweet, the is, how negative or positive it is on a scale from -1 to 1. My app chooses tweets with a polarity greater than zero and adds them to a data frame. A random number between and including 0 to the length of the data frame - 1 is generated and then that number determines the tweet to be sent out.

#Example Code

<img width="761" alt="Screen Shot 2022-12-19 at 10 33 13 PM" src="https://user-images.githubusercontent.com/93225913/208572513-84035107-3940-44c5-a9fc-1e4b80524d6d.png">


The app also uses the OpenWeatherMap API to create an object with the needed API key and request the current weather conditions in Boston from the OpenWeatherMap website. The parameters collected are temperature, humidity and weather description.

#Example Code

<img width="731" alt="Screen Shot 2022-12-19 at 11 10 52 PM" src="https://user-images.githubusercontent.com/93225913/208573155-b2a1fff7-a71d-4830-a82a-f4f0a487e996.png">


ERROR HANDLING

Twitter API v2:

The create tweet method is surrounded by try except blocks to account for twitter server errors, attempts to send duplicate tweets or tweets that are too long. If any of these occur, a message related to the error is printed. Other than that, the tweet is successfully sent and a message is printed confirming this.

#Example Code

<img width="731" alt="Screen Shot 2022-12-19 at 11 10 52 PM" src="https://user-images.githubusercontent.com/93225913/208572669-30eac805-fe45-47ea-8492-4d023433642c.png">


OpenWeatherMap API:

If a 404 error is caught, a message is printed stating that the chosen city has not been found or the input URL is incorrect.


AUTOMATING THE SCRIPT

The script can be automated by creating an exe file of the script using the command: pyinstaller --onefile [NAME_OF_FILE] and then using crontab -e to set the time, date and frequency of running the script. Use crontab.guru for help setting the time, data and frequency parameters. It is important to ensure that the modules used in the script are in the same path as pyinstaller, else there may be importation errors.

