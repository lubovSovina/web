from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/sample_page')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')