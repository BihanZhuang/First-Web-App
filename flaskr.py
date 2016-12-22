# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \render_template, flash

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# load default config and override config from an environment variable
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'flask.db'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)

def connect_bd():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.row_factory
    return rv
