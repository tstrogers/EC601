# EC601
Project2_2.py retrieves the likes, mentions and tweets of the @botometer user on twitter and writes the results to different txt files. The txt files entitled botometerlikes.txt, botometermentions.txt and botometertweets.txt include the most recent 3200 (if possible) likes, mentions and tweets respectively of @botometer. The text file entitled tweetinfo.txt includes the author ids, time stamps and languages of the 20 most recent tweets across the platform containing the the key word music. Only original tweets were collected as retweets were excluded.

Example output:

<img width="1115" alt="Screen Shot 2022-12-19 at 10 10 42 PM" src="https://user-images.githubusercontent.com/93225913/208565735-786bec28-0eff-4285-aba3-4d0770522f07.png">





<img width="1085" alt="Screen Shot 2022-12-19 at 10 11 33 PM" src="https://user-images.githubusercontent.com/93225913/208565116-e37a56e5-4b0c-4516-92d7-00707f5a3148.png">





<img width="868" alt="Screen Shot 2022-12-19 at 10 11 09 PM" src="https://user-images.githubusercontent.com/93225913/208567251-74b771aa-c849-4900-a533-1b2f280be2f9.png">


#Code Explanation

The twitter API is used to search tweets of the client who is in this case botometer. The botometer twitter account is identified by a unique ID. A newly named file is opened before each method is called. The method dictates if the most recent likes, etc are collected. The twitter API can only be used with tokens/keys issued by twitter.

<img width="1068" alt="Screen Shot 2022-12-19 at 10 57 21 PM" src="https://user-images.githubusercontent.com/93225913/208571589-e4dfc3ba-7b5b-4c5c-9471-428e0556ad14.png">


<img width="873" alt="Screen Shot 2022-12-19 at 10 57 44 PM" src="https://user-images.githubusercontent.com/93225913/208571640-c885c244-f247-4c61-8337-5979401564b7.png">




