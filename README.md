from random import randint
from flask import Flask, session, redirect, url_for, request
# from main_db_controll import db
# from db_scripts import get_question_after
form = '''&lt;form method="POST" acti&gt;
           Name: &lt;input type="text" name="name"&gt;
           &lt;input type="submit" value="Send"&gt;
           &lt;/form&gt;'''
def index():
   max_quiz = 3
   session['quiz'] = randint(1, max_quiz)
 
   session['last_question'] = 0
   return form
# f'''<a href="/test">Тест №{session['quiz']}</a>'''
 
 
 
def test():
   # result = get_question_after(session['last_question'], session['quiz'])
   # if result is None or len(result) == 0:  
   #         return redirect(url_for('result'))
   # else:
   #     session['last_question'] = result[0]
      #  якщо ми навчили базу повертати Row чи dict, то треба писати не result[0], а result['id']
       return '<h1>' + str(session['quiz']) + '<br>' + request.form.get('name') + '</h1>'
   # data = db.get_data(1)
   # return f'''<h1>Вы на странице тестирования</h1><a href="/result">Страница результата</a><p>{1}</p>'''
 
def result():
   return "that's all folks!"
 
 
 
# Створюємо об'єкт веб-програми:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/test', 'test', test, methods=['POST']) # створює правило для URL '/test'
app.add_url_rule('/result', 'result', result) # створює правило для URL '/test'
app.config['SECRET_KEY'] = 'secret_key'
 
if __name__ == '__main__':
  # Запускаємо веб-сервер:
  app.run(debug=True)
