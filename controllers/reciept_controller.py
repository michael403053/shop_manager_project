from flask import Blueprint, Flask, redirect, render_template, request

from models.reciept import Reciept
import repositories.reciept_repository as reciept_repository
import repositories.products_repository as products_repository
import repositories.staff_repository as staff_repository

reciepts_blueprint = Blueprint("reciepts", __name__)


# INDEX
@reciepts_blueprint.route("/reciepts")
def reciepts():
    reciepts = reciept_repository.select_all()
    return render_template("reciepts/index.html", reciepts=reciepts)

# NEW
@reciepts_blueprint.route("/reciepts/new")
def new_reciept():
    staffs = staff_repository.select_all()
    products = products_repository.select_all()
    return render_template("reciepts/new.html", staffs=staffs, products=products)


# CREATE
@reciepts_blueprint.route("/reciepts", methods=["POST"])
def create_reciept():
    product_id = request.form["product_id"]
    staff_id = request.form["staff_id"]
    time_stamp = request.form["time_stamp"]
    quantity = request.form["quantity"]
    product = products_repository.select(product_id)
    staff = staff_repository.select(staff_id)
    new_reciept = Reciept(product, staff, time_stamp, quantity)
    reciept_repository.save(new_reciept)
    return redirect("/reciepts")

# DELETE
@reciepts_blueprint.route("/reciepts/<id>/delete", methods=["POST"])
def delete_reciept(id):
    reciept_repository.delete(id)
    return redirect("/reciepts")
