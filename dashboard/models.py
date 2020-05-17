# -*- coding: utf-8 -*-

from dashboard import db


class Card(db.Model):
	__tablename__ = 'card'
	id = db.Column(db.Integer, primary_key=True)
	header = db.Column(db.String(20))
	icon = db.Column(db.String(10))
	category = db.Column(db.String(10))
	title = db.Column(db.String(12))
	footer_icon = db.Column(db.String(10))
	footer_title = db.Column(db.String(12))
	footer_text = db.Column(db.String(20))


class Employee(db.Model):
	__tablename__ = 'employee'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	country = db.Column(db.String(12))
	city = db.Column(db.String(12))
	salary = db.Column(db.Integer)


class Task(db.Model):
	__tablename__ = 'task'
	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(10))
	check = db.Column(db.Boolean)
	text = db.Column(db.Text)


class Upgrade(db.Model):
	__tablename__ = 'upgrade'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	free = db.Column(db.String(10))
	pro = db.Column(db.String(10))