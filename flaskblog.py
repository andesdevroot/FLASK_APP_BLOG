from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Home Page</h1>'


# script para que siempre la app este en modo debugger

if __name__ == '__main__':
    app.run(debug=True)

