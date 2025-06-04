# this is going to store all of the main views or url end points for the actual 
# functioning kind of front end aspect of our website
# we are going to store standard routes for our website where users can go to
# and do things like login, register, etc
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# This is a blueprint in Flask, which is a way to organize routes and views in a modular fashion.
# Blueprints allow you to group related routes and views together, making it easier to manage larger applications.
# This blueprint can then be registered with the main Flask application instance, allowing the routes defined in this blueprint to be accessible.
# The views blueprint is typically used to define the main routes and views for the application, such as the home page, login page, and other user-facing pages.

# define first route
@views.route('/')
def home():
    return render_template('home.html')
# When a user accesses this URL, the home function is called, and it returns an HTML response with the text "Home Page" wrapped in <h1> tags.
# The @views.route decorator is used to associate the function with the specified URL path.
# Now we need to register this blueprint with the main Flask application instance in the create_app function or a similar setup function.
# This allows the routes defined in the views blueprint to be accessible when the application is run.


