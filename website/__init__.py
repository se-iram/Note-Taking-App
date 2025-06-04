# this is going to make website folder a python package
from flask import Flask

# create_app function is responsible for creating and configuring the Flask application instance
# The function returns the created Flask application instance, which can be used to define routes, views, and other application logic.

def create_app():
    # Flask(__name__)is constructor that creates an instance of the Flask class, which represents the web application.
    # The __name__ argument represents the name of the current module.

    app = Flask(__name__)
    # app.config is a dictionary-like object that stores configuration settings for the Flask application like the secret key, database connection details, and other application-specific configurations.
    # ['SECRET_KEY'] key is used by Flask for various purposes, such as signing cookies and protecting session data.
    app.config['SECRET_KEY'] = 'note taking app secret key 213'

    # Register the views and auth blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # url_prefix='/' means that all routes defined in the views and auth blueprints will be prefixed with this URL prefix.

    return app
