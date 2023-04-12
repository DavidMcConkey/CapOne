import os
from flask import Flask,render_template, request, redirect, session, abort
from flask_debugtoolbar import DebugToolbarExtension

from models import db,connect_db
CURR_USER_KEY = 'curr_user'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL','postgresql:///placeholder'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretsecretsecret')
toolbar = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)