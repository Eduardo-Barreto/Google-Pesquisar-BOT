import tweepy
from datetime import datetime

import authkeys
auth = tweepy.OAuthHandler(authkeys.key1, authkeys.key2)
auth.set_access_token(authkeys.key3, authkeys.key4)

twiiter = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def getFirstTweet():
    agora = datetime.now().strftime('%Y-%m-%d')
    return tweepy.Cursor(twiiter.search, 'Google Pesquisar', since=agora).items(1)

def getTweets():
    agora = datetime.now().strftime('%Y-%m-%d')
    return tweepy.Cursor(twiiter.search, 'Google Pesquisar', since=agora).items(30)

def reply(content, tweetId, url):
    twiiter.update_with_media(
        status=content+'\n\nsua pesquisa: '+url, 
        filename='screenshot.jpg', 
        in_reply_to_status_id=tweetId, 
        auto_populate_reply_metadata=True
    )