from functools import wraps
from flask import session, Blueprint, url_for, request, redirect, \
                  flash, render_template




users = Blueprint("users", __name__)

@users.route('/login')
def login():
    return render_template('login.html')

@users.route('/logout')
def logout():
    session.pop('recipe_token', None)
    return redirect(url_for('repos.index'))
