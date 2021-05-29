from flask import Flask, render_template

from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.product_controller import products_blueprint
from controllers.reciept_controller import reciepts_blueprint


app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(reciepts_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()