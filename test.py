# import the module
import tweepy
import pandas as pd


# assign the values accordingly
consumer_key = "Bt1HVhGcL1Z4oCSGZQ2lzIE3V"
consumer_secret = "9kbkZPNXRaTQ6juAoSOxUuUYbIZNAvX69xEuA9zfc4ta5CKKFT"
access_token = "1518980900029095938-CwZ7M4P9pjfEhHFoKOQDTaH6ltCXS7"
access_token_secret = "LnLT2JfumjaxaZYeyIAp674f92dXFQdZkwU2NlKEVFmnC"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

keywords = '@kicksonfire'
limit = 300

tweets = tweepy.Cursor(api.search_tweets, q=keywords,
                       count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)
