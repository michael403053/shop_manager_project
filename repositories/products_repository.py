from db.run_sql import run_sql
from models.staff import Staff
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturers_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buy_price, sell_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.stock_quantity, product.buy_price, product.sell_price, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id


def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for result in results:
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        product = Product(result["name"], result["description"], result["stock_quantity"], result["buy_price"], result["sell_price"], manufacturer, result["id"])
        products.append(product)
    return products


def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = manufacturer_repository.select(result["manufacturer_id"])
    product = Product(result["name"], result["description"], result["stock_quantity"], result["buy_price"], result["sell_price"], manufacturer, result["id"])
    return product


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM products WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(product):
#     sql = "UPDATE products SET (name, manufacturer_id) = (%s, %s) WHERE id = %s"
#     values = [product.name, product.manufacturer.id, product.id]
#     run_sql(sql, values)


# def select_staff_of_product(id):
#     staff = []
#     sql = "SELECT staff.* FROM staff INNER JOIN reciepts ON reciepts.staff_id = staff.id WHERE reciepts.product_id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     for result in results:
#         staff = Staff(result["name"])
#         staff.append(staff)
#     return staff