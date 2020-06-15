from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Cesar rivas',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Abril'
    },
    {
        'author': 'Carlos',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Mayo'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# script para que siempre la app este en modo debugger

if __name__ == '__main__':
    app.run(debug=True)


