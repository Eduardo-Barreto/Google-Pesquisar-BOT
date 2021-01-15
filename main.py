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
print('Estou online')

last_id = ''

sleep(5)
tweets = twitter.getFirstTweet()
for tweet in tweets:
    if tweet.author.screen_name not in contas:
        if twitter.nao_foi(tweet.id):
            content = text.formatText(tweet)
            if 'google pesquisar' in content:
                if ('rt' not in content) and ('!q' not in content):
                    content = text.replaces(content)
                    if len(content) > 1:
                        print()
                        print(content)
                        link = text.getLink(content)
                        print(link)
                        screenshot.get(link)

                        try:
                            twitter.reply(tweet.id, content, link)
                            print('\nRespondido com sucesso\n')

                        except tweepy.TweepError:
                            print('\nConta principal suspensa')
                            try:
                                twitter.reserva_reply(
                                    tweet.id,
                                    content,
                                    link
                                )
                                print('\nRespondido na reserva\n')

                            except tweepy.TweepError:
                                print('\nConta reserva suspensa')
                                try:
                                    twitter.reserva2_reply(
                                        tweet.id,
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

while True:
    sleep(7)
    clear()
    print('Carregando tweets')

    tweets = twitter.getTweets(last_id)

    for tweet in tweets:
        if tweet.author.screen_name not in contas:
            if twitter.nao_foi(tweet.id):
                content = text.formatText(tweet)
                if 'google pesquisar' in content:
                    if ('rt' not in content) and ('!q' not in content):
                        content = text.replaces(content)
                        if len(content) > 1:
                            print()
                            print(content)
                            link = text.getLink(content)
                            print(link)
                            screenshot.get(link)

                            try:
                                twitter.reply(tweet.id, content, link)
                                print('\nRespondido com sucesso\n')

                            except tweepy.TweepError:
                                print('\nConta principal suspensa')
                                try:
                                    twitter.reserva_reply(
                                        tweet.id,
                                        content,
                                        link
                                    )
                                    print('Respondido na reserva\n')

                                except tweepy.TweepError:
                                    print('Conta reserva suspensa')
                                    try:
                                        twitter.reserva2_reply(
                                            tweet.id,
                                            content,
                                            link
                                        )
                                        print('respondido na' +
                                              ' reserva da reserva\n')

                                    except tweepy.TweepError:
                                        clear()
                                        print(
                                            'Todas as contas suspensas'
                                        )

                            last_tweets = open('./last_tweets.txt', 'a')
                            last_tweets.write('\n' + str(tweet.id))
                            last_tweets.close()

        last_id = tweet.id
