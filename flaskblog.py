from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5a770abe765f4a8ea2b798f4d88b5bfd'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Cuenta Creada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    
   
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# script para que siempre la app este en modo debugger

if __name__ == '__main__':
    app.run(debug=True)






