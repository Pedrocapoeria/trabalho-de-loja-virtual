from flask import Blueprint, render_template

user_bp = Blueprint("user", __name__)


@user_bp.route('login')
def login():
    return render_template('login.html')

@user_bp.route('/register')
def registro():
    return render_template('register.html')