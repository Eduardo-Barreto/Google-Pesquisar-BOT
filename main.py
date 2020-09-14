import twitter
import text

tweets = twitter.getTweets()

for tweet in tweets:
    print(tweet.text, tweet.user.screen_name)