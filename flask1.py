from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return "Главная страничка"


@app.route('/users/<int:uid>')
def profile(uid):
    print(uid)
    print(type(uid))
    return ""


@app.route('/feed/')
def page_feed():
    return "Лента пользователя"


@app.route('/messages/')
def page_messages():
    return "Сообщения пользователя"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.21', port=800)