from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', 
                                  filename='img/riana.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')