"""Tiny Flask Example

From https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

Requires you to install flask in your virtual environment:

  $ . .venv/Scripts/activate

  $ python -m pip install flask

To run this on windows:

  Activate your environment if you haven't already.

  $ flask --app main run --debug

Then in a browser go to http://127.0.0.1:5000/
"""
from flask import Flask

# First party imports
from views.home import (
    home_view,
    contact_view,
)

from views.beverage import (
    beverage_list_view,
    beverage_add_view,
    beverage_edit_view,
    beverage_delete_view,
)

app = Flask(__name__)

# Define the secret key for use with cookies and the session
app.secret_key = b"CIwdcuCtI9PSC--DhkWjk1ACPNzUoy3Vb2avY9k322c"


# Define the routes for the app
app.add_url_rule("/", view_func=home_view)
app.add_url_rule("/contact", view_func=contact_view)
app.add_url_rule("/beverages", view_func=beverage_list_view)
app.add_url_rule("/beverages/add", view_func=beverage_add_view, methods=["GET", "POST"])
app.add_url_rule("/beverage/<string:pk>/edit", view_func=beverage_edit_view, methods=["GET", "POST"])
app.add_url_rule("/beverage/<string:pk>/delete", view_func=beverage_delete_view, methods=["GET", "POST"])