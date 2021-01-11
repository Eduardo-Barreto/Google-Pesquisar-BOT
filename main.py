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

tweets = twitter.getFirstTweet()
for tweet in tweets:
    if tweet.author.screen_name != 'seu_google':
        if twitter.nao_foi(tweet.id):
            content = text.formatText(tweet)
            if 'google pesquisar' in content:
                content = content.replace('google pesquisar', '')
                if ('rt' not in content) and ('!q' not in content):
                    if len(content) > 1:
                        print(content)
                        link = text.getLink(content)
                        print(link)
                        screenshot.get(link)
                        try:
                            twitter.reply(tweet.id, content, link)
                        except:
                            try:
                                twitter.reserva_reply(tweet.id, content, link)
                            except:
                                clear()
                                print('outro ban')

            last_id = tweet.id
            last_tweets = open('./last_tweets.txt', 'a')
            last_tweets.write('\n' + str(tweet.id))
            last_tweets.close()

while True:
    sleep(5)
    clear()
    print('mais uma leva de tweets')

    tweets = twitter.getTweets(last_id)

    for tweet in tweets:
        if tweet.author.screen_name != 'seu_google':
            if twitter.nao_foi(tweet.id):
                content = text.formatText(tweet)
                if 'google pesquisar' in content:
                    content = content.replace('google pesquisar', '')
                    if ('rt' not in content) and ('!q' not in content):
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
                                try:
                                    twitter.reserva_reply(
                                        tweet.id,
                                        content,
                                        link
                                    )
                                    print('\nrespondido na reserva\n')
                                except:
                                    clear()
                                    print('outro ban')

                            last_tweets = open('./last_tweets.txt', 'a')
                            last_tweets.write('\n' + str(tweet.id))
                            last_tweets.close()

        last_id = tweet.id
