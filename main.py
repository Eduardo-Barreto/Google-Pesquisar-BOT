import twitter
import text
import screenshot

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
                twitter.reply(content, tweet.id)
            else:
                print('rt nao conta')
        else:
            pass
        print()
        last_id = tweet.id

while True:
    tweets = twitter.getTweets(last_id)

    for tweet in tweets:
        content = text.formatText(tweet)
        if 'google pesquisar' in content:
            content = content.replace('google pesquisar', '')
            if 'rt' not in content:
                print(content)
                screenshot.get(content)
                twitter.reply(content, tweet.id)
            else:
                print('rt nao conta')
        else:
            pass
        print()
        last_id = tweet.id