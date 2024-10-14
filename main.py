from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)