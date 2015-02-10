# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import mimetypes
from contextlib import closing

# db functions
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as db_schema:
			db.cursor().executescript(db_schema.read())
		db.commit()

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# configuration
DATABASE = '/tmp/flask_app.db'
DEBUG = True
SECRET_KEY = 'f2002barCal@'
USERNAME = 'admin'
PASSWORD = '3volusHun'

# the app - this gets imported into a run script and views
app = Flask(__name__)
# flask's config looks for upper case variables 
# and stashes them into a dict
app.config.from_object(__name__)
app.config.from_envvar('FLASKAPP_SETTINGS', silent=True)
app.debug = False
mimetypes.add_type('image/svg+xml', ',svg')

# import dependencies here after creating the app object. Yes,
# bad python, as it promotes circular imports

# view routes
import flaskapp.views

