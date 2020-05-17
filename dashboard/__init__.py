# -*- coding: utf-8 -*-

import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, gettext as _

app = Flask(__name__)

win = sys.platform.startswith('win')
prefix = 'sqlite:///' if win else 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data/data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)

db = SQLAlchemy(app)

from dashboard import views