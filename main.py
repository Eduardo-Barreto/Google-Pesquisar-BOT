import os
from time import sleep

import twitter
import text
import screenshot


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print('pai ta on')

last_id = ''

sleep(5)
tweets = twitter.getFirstTweet()
for tweet in tweets:
    if tweet.author.screen_name != 'seu_google':
        if twitter.nao_foi(tweet.id):
            content = text.formatText(tweet)
            if 'google pesquisar' in content:
                if ('rt' not in content) and ('!q' not in content):
                    content = text.replaces(content)
                    if len(content) > 1:
                        print(content)
                        link = text.getLink(content)
                        print(link)
                        screenshot.get(link)
                        try:
                            twitter.reply(tweet.id, content, link)
                            print('\nrespondido com sucesso\n')
                        except:
                            print('\nprincipal suspensa')
                            try:
                                twitter.reserva_reply(
                                    tweet.id,
                                    content,
                                    link
                                )
                                print('respondido na reserva\n')
                            except:
                                print('reserva suspensa')
                                try:
                                    twitter.reserva2_reply(
                                        tweet.id,
                                        content,
                                        link
                                    )
                                    print('\nrespondido na reserva da reserva\n')
                                except:
                                    clear()
                                    print('eu nao aguento mais ser suspenso')

                        last_id = tweet.id
                        last_tweets = open('./last_tweets.txt', 'a')
                        last_tweets.write('\n' + str(tweet.id))
                        last_tweets.close()

while True:
    sleep(7)
    clear()
    print('mais uma leva de tweets')

    tweets = twitter.getTweets(last_id)

    for tweet in tweets:
        if tweet.author.screen_name != 'seu_google':
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
                                print('\nrespondido com sucesso\n')
                            except:
                                print('\nprincipal suspensa')
                                try:
                                    twitter.reserva_reply(
                                        tweet.id,
                                        content,
                                        link
                                    )
                                    print('\nrespondido na reserva\n')
                                except:
                                    print('\nprincipal suspensa')
                                    try:
                                        twitter.reserva2_reply(
                                            tweet.id,
                                            content,
                                            link
                                        )
                                        print('\nrespondido na reserva da reserva\n')
                                    except:
                                        clear()
                                        print(
                                            'eu nao aguento mais ser suspenso'
                                        )

                            last_tweets = open('./last_tweets.txt', 'a')
                            last_tweets.write('\n' + str(tweet.id))
                            last_tweets.close()

        last_id = tweet.id
