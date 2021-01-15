import imgkit
import os
from time import sleep


windows_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe'
raspi_path = '/usr/bin/wkhtmltoimage'


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
                    wkhtmltoimage=raspi_path
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

        except OSError:
            sleep(2)
            continue
