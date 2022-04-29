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


# Begins the projects #################################################
def start_project():
    beginningChoice = input(
        "Welcome to TheShoeTracker. Here are some options:\n a) search for the top sneaker accounts\n b)search for specific keywords\nPlease enter your choice: ")

    # if beginningChoice equals a, then run users
    if beginningChoice == "a":
        # set q to search for sneakers, sneaker, kicks
        query = input('Please enter your search query: ')
        users = api.search_users(query)
        for user in users:
            print(user.screen_name+' - '+str(user.followers_count)+' followers')
            print("\n")
            if user.followers_count > 100000:
                print('The account '+user.screen_name+' has ' +
                      str(user.followers_count)+' followers')

        topFollowers = input(
            "Would you like to see the most reputable accounts? (y/n) ")
        if topFollowers == "y":
            # print the accounts that have more than 100000 followers.
            print(
                'These are the users that are worth following (more than 100k followers)')
            for user in users:
                if user.followers_count > 100000:
                    print(user.screen_name + ' - ' + 'you should follow')
                    print("\n")

        else:
            print("Okay, goodbye!")

    if beginningChoice == "b":
        choice = input("Enter the hashtag: ")

        tweets = tweepy.Cursor(api.search_tweets, q=choice).items(2)

        for tweet in tweets:
            # if tweet.text contains 'test tweet 1', return hello!
            if '$' in tweet.text:
                print("hello!")
            print(tweet.text)
            # print the amount of likes that the tweet has
            print(str(tweet.favorite_count)+' likes')

            print("\n")

    if beginningChoice == "c":
        print("Enter the @ of the trusted sneaker account you would like to pull information from. We recommend ")

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

            # Printing the tweets
            print(tweetArray)

        # Driver code
        if __name__ == '__main__':
            # Here goes the twitter handle for the user
            # whose tweets are to be extracted.
            get_tweets(input('Enter @: '))


# This allows the user to start the project again instead of ending the function
while True:
    start_project()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
