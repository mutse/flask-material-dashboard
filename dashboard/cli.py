# -*- coding: utf-8 -*-

import os
import click

from dashboard import app, db
from dashboard.models import Card, Employee, Task, Upgrade

@app.cli.command('db')
@click.option('--drop', is_flag=True, help='Create database tables after drop.')
@click.option('--update', is_flag=True, help='Update database tables from data.')
def database(drop, update):
	"""Initialized database."""
	if drop:
		db.drop_all()
		db.create_all()
		click.echo('database tables initialized.')

	if update:
		update_cards()
		click.echo('update table card ok.')
		update_employees()
		click.echo('update table employee ok.')
		update_tasks()
		click.echo('update tasks ok.')
		update_upgrade()
		click.echo('update upgrade items ok.')

def update_cards():
	datas = [('card-header-warning', 'content_copy', 'Used Space', '49/50', 'text-danger', 'warning', 'Get More Space...'),
			('card-header-success', 'store', 'Revenue', '$3,424', ' ', 'date_range', ' Last 24 Hours'),
			('card-header-danger', 'info_outline', 'Fixed Issues', '75', ' ', 'local_offer', ' Tracked from Github'),
			('card-header-info', '', 'Followers', '+245', ' ', 'update', ' Just Updated')]
	for data in datas:
		card = Card(header=data[0], icon=data[1], category=data[2], title=data[3],
			footer_icon=data[4], footer_title=data[5], footer_text=data[6])
		db.session.add(card)
	db.session.commit()

def update_employees():
	datas = [('Dakota Rice', 'Niger', 'Oud-Turnhout', 36738),
			('Minerva Hooper', 'Curaçao', 'Sinaai-Waas', 23789),
			('Sage Rodriguez', 'Netherlands', 'Baileux', 56142),
			('Philip Chaney', 'Korea, South', 'Overland Park', 38735),
			('Doris Greene', 'Malawi', 'Feldkirchen in Kärnten', 63542),
			('Mason Porter', 'Chile', 'Gloucester', 78615)]
	for data in datas:
		employ = Employee(name=data[0], country=data[1], city=data[2], salary=data[3])
		db.session.add(employ)
	db.session.commit()

def update_tasks():
	datas = [('profile', True, 'Sign contract for "What are conference organizers afraid of?"'),
			('profile', False, 'Lines From Great Russian Literature? Or E-mails From My Boss?'),
			('profile', False, 'Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit'),
			('profile', True, 'Create 4 Invisible User Experiences you Never Knew About'),
			('messages', True, 'Sign contract for "What are conference organizers afraid of?"'),
			('messages', False, 'Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit'),
			('settings', False, 'Lines From Great Russian Literature? Or E-mails From My Boss?'),
			('settings', False, 'Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit'),
			('settings', True, 'Sign contract for "What are conference organizers afraid of?"')]
	for data in datas:
		task = Task(category=data[0], check=data[1], text=data[2])
		db.session.add(task)
	db.session.commit()

def update_upgrade():
	datas = [('Components', '60', '200'),
			('Plugins', '2', '15'),
			('Example Pages', '3', '27'),
			('Login, Register, Pricing, Lock Pages', 'danger', 'success'),
			('DataTables, VectorMap, SweetAlert, Wizard, jQueryValidation, FullCalendar etc...', 'danger', 'success'),
			('Mini Sidebar', 'danger', 'success'),
			('Premium Support', 'danger', 'success'),
			('', 'Free', 'Just $49')]
	for data in datas:
		upgrade = Upgrade(title=data[0], free=data[1], pro=data[2])
		db.session.add(upgrade)
	db.session.commit()

@app.cli.command('lang')
@click.option('--init', is_flag=True, help='Initialized locale pot file.')
@click.option('--generate', is_flag=True, help='Generate locale po file')
@click.option('--update', is_flag=True, help='Update locale po file.')
@click.option('--compile', is_flag=True, help='Compile locale po file.')
def locale(init, generate, update, compile):
	"""Extract locale from source."""
	if init:
		init_locale()

	if generate:
		gen_po()

	if update:
		update_po()

	if compile:
		compile_mo()

def init_locale():
	cfg = os.path.join(app.root_path, 'babel.cfg')
	pot = os.path.join(app.root_path, 'translations/messages.pot')
	os.system('pybabel extract -F {0} -o {1} .'.format(cfg, pot))
	click.echo('messages.pot generated in translations.')

def gen_po():
	i18n_dir = os.path.join(app.root_path, 'translations')
	pot = os.path.join(app.root_path, 'translations/messages.pot')
	os.system('pybabel init -i {0} -d {1} -l zh_Hans'.format(pot, i18n_dir))
	click.echo('messages.po generated in translations.')

def update_po():
	i18n_dir = os.path.join(app.root_path, 'translations')
	pot = os.path.join(app.root_path, 'translations/messages.pot')
	os.system('pybabel update -i {0} -d {1}'.format(pot, i18n_dir))
	click.echo('messages.po updated in translations.')

def compile_mo():
	i18n_dir = os.path.join(app.root_path, 'translations')
	os.system('pybabel compile -d {0}'.format(i18n_dir))
	click.echo('messages.mo generated in translations.')