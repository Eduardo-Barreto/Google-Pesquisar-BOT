from unicodedata import normalize

def formatText(tweet):
    text = normalize('NFKD', tweet.text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.replace('@', '')
    text = text.lower()
    if 'http' in text:
        text = text[:text.find('http')]
    return text
