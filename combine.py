# Tweepy is really the only dependency required, potentially IMPORT MATH
import tweepy

# Access codes - Twitter for Developers ###############################
access_token = "1518980900029095938-CwZ7M4P9pjfEhHFoKOQDTaH6ltCXS7"
access_token_secret = "LnLT2JfumjaxaZYeyIAp674f92dXFQdZkwU2NlKEVFmnC"

api_key = "Bt1HVhGcL1Z4oCSGZQ2lzIE3V"
api_key_secret = "9kbkZPNXRaTQ6juAoSOxUuUYbIZNAvX69xEuA9zfc4ta5CKKFT"
#######################################################################

# Simple Twitter Authentication for Elevated Access Point #############
auth = tweepy.OAuthHandler(
    consumer_key=api_key, consumer_secret=api_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#######################################################################

# create a separator so you only have one line in the code
sep = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# Begins the projects #################################################


def start_project():
    beginningChoice = input(
        "Welcome to TheShoeTracker. Here are some options:\n a) search for the top sneaker accounts\n b) search for specific keywords\n c) search for tweets from a specific account\nPlease enter your choice: ")

    # if beginningChoice equals a, then run users
    if beginningChoice == "a":
        # set q to search for sneakers, sneaker, kicks
        query = input(
            'Please enter your search query (i.e sneakers, sneaker, kicks, shoes): ')
        # query_count = int(input("How many accounts would you like to see?"))
        # users = api search for query and query_count

        users = api.search_users(query)
        print(sep)

        print('The top accounts for ' + query + ' are: ')
        print('\n')
        for user in users:
            print(user.screen_name+' - '+str(user.followers_count)+' followers')
            print("\n")
        print(sep)
        topFollowers = input(
            "Would you like to see the most reputable accounts? (y/n) ")
        print(sep)
        if topFollowers == "y":
            # print the accounts that have more than 100000 followers.
            print(
                'These are the users that are worth following (more than 100k followers):')
            print('\n')
            for user in users:
                if user.followers_count > 50000:
                    # print the screen name of the user and their followers count
                    print(user.screen_name+' - Very reputable account with ' +
                          str(user.followers_count)+' followers')
                    print("\n")

        else:
            print("Okay. Returning back to main page.")

    if beginningChoice == "b":
        choice = input(
            "Enter the hashtag/term (i.e air jordan 1, air jordan 2, air jordan 3, etc, yeezys): ")
        choice_amount = int(input('How many tweets would you like to see?: '))
        tweet_type = input(
            'Would you like to see popular or mixed tweets? (popular or mixed): ')
        print(sep)
        # tweets = api search with q=choice, result_type='popular' and count=choice_amount
        tweets = api.search_tweets(
            q=choice, result_type=tweet_type, count=choice_amount)

        # hash_tag likes = sum of the likes from the tweets
        hash_tag_likes = sum(tweet.favorite_count for tweet in tweets)

        for tweet in tweets:
            # if tweet.text contains 'test tweet 1', return hello!
            if '$' in tweet.text:
                print("This tweet has the price mentioned!")
            print(tweet.text)
            # print the amount of likes that the tweet has
            print(str(tweet.favorite_count)+' likes')
            print("\n")
        print('The term '+choice+' has ' +
              str(hash_tag_likes)+' likes in the past week (fully includes all tweets, not just choice_amount)')

    if beginningChoice == "c":
        print("Enter the @ of the trusted sneaker account you would like to pull information from. We recommend kicksonfire, zSneakerHeadz, sneakerhuddle, SoleRetriever, SOLELINKS.\nIt is pretty apparent which sneakers catch the attention of sneaker collectors due to the drastic increase in likes.")

        print("\n")
        # Inner function for retrieving the tweets from a specific account, utilizing  if __name__ == '__main__' to ensure that the function is only called when the file is run directly.

        def get_tweets(username):
            tweets = api.user_timeline(screen_name=username)

            # Empty Array
            tweetArray = []

            # create array of tweet information: username,
            # tweet id, date/time, text
            # CSV file created
            tweets_for_csv = [tweet.text for tweet in tweets]
            for j in tweets_for_csv:

                # Appending tweets to the empty array tmp
                tweetArray.append(j)

            # Print 10 recent tweets and their favorite_count
            number_of_tweets = int(
                input("How many tweets would you like to see? "))
            for tweet in tweets[:number_of_tweets]:
                # Removing ad here to keep content consistent, the ad is still a release date
                print(tweet.text.replace('Ad:', ''))
                print(str(tweet.favorite_count)+' likes')
                print(str(tweet.retweet_count)+' retweets')
                print("\n")

            total_likes = sum(int(tweet.favorite_count) for tweet in tweets)
            print("Total likes for the user timeline: " + str(total_likes))

            total_retweets = sum(int(tweet.retweet_count) for tweet in tweets)
            print("Total retweets for the user timeline: " + str(total_retweets))
            print("\n")

            top_tweets = input(
                'Would you like to split the tweet into an array of the shoe name? y/n\n')
            if top_tweets == "y":
                # here we set the loop to the custom integer input of number_of_tweets
                for tweet in tweets[:number_of_tweets]:
                    if tweet.favorite_count > 100:
                        print("\n")
                        # hard coded the number of words to print, can be modified however 5 seems to work well
                        print(tweet.text.split()[:5])
                        # print the number of likes that the tweet has
                        print(str(tweet.favorite_count)+' likes')

                        # print the status id of the tweet and link to the tweet
                        print('Link to the tweet: https://twitter.com/' +
                              username + '/status/' + tweet.id_str)
                        # if the tweet has an image associated with it, print the link to the image
                        if tweet.entities.get('media', False):
                            media_url = tweet.entities['media'][0]['media_url']
                            print('Link to the image: ' + media_url)

                        print("\n")
                        # print the first 5 words of the tweet

        # Driver code
        if __name__ == '__main__':
            # Here goes the twitter handle for the user
            # whose tweets are to be extracted.
            get_tweets(input('Enter @: '))


print(sep)
# This allows the user to start the project again instead of ending the function
while True:
    start_project()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
