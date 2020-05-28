import tweepy
import config

def tweepysearch(search, number):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()


    search = search
    numberOfTweets = number

    response = ''
    api = tweepy.API(auth)
    try:
        for tweet in tweepy.Cursor(api.search, q=search).items(numberOfTweets):
            response += f'{tweet.user.name} : {tweet.text}\n\n'
        return response
    except:
        response = 'uh oh 5'
        return response