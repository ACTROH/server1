from random import randint
from flask import Flask, session, redirect, url_for


def index():
    max_quiz = 3
    session['quiz'] = randint(1,max_quiz)

    session['last_question'] = 0
    return f'''<a href="/test">Тест №{session['quiz']}</a>'''

def test():
    return '<h1>ok</h1><a href="/result">Тест</a>'

def result():
    return "that's all folks!"



app = Flask(__name__)
app.add_url_rule('/','index', index)
app.add_url_rule('/test','test',test)
app.add_url_rule('/result','result',result)
app.config['SECRET_KEY'] = 'secret_key'



if __name__ == '__main__':
    app.run(debug=True)