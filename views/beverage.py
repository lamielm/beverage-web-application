"""Beverage Views"""

from flask import flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.beverage import Beverage

engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()


def beverage_list_view():
    """Display a list of beverage from the database"""
    beverages = db_session.query(Beverage).all()

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_add_view():
    """Allow adding a new Beverage to the database"""

    # List to store any errors encountered
    errors = []

    if request.method == "POST":
        id_ = request.form["id"]
        name = request.form["name"]
        pack = request.form["pack"]
        price = request.form["price"]
        active = request.form["active"] == "true"

        if not id_:
            errors.append("The ID is required")
        elif db_session.query(Beverage).filter_by(id=id_).first():
            errors.append(f"A beverage with the ID {id_} already exists")
        if not name:
            errors.append("The name is required")
        if not pack:
            errors.append("The pack is required")
        if not price:
            errors.append("The price is required")
        if not active:
            errors.append("The status is required")

        

        if not errors:
            # Create the new Beverage
            new_beverage = Beverage(id_, name, pack, price, active)
            db_session.add(new_beverage)
            db_session.commit()

            flash("Beverage added successfully!", "success")

            return redirect(url_for("beverage_list_view"))

    # Return the form for adding a new beverage
    return render_template(
        "beverage/beverage_add.html",
        errors=errors,
    )


def beverage_edit_view(pk):
    """Allow editing an existing Beverage to the database"""

    # List to store any errors encountered
    errors = []

    beverage = db_session.get(Beverage, pk)

    if not beverage:
        flash(f"Unknown beverage with ID of {pk}", "danger")
        return redirect(url_for("beverage_list_view"))

    if request.method == "POST":
        name = request.form["name"]
        pack = request.form["pack"]
        price = request.form["price"]
        active = request.form["active"] == "true"

        if not name:
            errors.append("The name is required")
        if not pack:
            errors.append("The pack is required")
        if not price:
            errors.append("The price is required")
        if not active:
            errors.append("The status is required")

        if not errors:
            # Create the new Beverage
            beverage.name = name
            beverage.pack = pack
            beverage.price = price
            beverage.active = active

            db_session.commit()

            flash("Beverage updated successfully!", "success")

            return redirect(url_for("beverage_list_view"))

    # Return the form for adding a new beverage
    return render_template(
        "beverage/beverage_edit.html",
        beverage=beverage,
        errors=errors,
    )

def beverage_delete_view(pk):
    """Show page for deleting existing beverage"""
    errors = []

    beverage = db_session.get(Beverage, pk)

    if not beverage:
        flash(f"Unknown beverage with ID of {pk}", "danger")
        return redirect(url_for("beverage_list_view"))

    if request.method == "POST":
        db_session.delete(beverage)
        db_session.commit()

        flash("Beverage deleted seccessfully!", "success")

        return redirect(url_for("beverage_list_view"))

    return render_template(
        "beverage/beverage_delete.html",
        beverage=beverage,
        errors=errors,
    )