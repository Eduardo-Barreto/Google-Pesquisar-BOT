import tweepy

import authkeys
auth = tweepy.OAuthHandler(autenticacao.key1, autenticacao.key2)
auth.set_access_token(autenticacao.key3, autenticacao.key4)

twiiter = tweepy.API(auth)


def getTweets(){
    return twitter.search(q='Google Pesquisar', result_type='recent')
}

