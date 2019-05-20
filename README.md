# twitter-sentiment
Twitter Sentiment Analyzer using tweepy and textblob. 

->Overview
This project is based on analyzing sentiments/ opinions of users' tweets on a particular topic/person or product and thereby, segregating tweets into 3 categories: Positive, Neutral, Negative. 

->Dependencies 

Tweepy used to access and authenticate the twitter apis to search tweets based on a query entered by the user
TextBlob is used to tokenize and analyze the tweets to calculate the sentiment value of each tweet.

-> Usage 
python Twitter-sentiment.py

Working Steps:
1. Auhtenticate the twitter user to access the api.
2. Search for tweets based on input given by the user.
3. Preprocess tweets to remove URL and image references.
4. Calculate sentiment value for each.
5. Generate a csv report.
6. Pie chart is generated for better visualization of sentiment classification.
