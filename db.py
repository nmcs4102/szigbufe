# http://flask.pocoo.org/docs/1.0/tutorial/database/
import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('//var//www//html//FlaskApp//users.db')

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
	try:
		db = get_db()
	except:
		with open('/var/www/html/FlaskApp/schema.sql', 'r') as sql_file:
			sql_script = sql_file.read()
			db = sqlite3.connect('//var//www//html//FlaskApp//users.db')
		cursor = db.cursor()
		cursor.executescript(sql_script)
		db.commit()
		db.close()

def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)