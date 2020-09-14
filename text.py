from unicodedata import normalize

def formatText(tweet){
    text = normalize('NFKD', tweet.text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower()
    text = text.replace('google pesquisar' '')
    return text
}