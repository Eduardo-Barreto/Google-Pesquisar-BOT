import tweepy
from datetime import datetime

import authkeys
auth = tweepy.OAuthHandler(authkeys.key1, authkeys.key2)
auth.set_access_token(authkeys.key3, authkeys.key4)

twiiter = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def getFirstTweet():
    agora = datetime.now().strftime('%Y-%m-%d')
    return tweepy.Cursor(twiiter.search, q='google pesquisar', since=agora).items(1)


def getTweets(last_id):
    return tweepy.Cursor(twiiter.search, q='google pesquisar', since_id=last_id).items(15)


def reply(tweet_id, content, url):
    twiiter.update_with_media(
        status=content+'\n\nsua pesquisa: '+url,
        filename='screenshot.jpg',
        in_reply_to_status_id=tweet_id,
        auto_populate_reply_metadata=True
    )

def nao_foi(tweet_id):
    read_last_tweets = open('./last_tweets.txt', 'r')

    for linha in read_last_tweets:
        if str(tweet_id) in linha:
            read_last_tweets.close()
            return False

    read_last_tweets.close()
    return True
