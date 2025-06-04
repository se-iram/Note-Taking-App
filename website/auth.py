from flask import Blueprint, render_template, request, flash
# request is used to handle incoming requests like GET and POST
# render_template is used to render HTML templates 
# flash is used to display messages to the user, such as success or error messages
# Blueprint is used to organize routes and views in a Flask application
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
    # differentiate between GET and POST requests
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        firstname = data.get('firstName')
        lastname = data.get('lastName')
        password1 = data.get('password1')
        password2 = data.get('password2')

        # pythonn checks for validation of the data
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger') 
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='danger')
        elif len(lastname) < 2:
            flash('Last name must be greater than 1 character.', category='danger')
        elif (password1 != password2) & (password1 != '') & (password2 != ''):
            flash('Passwords don\'t match.', category='danger')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters long.', category='danger')
        else:
            # add user to a database
            flash('Account created successfully!', category='success')
        
    # message flashing is used to display messages to the user, such as success or error messages.

    return render_template('sign_up.html')

# GET and POST methods are used to handle different types of requests:
# - GET: Used to retrieve data from the server. In this case, it retrieves the login, logout, or sign-up page.
# - POST: Used to send data to the server, typically when submitting a form. In this case, it would handle form submissions for login or sign-up.
# data = request.form is used to access the data submitted in a form via POST request.
# The request.form object contains the form data as key-value pairs, allowing you to process user input.
# .form is a dictionary-like object that contains the data submitted in the form.
# request is an object that contains all the information about the current request, including form data, query parameters, and more.