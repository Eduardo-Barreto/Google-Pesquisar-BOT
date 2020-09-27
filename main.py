import twitter
import text
import screenshot
from time import sleep

tweets = twitter.getFirstTweets()
for tweet in tweets:
        content = text.formatText(tweet)
        if 'google pesquisar' in content:
            content = content.replace('google pesquisar', '')
            if 'rt' not in content:
                print(content)
                link = text.getLink(content)
                print(link)
                screenshot.get(link)
                twitter.reply(content, tweet.id, link)
                last_id = tweet.id
            else:
                print('rt nao conta')
        else:
            pass
        print('-'*50)

while True:
    tweets = twitter.getTweets(last_id)

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
                    last_id = tweet.id
            else:
                print('rt nao conta')
        else:
            pass
        print('-'*50)