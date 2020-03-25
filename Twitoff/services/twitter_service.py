# web_app/services/twitter_service.py

import os
from dotenv import load_dotenv
import tweepy
from pprint import pprint

load_dotenv()

# twitter access hidden in env
consumer_key = os.getenv("TWITTER_API_KEY", default="OOPS")
consumer_secret = os.getenv("TWITTER_API_SECRET", default="OOPS")
access_token = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")

def twitter_api_client():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("AUTH", type(auth))

    api = tweepy.API(auth)
    print("API", type(auth))
    return api

if __name__ == "__main__":
    # breakpoint()
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
    
    # get info on user
    
    api = twitter_api_client()
    
    screen_name = "elonmusk"
    
    print("----------------")
    print("USER......")
    user = api.get_user(screen_name)
    print(type(user))  # class 'tweepy.models.User
    print(user.screen_name)
    print(user.followers_count)
    pprint(user._json)
    
    # get users tweets:
    statuses = api.user_timeline(screen_name, tweetmode="extended", count=100, exclude_replies=True, include_rts=False )