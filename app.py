from flask import Flask, render_template

app = Flask(__name__)

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
def hello_world():  # put application's code here
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    #title sets the name at our tab in browser
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)
