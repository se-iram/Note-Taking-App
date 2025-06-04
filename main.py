# Here code run to start our webserver or start website
from website import create_app

app = create_app()

# this is going to run the app 
if __name__ == '__main__':
    app.run(debug=True)

# This is the main entry point of the application.
# It creates an instance of the Flask application by calling the create_app function from the website module.
# The app.run(debug=True) line starts the Flask development server with debug mode enabled, which provides helpful error messages and auto-reloads the server when code changes are made.
# This is useful for development purposes, as it allows you to see changes in real-time without manually restarting the server.
# The if __name__ == '__main__': block ensures that the app runs only when this script is executed directly, not when imported as a module.
# Flask development server allow you to access the application in your web browser.
