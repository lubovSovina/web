from flask import Flask
i = 0
app = Flask(__name__)


@app.route('/i')
def show_i():
    global i
    i += 1
    return str(i)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')