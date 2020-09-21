import tweepy

import authkeys
auth = tweepy.OAuthHandler(authkeys.key1, authkeys.key2)
auth.set_access_token(authkeys.key3, authkeys.key4)

twiiter = tweepy.API(auth)


def getFirstTweets():
    return twiiter.search(q='Google Pesquisar', result_type='recent')

def getTweets(last_id):
    return twiiter.search(q='Google Pesquisar', result_type='recent', since_id=last_id)

def reply(content, tweetId):
    twiiter.update_with_media(status=content, filename='screenshot.png', in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)