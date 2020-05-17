# -*- coding: utf-8 -*-

from flask import render_template, url_for, request

from pyecharts import options as opts
from pyecharts.charts import Pie
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

from dashboard import app, db, babel
from dashboard.models import Card, Employee, Task, Upgrade

from dashboard import cli

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("templates"))

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match('zh_Hans')

@app.route('/')
def index():
	cards = Card.query.all()
	employees = Employee.query.all()
	tasks = Task.query.all()
	return render_template('index.html', cards=cards, employees=employees, tasks=tasks)

@app.route('/pie')
def draw_pie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 =[19, 21, 32, 20, 20, 33]
    pie = (
        Pie()
            .add("商品B", [list(v) for v in zip(attr, v2)], center=[300, 260], radius=[100, 180], rosetype='radius')
        )
    return pie.dump_options_with_quotes()

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