import os
from flask import Flask,render_template, request, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies,jwt_required,JWTManager
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

jwt = JWTManager(app)

@app.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body