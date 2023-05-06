from sqlalchemy.sql import text
from db import db
from flask import session, abort, request
from werkzeug.security import generate_password_hash, check_password_hash
import os

def login(username, password):
    sql = text("SELECT id, password, username FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user.password, password):
        return False
    session["user_id"] = user.id
    session["username"] = user.username
    session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["username"]
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("""
            INSERT INTO users (username, password)
            VALUES (:username, :password)
        """)
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def user_id():
    return session.get("user_id", 0)

def username():
    return session.get("username", 0)


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)