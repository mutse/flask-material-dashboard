# -*- coding: utf-8 -*-

from flask import render_template, url_for, request

from dashboard import app, db, babel
from dashboard.models import Card, Employee, Task, Upgrade

from dashboard import cli

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match('zh_Hans')

@app.route('/')
def index():
	cards = Card.query.all()
	employees = Employee.query.all()
	tasks = Task.query.all()
	return render_template('index.html', cards=cards, employees=employees, tasks=tasks)

@app.route('/user')
def user():
	return render_template('user.html')

@app.route('/tables')
def tables():
	employees = Employee.query.all()
	return render_template('tables.html', employees=employees)

@app.route('/typography')
def typography():
	return render_template('typography.html')

@app.route('/icons')
def icons():
	return render_template('icons.html')

@app.route('/notifications')
def notifications():
	return render_template('notifications.html')

@app.route('/rtl')
def rtl():
	return render_template('rtl.html')

@app.route('/upgrade')
def upgrade():
	items = Upgrade.query.all()
	return render_template('upgrade.html', items = items)