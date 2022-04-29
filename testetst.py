# import the module
import tweepy

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

# screen name of the account to be fetched
screen_name = "kicksonfire"

# number of statuses to be fetched
count = 3

# fetching the statuses
statuses = api.user_timeline(screen_name, count=count)

# printing the statuses
for status in statuses:
    print(status.text, end="\n\n")
