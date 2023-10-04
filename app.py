# pip3 freeze > requirements.txt

from flask import Flask, render_template, flash, request, redirect

from datetime import datetime as dt

from models.user import User
from models.db_base import students

app = Flask(__name__)
app.secret_key = r'\xf9\xc0\x1c09\xf2c\x19\xec/\x1eX\x1fX\xd5\x8a^\x06\xa0&'


@app.route('/')
def index():
    user = User()
    return render_template('index.html', user=user)


@app.route('/Скуд', methods=['GET', 'POST'])
def skud_activate():
    if request.method == 'POST':
        daytime_filter = request.form.get('month')
        if not daytime_filter:
            flash('Выберите месяц для отчета', 'error')
    return render_template('skud_menu.html', max_date=dt.now().month)


@app.errorhandler(404)
def page_not_found(e):
    flash('Страница еще не придумана!!! КУДА ТЫ ЖМЕШЬ???', 'error')
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run()
