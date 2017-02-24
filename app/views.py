from flask import render_template, flash, redirect, request
from app import app, db
from .forms import LoginForm
from config import POSTS_PER_PAGE

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'HyoJung'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("main.html",
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/home')
def home():
    return render_template("home2.html")

@app.route('/join', methods=['GET', 'POST'])
def join():
    return render_template("join.html",
                        title='Join membership')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['email'] != app.config['EMAIL']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            # session['logged_in'] = True
            # flash('You were logged in','normal')

            return redirect('/main2')

    return render_template("login.html",
                        title='Sign In',
                        error=error)

@app.route('/asset', methods = ['GET','POST'])
# @app.route('/asset/<int:id>', methods = ['GET','POST'])
def asset():
    return render_template("asset.html")

@app.route('/newhouse', methods=['GET', 'POST'])
def newhouse():
    if request.method == 'POST':
        return redirect('/asset')
    return render_template("newhouse.html")

@app.route('/newpet', methods=['GET', 'POST'])
def newpet():
    if request.method == 'POST':
        return redirect('/asset')
    return render_template("newpet.html")

@app.route('/viewsitter', methods=['GET', 'POST'])
def viewsitter():
    return render_template("viewsitter.html")

@app.route('/viewsitter2', methods=['GET', 'POST'])
def viewsitter2():
    return render_template("viewsitter2.html")



@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("search.html",
                        title='Search Petsitter')

@app.route('/search2', methods=['GET', 'POST'])
def search2():
    return render_template("search2.html",
                        title='Search Petsitter')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return redirect('/search')
    return render_template("main.html")

@app.route('/main2', methods=['GET', 'POST'])
def main2():
    if request.method == 'POST':
        return redirect('/search2')

    return render_template("main2.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/contact2')
def contact2():
    return render_template("contact2.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/about2')
def about2():
    return render_template("about2.html")

@app.route('/petsitter')
def petsitter():
    return render_template("petsitter.html")
