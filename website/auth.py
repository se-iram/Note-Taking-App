from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# login route
@auth.route('/login', methods=['GET', 'POST']) # accepting requests
def login():
    return render_template('login.html')

# logout route
@auth.route('/logout')
def logout():
    return render_template('logout.html')

# signup route
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')


