# import the module
import tweepy

# assign the values accordingly
consumer_key = "Bt1HVhGcL1Z4oCSGZQ2lzIE3V"
consumer_secret = "9kbkZPNXRaTQ6juAoSOxUuUYbIZNAvX69xEuA9zfc4ta5CKKFT"
access_key = "1518980900029095938-CwZ7M4P9pjfEhHFoKOQDTaH6ltCXS7"
access_secret = "LnLT2JfumjaxaZYeyIAp674f92dXFQdZkwU2NlKEVFmnC"


def get_tweets(username):

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 2
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:

        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Printing the tweets
    print(tmp)


# Driver code
if __name__ == '__main__':

    # imput the username
    get_tweets(input('Enter'))
