import webbrowser
import pyautogui
import time
from unicodedata import normalize


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
def getScreenshot(search):
    fds = search.replace(' ', '+')

    url = 'www.google.com/search?&q='+ fds+ '&ie=UTF-8&oe=UTF-8'

    webbrowser.get(chrome_path).open_new(url)

    time.sleep(5)

    myScreenshot = pyautogui.screenshot(region=(50, 110, 850, 1025))
    myScreenshot.save('screenshot.png')



def fetchText(tweet):
    texto = tweet.text
    texto = normalize('NFKD', tweet.text).encode('ASCII', 'ignore').decode('ASCII')
    texto = texto
    texto = texto.replace(':', '')
    texto = texto.replace(str(tweet.user.screen_name), '')
    texto = texto.strip('https://')
    return texto
