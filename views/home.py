"""Home and static views"""

# Landon Lamie
# CIS 226
# 12/11/2024

# Third-party imports
from flask import render_template


def home_view():
    """Home View"""
    return render_template("home.html")


def contact_view():
    """Contact View"""
    return render_template("contact.html")