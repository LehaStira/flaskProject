from app import app
from flask import render_template


@app.route('/')
def index():
    my_str = 'Какой-то текст'
    return render_template('index.html', my_variable = my_str)