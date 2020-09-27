from unicodedata import normalize
import pyshorteners

def formatText(tweet):
    text = normalize('NFKD', tweet.text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.replace('@', '')
    text = text.lower()
    if 'http' in text:
        text = text[:text.find('http')]
    text = text.replace('\n', '')

    mentions = tweet.entities.get('user_mentions')
    if mentions != []:
        for user in mentions:
            text = text.replace(user.get('screen_name'), '')

    return text

def getLink(search):
    search = search.replace(' ', '+')

    url = 'https://www.google.com/search?&q='+ search+ '&ie=UTF-8&oe=UTF-8'
    
    xorx = pyshorteners.Shortener()
    url = xorx.tinyurl.short(url)

    return url
