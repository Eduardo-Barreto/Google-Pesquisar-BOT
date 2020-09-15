import tweepy

import authkeys
auth = tweepy.OAuthHandler(authkeys.key1, authkeys.key2)
auth.set_access_token(authkeys.key3, authkeys.key4)

twiiter = tweepy.API(auth)


def getTweets():
    return twiiter.search(q='Google Pesquisar', result_type='recent')
