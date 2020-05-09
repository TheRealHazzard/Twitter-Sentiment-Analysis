# Twitter-Sentiment-Analysis-Web
Sentiment analysis falls under the domain of Pattern Classification and Data Mining. Sentiment analysis is also often called opinion mining. Sentiment analysis deals with predicting the mood of the person based on classifying tweets and using natural language processing (NLP) techniques. For example, let’s say the word ‘amazing’ means that the person is in a happy state while the word ‘uneasy’ can mean the person is not so happy about it. By using NLP techniques, we differentiate between the important words and the unnecessary words which can be used further for classification. Also, since the tweet can contain special characters like hashtags, we also are eliminating these delimiters for accurate classification of the text.
Here , Twitter Sentiment Analysis is done using Textblob and Tweepy, wrapped with Flask as a web app.


## Installation
1. Clone/Download this repository.
2. Obtain your Twitter API credentials.
3. Replace appropriate credentials in ```main.py``` file.
4. Install all the required dependencies listed in ```requirements.txt```.
5. Run the flask server using ```python main.py``` to see the result on port 5000(by default).

## A brief on the libraries used :
Mainly TextBlob and Tweepy are used for the main functionality. TextBlob is a great choice for NLP tasks, built on top of the famous Python library for NLP, i.e., NLTK.
Tweepy is used for Interacting easily with the Twitter API and handling complex tasks such as Authentication(OAuth) with after obtaining the relevant credentials from Twitter Developer API.

## Developed By:
Robin Thomas J
as a Web Mining Digital Assigment Project


