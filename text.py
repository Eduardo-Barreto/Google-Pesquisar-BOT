from unicodedata import normalize
from html import unescape
import pyshorteners


def formatText(tweet):
    text = normalize('NFKD', tweet.text)
    text = text.encode('ASCII', 'ignore')
    text = text.decode('ASCII')
    text = text.lower()
    text = unescape(text)

    text = text.strip()

    to_replace = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
        '=', '"', ',', '?', '.', ':', '~', '>', '<', '{', '}', ';',
        'botpesquisar ', 'seugoogle ', 'botpesquisar', 'seugoogle'
    ]

    for item in to_replace:
        text = text.replace(item, '')

    text = text.strip()

    if 'http' in text:
        text = text[:text.find('http')]
    text = text.replace('\n', '')

    mentions = tweet.entities.get('user_mentions')
    if mentions != []:
        for user in mentions:
            text = text.replace(user.get('screen_name').lower(), '')

    text = text.strip()
    return text


def getLink(search):
    search = search.replace(' ', '+')

    url = 'https://www.google.com/search?&q=' + search + '&ie=UTF-8&oe=UTF-8'

    shorted = pyshorteners.Shortener()
    url = shorted.tinyurl.short(url)

    return url
