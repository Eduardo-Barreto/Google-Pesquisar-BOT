import os
from time import sleep
import tweepy

import twitter
import text
import screenshot


contas = ['seu_google', 'bot_pesquisar', 'GoogleReserva']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
sleep(5)

last_id = ''

print('Estou online')
first_tweet = twitter.get_first_tweet()
content = text.format(first_tweet)
if first_tweet.in_reply_to_status_id is None:
    if first_tweet.author.screen_name not in contas:
        if twitter.nao_foi(first_tweet.id):
            if ('rt' not in content) and ('!q' not in content):
                content = text.replaces(content)
                if len(content) > 1:
                    print(content)
                    link = text.get_link(content)
                    print(link)
                    screenshot.get(link)

                    try:
                        twitter.reply(first_tweet, content, link)
                        print('\nRespondido com sucesso\n')

                    except tweepy.TweepError:
                        print('\nConta principal suspensa')
                        try:
                            twitter.reserva_reply(
                                first_tweet,
                                content,
                                link
                            )
                            print('Respondido na reserva\n')

                        except tweepy.TweepError:
                            print('\nConta reserva suspensa')
                            try:
                                twitter.reserva2_reply(
                                    first_tweet,
                                    content,
                                    link
                                )
                                print('\nrespondido na' +
                                      ' reserva da reserva\n')

                            except tweepy.TweepError:
                                clear()
                                print(
                                    'Todas as contas suspensas'
                                )

                    last_id = first_tweet.id
                    last_tweets = open('./last_tweets.txt', 'a')
                    last_tweets.write('\n' + str(first_tweet.id))
                    last_tweets.close()


while True:
    tweets = twitter.get_tweets(last_id)
    for tweet in tweets:
        if tweet.in_reply_to_status_id is None:
            if tweet.author.screen_name not in contas:
                if twitter.nao_foi(tweet.id):
                    content = text.format(tweet)
                    if ('rt' not in content) and ('!q' not in content):
                        content = text.replaces(content)
                        if len(content) > 1:
                            print(content)
                            link = text.get_link(content)
                            print(link)
                            screenshot.get(link)

                            try:
                                twitter.reply(tweet, content, link)
                                print('\nRespondido com sucesso\n')

                            except tweepy.TweepError:
                                print('\nConta principal suspensa')
                                try:
                                    twitter.reserva_reply(
                                        tweet,
                                        content,
                                        link
                                    )
                                    print('Respondido na reserva\n')

                                except tweepy.TweepError:
                                    print('\nConta reserva suspensa')
                                    try:
                                        twitter.reserva2_reply(
                                            tweet,
                                            content,
                                            link
                                        )
                                        print('\nrespondido na' +
                                              ' reserva da reserva\n')

                                    except tweepy.TweepError:
                                        clear()
                                        print(
                                            'Todas as contas suspensas'
                                        )

                            last_id = tweet.id
                            last_tweets = open('./last_tweets.txt', 'a')
                            last_tweets.write('\n' + str(tweet.id))
                            last_tweets.close()
