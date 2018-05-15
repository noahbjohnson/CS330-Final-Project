from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Noah'}
    posts = [
        {
            'author': {'username':'Brad'},
            'body': 'Beautiful day in Decorah!'
        },
        {
            'author': {'username':'Paula'},
            'body': '''We're tripling tuition...'''
        },
        {
            'author': {'username':'Paula'},
            'body': '''Someone was racist again...'''
        },
        {
            'author': {'username':'Kent'},
            'body': '''All my office hours are canceled until 2020...'''
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)