#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

user = api.me()
print(user.name)
print(user.location)


# In[3]:


# USER

user = api.get_user("MikezGarcia")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)


# In[20]:


# TRENDS

api.trends_available()
api.trends_place(1099805)


# In[ ]:


# SEARCH

search = 'cybersecurity'
numberOfTweets = 5


# In[38]:


# STANDARD

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q=search).items(numberOfTweets):
    print('=======')
    print(tweet.text)


# In[39]:


# AS PANDAS DATAFRAME

import pandas as pd
api = tweepy.API(auth)
results = api.search(q=search, count=numberOfTweets)
json_data = [r._json for r in results]
df = pd.json_normalize(json_data)
df


# In[40]:


# AS JSON

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
results = api.search(q=search, count=numberOfTweets)
results.keys()
results["statuses"]


# In[ ]:




