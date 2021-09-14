import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()


def handle_rate_limit(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Automatically follow people back
for follower in handle_rate_limit(tweepy.Cursor(api.followers).items()):
    follower.follow()

# Automatically love your own tweets or love a tweet based on some certain words
query_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, query_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break
