#Author Robin Thomas
from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob

consumer_key = 'A3tMsP66iCW5Gqeja8xiwOkmD'
consumer_secret = 'qjw9CTugWwwrvWtyHrDgvPahE1RQmQUqWBQFWod6dWSAhsSwBI'

access_token = '3052501375-FY3TxCbMMZRq0dSJO9SZ5KENnwsYoeCPBYl8jHX'
access_token_secret = 'ugi79nBbiY3BYaq758HZCyopOCs4wgDdML0pEK5Ntukmn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])


    return jsonify({"success":True,"tweets":t})

class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        '''# keys and tokens from the Twitter Dev Console 
        consumer_key = 'qBUPcn9g2BDgn4YuIThH1uamj'
        consumer_secret = 'K3nrtfYWMMm5cgQKxmGNKc0hWRKEsvu4gi8LSKR4i4n2nCqRWl'
        access_token = '1183353803354980352-XcB4ddx8348bgPV8pIMgWg347A3t3Y'
        access_token_secret = '25k7k8LMS8eTesUJUmbeFbsNTA87uly0Qvuzw0Ho4IyFT'
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") '''
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("""(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) 
                                    |(\w+:\/\/\S+)""", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''

        analysis = TextBlob(self.clean_tweet(tweet)) 

        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets 
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
  
def MAIN(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = 'Donald Trump', count = 200) 
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} % \ ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets))) 
    
    analyser = SentimentIntensityAnalyzer() #using object for sentiment intensity analyzer
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
        sentiment_dict = analyser.polarity_scores(tweet['text'])   #dictionary for which contains the scores 
        print(str(sentiment_dict))

        
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
        sentiment_dict = analyser.polarity_scores(tweet['text']) 
        print(str(sentiment_dict))


app.run()