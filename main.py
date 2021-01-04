import os
from time import sleep

import twitter
import text
import screenshot

os.system('cls' if os.name == 'nt' else 'clear')

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
                    twitter.reply(content, tweet.id, link)
            else:
                print('rt nao conta')

        print('-'*10)
        last_id = tweet.id
        last_tweets = open('./last_tweets.txt', 'a')
        last_tweets.write('\n' + str(tweet.id))
        last_tweets.close()

while True:

    tweets = twitter.getTweets(last_id)

    for tweet in tweets:
        if twitter.nao_foi(tweet.id):
            content = text.formatText(tweet)
            if 'google pesquisar' in content:
                content = content.replace('google pesquisar', '')
                if 'rt' not in content:
                    if content != '' and content != ' ':
                        print(content)
                        link = text.getLink(content)
                        print(link)
                        screenshot.get(link)
                        twitter.reply(tweet.id, content, link)
                else:
                    print('rt nao conta')

            print('-'*10)
            last_id = tweet.id
            last_tweets = open('./last_tweets.txt', 'a')
            last_tweets.write('\n' + str(tweet.id))
            last_tweets.close()
