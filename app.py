from flask import Flask, render_template, flash, redirect, url_for
import secret_key
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key.SECRET_KEY

posts = [
    {
        'author' : 'Ergi Kame',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'October 4, 2021'
    },
    {
        'author' : 'Ergi Kame',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'October 5, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    #title sets the name at our tab in browser
    return render_template("about.html", title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@flask.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
