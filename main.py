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
    if twitter.nao_foi(tweet.id):
        content = text.formatText(tweet)
        if 'google pesquisar' in content:
            content = content.replace('google pesquisar', '')
            if 'rt' not in content:
                if content != '':
                    print(content)
                    link = text.getLink(content)
                    print(link)
                    screenshot.get(link)
                    twitter.reply(tweet.id, content, link)

        last_id = tweet.id
        last_tweets = open('./last_tweets.txt', 'a')
        last_tweets.write('\n' + str(tweet.id))
        last_tweets.close()

while True:
    sleep(5)
    clear()
    print('mais uma leva de tweets')
    try:
        tweets = twitter.getTweets(last_id)

        for tweet in tweets:
            if tweet.author.screen_name != 'seu_google':
                if twitter.nao_foi(tweet.id):
                    content = text.formatText(tweet)
                    if 'google pesquisar' in content:
                        content = content.replace('google pesquisar', '')
                        if 'rt' not in content:
                            if content != '' and content != ' ':
                                print()
                                print(content)
                                link = text.getLink(content)
                                print(link)
                                screenshot.get(link)
                                twitter.reply(tweet.id, content, link)
                                last_tweets = open('./last_tweets.txt', 'a')
                                last_tweets.write('\n' + str(tweet.id))
                                last_tweets.close()

            last_id = tweet.id
    except:
        clear()
