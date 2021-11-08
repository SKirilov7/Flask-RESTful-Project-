from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = 'Flask'
    context = {'name': name}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
