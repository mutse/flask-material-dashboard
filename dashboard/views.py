# -*- coding: utf-8 -*-

from flask import render_template, url_for

from dashboard import app


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user')
def user():
	return render_template('user.html')

@app.route('/tables')
def tables():
	return render_template('tables.html')

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
	return render_template('upgrade.html')