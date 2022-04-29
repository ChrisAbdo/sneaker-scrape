import time
import datetime
import tweepy

access_token = "1518980900029095938-CwZ7M4P9pjfEhHFoKOQDTaH6ltCXS7"
access_token_secret = "LnLT2JfumjaxaZYeyIAp674f92dXFQdZkwU2NlKEVFmnC"

api_key = "Bt1HVhGcL1Z4oCSGZQ2lzIE3V"
api_key_secret = "9kbkZPNXRaTQ6juAoSOxUuUYbIZNAvX69xEuA9zfc4ta5CKKFT"

auth = tweepy.OAuthHandler(
    consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_tweets(api, username):
    page = 1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page=page)

        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days < 2:
                print(tweet.text.encode('utf-8'))
            else:
                deadend = True
                return
        if not deadend:
            page += 1
            time.sleep(500)


get_tweets(api, 'SpaceX')
