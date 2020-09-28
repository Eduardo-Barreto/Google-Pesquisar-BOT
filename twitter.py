import tweepy

import authkeys
auth = tweepy.OAuthHandler(authkeys.key1, authkeys.key2)
auth.set_access_token(authkeys.key3, authkeys.key4)

twiiter = tweepy.API(auth, wait_on_rate_limit=True)


def getFirstTweets():
    return twiiter.search(q='Google Pesquisar', result_type='recent', count=15)

def getTweets(last_id):
    return twiiter.search(q='Google Pesquisar', result_type='recent', since_id=last_id, count=30)

def reply(content, tweetId, url):
    twiiter.update_with_media(
        status=content+'\n\nsua pesquisa: '+url, 
        filename='screenshot.jpg', 
        in_reply_to_status_id=tweetId, 
        auto_populate_reply_metadata=True
    )