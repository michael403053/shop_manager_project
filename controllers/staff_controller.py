from flask import Blueprint, Flask, redirect, render_template, request

from models.staff import Staff
import repositories.staff_repository as staff_repository

staff_blueprint = Blueprint("staff", __name__)

# INDEX
@staff_blueprint.route("/staff")
def staff():
    staff = staff_repository.select_all()
    return render_template("staff/index.html", staff=staff)


# NEW
@staff_blueprint.route("/staff/new")
def new_staff():
    return render_template("staff/new.html")


# CREATE
@staff_blueprint.route("/staff", methods=["POST"])
def create_staff():
    name = request.form["name"]
    shift = request.form["shift"]
    new_staff = Staff(name, shift)
    staff_repository.save(new_staff)
    return redirect("/staff")


# EDIT
@staff_blueprint.route("/staff/<id>/edit")
def edit_staff(id):
    staff = staff_repository.select(id)
    return render_template('staff/edit.html', staff=staff)


# UPDATE
@staff_blueprint.route("/staff/<id>", methods=["POST"])
def update_staff(id):
    name = request.form["name"]
    shift = request.form["shift"]
    staff = Staff(name, id)
    staff_repository.update(staff)
    return redirect('/staff')


# DELETE
@staff_blueprint.route("/staff/<id>/delete", methods=["POST"])
def delete_staff(id):
    staff_repository.delete(id)
    return redirect("/staff")