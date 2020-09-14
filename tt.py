import pyautogui
import config
import tweepy
import autenticacao
import webbrowser

auth = tweepy.OAuthHandler(autenticacao.key1, autenticacao.key2)
auth.set_access_token(autenticacao.key3, autenticacao.key4)

api = tweepy.API(auth)

resultados = api.search(q='Google Pesquisar', result_type='recent') #

for tweet in resultados:
    if tweet.user.id ==1002540619653439488:
        api.update_status(status='vo te responde nao mane', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    else:
        texto = config.fetchText(tweet)
        
        if 'google pesquisar' in texto or 'pesquisar google' in texto:
            texto = tweet.text.replace(' google pesquisar ', '').lower()
            texto = texto.replace(' pesquisar google ', '').lower()
            print(f'texto: {texto}')
            print(type(texto))
            if 'rt ' not in texto and 'RT ' not in texto:
                if texto != '':
                    print('ok')
                    config.getScreenshot(texto)
                    api.update_with_media(status=texto, filename='screenshot.png', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                    pyautogui.hotkey('Ctrl','w')
        else:
            pass
print('fim')
pyautogui.hotkey('Alt','Tab')
