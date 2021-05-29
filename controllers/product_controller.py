from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.products_repository as product_repository
import repositories.manufacturers_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

# INDEX
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)


# SHOW
@products_blueprint.route("/products/<id>")
def show_product(id):
    victims = product_repository.select_victims_of_product(id)
    product = product_repository.select(id)
    return render_template("products/show.html", victims=victims, product=product)


# NEW
@products_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", manufacturers=manufacturers)


# CREATE
@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buy_price = request.form["buy_price"]
    sell_price = request.form["sell_price"]
    manufacturer_id = request.form["manufacturer_id"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    new_product = Product(name, description, stock_quantity, buy_price, sell_price, manufacturer)
    product_repository.save(new_product)
    return redirect("/products")


# EDIT
@products_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product=product, manufacturers=manufacturers)


# UPDATE
@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buy_price = request.form["buy_price"]
    sell_price = request.form["sell_price"]
    manufacturer_id = request.form["manufacturer_id"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buy_price, sell_price, manufacturer)
    product_repository.update(product)
    return redirect("/products")


# DELETE
@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")
