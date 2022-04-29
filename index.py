import tweepy

access_token = "1518980900029095938-CwZ7M4P9pjfEhHFoKOQDTaH6ltCXS7"
access_token_secret = "LnLT2JfumjaxaZYeyIAp674f92dXFQdZkwU2NlKEVFmnC"

api_key = "Bt1HVhGcL1Z4oCSGZQ2lzIE3V"
api_key_secret = "9kbkZPNXRaTQ6juAoSOxUuUYbIZNAvX69xEuA9zfc4ta5CKKFT"

auth = tweepy.OAuthHandler(
    consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


choice = input("Enter the hashtag: ")

tweets = tweepy.Cursor(api.search_tweets, q=choice).items(10)

for tweet in tweets:
    # if tweet.text contains 'test tweet 1', return hello!
    if 'test tweet 1' in tweet.text:
        print("hello!")
    print(tweet.text)
    print("\n")

for user in users:
    print(user.screen_name)
    print("\n")
