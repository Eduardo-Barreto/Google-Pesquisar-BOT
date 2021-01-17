import tweepy
from datetime import datetime

import authkeys

# Conta Principal
auth = tweepy.OAuthHandler(
    authkeys.key1,
    authkeys.key2
)
auth.set_access_token(
    authkeys.key3,
    authkeys.key4
)
twiiter = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True
)

# Conta Reserva
auth_reserva = tweepy.OAuthHandler(
    authkeys.reserva_key1,
    authkeys.reserva_key2
)
auth_reserva.set_access_token(
    authkeys.reserva_key3,
    authkeys.reserva_key4
)
reserva = tweepy.API(
    auth_reserva,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True
)

# Conta Reserva
auth_reserva2 = tweepy.OAuthHandler(
    authkeys.reserva2_key1,
    authkeys.reserva2_key2
)
auth_reserva2.set_access_token(
    authkeys.reserva2_key3,
    authkeys.reserva2_key4
)
reserva2 = tweepy.API(
    auth_reserva2,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True
)


def getFirstTweet():
    agora = datetime.now().strftime('%Y-%m-%d')
    return tweepy.Cursor(
        twiiter.search,
        q='google pesquisar',
        since=agora
    ).items(1)


def getTweets(last_id):
    return reversed(list(tweepy.Cursor(
        twiiter.search,
        q='google pesquisar',
        since_id=last_id
    ).items(15)))


def reply(tweet, content, url):
    author = tweet.author.screen_name
    twiiter.update_with_media(
        status=f'@{author} {content}\n\nlink para a sua pesquisa: {url}',
        filename='screenshot.jpg',
        in_reply_to_status_id=tweet.id,
    )


def reserva_reply(tweet, content, url):
    author = tweet.author.screen_name
    reserva.update_with_media(
        status=f'@{author} {content}\n\nlink para a sua pesquisa: {url}',
        filename='screenshot.jpg',
        in_reply_to_status_id=tweet.id,
    )


def reserva2_reply(tweet, content, url):
    author = tweet.author.screen_name
    reserva2.update_with_media(
        status=f'@{author} {content}\n\nlink para a sua pesquisa: {url}',
        filename='screenshot.jpg',
        in_reply_to_status_id=tweet.id,
    )


def nao_foi(tweet_id):
    read_last_tweets = open('./last_tweets.txt', 'r')

    for linha in read_last_tweets:
        if str(tweet_id) in linha:
            read_last_tweets.close()
            return False

    read_last_tweets.close()
    return True
