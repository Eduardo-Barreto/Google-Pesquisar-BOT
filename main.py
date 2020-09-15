import twitter
import text

tweets = twitter.getTweets()

for tweet in tweets:
    content = text.formatText(tweet)
    if 'google pesquisar' in content:
        content = content.replace('google pesquisar', '')
        if 'rt' not in content:
            print(content)
        else:
            print('rt nao conta')
    else:
        pass
    print()