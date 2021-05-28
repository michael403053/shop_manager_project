from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
import repositories.manufacturers_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# INDEX
@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)


# NEW
@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    return render_template("manufacturers/new.html")


# CREATE
@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    contact = request.form["contact"]
    new_manufacturer = Manufacturer(name, contact)
    manufacturer_repository.save(new_manufacturer)
    return redirect("/manufacturers")


# EDIT
@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer=manufacturer)


# UPDATE
@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    contact = request.form["contact"]
    manufacturer = Manufacturer(name, contact, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')


# DELETE
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")