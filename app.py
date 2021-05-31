from flask import Flask, render_template

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

@app.route("/")
def main():
    all_reciepts = reciept_repository.select_all()
    all_staff = staff_repository.select_all()
    all_products = product_repository.select_all()
    return render_template('index.html', all_reciepts=all_reciepts, all_staff=all_staff, all_products=all_products)

if __name__ == '__main__':
    app.run()