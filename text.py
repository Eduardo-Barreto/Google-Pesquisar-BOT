from unicodedata import normalize

def formatText(tweet):
    text = normalize('NFKD', tweet.text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.replace('@', '')
    text = text.lower()
    if 'http' in text:
        text = text[:text.find('http')]
    if '/n' in text:
        text = text[:text.find('/n')]
    return text

def getLink(search):
    search = search.replace(' ', '+')

    url = 'https://www.google.com/search?&q='+ search+ '&ie=UTF-8&oe=UTF-8'

    return url
