import imgkit
import os
from time import sleep


windows_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe'
# linux_path = '/usr/local/bin/wkhtmltoimage'
heroku_path = '/app/bin/wkhtmltoimage'


def get(url):
    sucesso = False
    while not sucesso:
        try:
            if os.name == 'nt':
                config = imgkit.config(
                    wkhtmltoimage=windows_path
                )
            else:
                config = imgkit.config(
                    wkhtmltoimage=heroku_path
                )

            options = {
                'format': 'jpg',
                'crop-h': '1230',
                'crop-w': '1440',
                'crop-x': '0',
                'crop-y': '0',
                'encoding': "UTF-8",
                'quiet': '',
            }

            imgkit.from_url(
                url,
                'screenshot.jpg',
                config=config,
                options=options
            )

            sucesso = True

        except OSError as e:
            print(e)
            sleep(2)
            continue
