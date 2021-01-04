import imgkit
import os


def get(url):
    if os.name == 'nt':
        config = imgkit.config(
            wkhtmltoimage='C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe'
        )
    else:
        config = imgkit.config(
            wkhtmltoimage='/usr/bin/wkhtmltoimage'
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

    imgkit.from_url(url, 'screenshot.jpg', config=config, options=options)
