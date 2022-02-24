""" This module implements a Flask application using Redis as persistent storage. """

from flask import Flask, render_template, request
from flask_redis import FlaskRedis

# Create flask instance
app = Flask(__name__)
app.config['REDIS_URL'] = "redis://redis:6379/0"

# Create Redis client
redis_client = FlaskRedis(app)


@app.route("/")
def home():
    """
    Renders the welcome page.
    """
    # Check if the user has already visited the page
    username = redis_client.get(request.remote_addr)

    if username:
        # Render the welcomeback page
        return render_template('welcomeback.html', value=str(username, 'utf8'))
    else:
        # Render the welcome page
        return render_template('welcome.html')


@app.route("/greeting", methods=['POST'])
def greeting():
    """Persist the username and show the greeting page."""
    # Get the username from the form
    username = request.form['username']

    if username:
        # Persist the username + ip address
        redis_client.set(request.remote_addr, str(bytes(username, 'utf-8'), 'utf-8'))

        # Render the greeting template passing the username
        return render_template('greeting.html', value=username)
    else:
        # Render the welcome page
        return render_template('welcome.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
