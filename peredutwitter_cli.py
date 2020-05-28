import sys
import tweepy
import config

def tweepysearch(search, number, count):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK\n")
    except:
        print("Error during authentication\n")

    user = api.me()
    print(f"Welcome {user.name}\n")

    search = search
    numberOfTweets = number
    count = count

    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search, q=search, tweet_mode='extended', include_entities=True).items(numberOfTweets):
        if tweet.favorite_count > count or tweet.retweet_count > count:
            print(f"{tweet.retweet_count}|{tweet.favorite_count} - {tweet.user.name} {tweet.user.screen_name}: {tweet.full_text}\nhttps://twitter.com/{tweet.user.screen_name}/status/{tweet.id}\n")
            print(tweet)
            print('\n\n\n\n\n\n\n\n\n\n')

if __name__ == '__main__':
    tweepysearch(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))