from unicodedata import normalize
from html import unescape
import pyshorteners
import pyshorteners.exceptions
from time import sleep
import re


def format(tweet):
    text = normalize('NFKD', tweet.text)
    text = text.encode('ASCII', 'ignore')
    text = text.decode('ASCII')
    text = text.lower()
    text = unescape(text)
    text = text.lower()

    text = text.strip()

    text = text.replace('\n', ' ')

    text = re.sub(
        r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)''' +
        r'''(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s(''' +
        r''')<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        '',
        text
    )

    text = text.replace('  ', ' ')

    mentions = tweet.entities.get('user_mentions')
    if mentions != []:
        for user in mentions:
            text = text.replace(user.get('screen_name').lower(), '')

    text = text.strip()

    return text


def replaces(text):
    to_replace = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
        '=', '"', ',', '?', '.', ':', '~', '>', '<', '{', '}', ';',
        ' google pesquisar', 'google pesquisar ', 'google pesquisar',
        'botpesquisar ', 'seugoogle ', 'botpesquisar', 'seugoogle'
    ]

    for item in to_replace:
        text = text.replace(item, '')

    text = text.strip()

    return text


def get_link(search):
    erros = (
        pyshorteners.exceptions.BadAPIResponseException,
        pyshorteners.exceptions.BadURLException,
        pyshorteners.exceptions.ExpandingErrorException,
        pyshorteners.exceptions.ShorteningErrorException
    )
    sucesso = False
    while not sucesso:
        search = search.replace(' ', '+')

        url = (
            'https://www.google.com/search?&q=' +
            search +
            '&ie=UTF-8&oe=UTF-8'
        )

        try:
            shorted = pyshorteners.Shortener()
            url = shorted.tinyurl.short(url)
            sucesso = True

        except erros:
            print('Erro ao pegar link')
            sleep(2)
            continue

    return url
