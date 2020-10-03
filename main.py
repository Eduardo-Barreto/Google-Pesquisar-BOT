import twitter
import text
import screenshot
from time import sleep

tweets = twitter.getFirstTweet()
for tweet in tweets:
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
        else:
            pass
        print('-'*100)
        last_id = tweet.id

while True:

    tweets = twitter.getTweets()

    for tweet in tweets:
        read_last_tweets = open('./last_tweets.txt', 'r')
        last_tweets = open('./last_tweets.txt', 'a')
        if str(tweet.id) not in read_last_tweets:
            content = text.formatText(tweet)
            if 'google pesquisar' in content:
                content = content.replace('google pesquisar', '')
                if 'rt' not in content:
                    if content != '' and content != ' ':
                        print(content)
                        link = text.getLink(content)
                        print(link)
                        screenshot.get(link)
                        twitter.reply(content, tweet.id, link)
                else:
                    print('rt nao conta')
            else:
                pass
            print('-'*100)
            last_tweets.write('\n' + str(tweet.id))
            read_last_tweets.close()
            last_tweets.close()
