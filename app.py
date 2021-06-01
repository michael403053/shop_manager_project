from flask import Flask, render_template
from jinja2 import Environment, meta
from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.product_controller import products_blueprint
from controllers.reciept_controller import reciepts_blueprint
import repositories.reciept_repository as reciept_repository
import repositories.staff_repository as staff_repository
import repositories.products_repository as product_repository

app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(reciepts_blueprint)

# def all_staff_wages():
#     all_staff = staff_repository.select_all()
#     total_wages = 0
#     for staff_member in all_staff:
#         total_wages += (staff_member.shift * 9.70)
#     return total_wages

@app.route("/")
def main():
    all_reciepts = reciept_repository.select_all()
    all_staff = staff_repository.select_all()
    all_products = product_repository.select_all()
    total_markup = 0
    total_wages = 0
    for reciept in all_reciepts:
        total_markup += ((reciept.product.sell_price - reciept.product.buy_price) * reciept.quantity)   
    for staff_member in all_staff:
        total_wages += (staff_member.shift * 9.70)   
    return render_template('index.html', all_reciepts=all_reciepts, all_staff=all_staff, all_products=all_products, total_markup=total_markup, total_wages=total_wages)

if __name__ == '__main__':
    app.run()