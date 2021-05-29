from db.run_sql import run_sql
from models.reciept import Reciept
from models.staff import Staff
import repositories.staff_repository as staff_repository
from models.product import Product
import repositories.products_repository as products_repository

def save(reciept):
    sql = "INSERT INTO reciepts (product_id, staff_id, time_stamp, quantity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [reciept.product.id, reciept.staff.id, reciept.time_stamp, reciept.quantity]
    print(values)
    results = run_sql(sql, values)    
    id = results[0]['id']
    reciept.id = id

def select(id):
    sql = "SELECT * FROM reciepts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    product = products_repository.select(result["product_id"])
    staff = staff_repository.select(result["staff_id"])
    time_stamp = result["time_stamp"]
    quantity = result["quantity"]
    reciept = Reciept(product, staff, time_stamp, quantity, result["id"])
    return reciept

def select_all():
    reciepts = []
    sql = "SELECT * FROM reciepts"
    results = run_sql(sql)
    for result in results:
        product = products_repository.select(result["product_id"])
        staff = staff_repository.select(result["staff_id"])
        reciept = Reciept(product, staff, result["time_stamp"], result["quantity"], result["id"])
        reciepts.append(reciept)
    return reciepts

def delete(id):
    sql = "DELETE FROM reciepts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(reciept):
    sql = "UPDATE reciepts SET (product_id, staff_id, time_stamp, quantity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [reciept.product.id, reciept.staff.id, reciept.time_stamp, reciept.quantity, reciept.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM reciept"
    run_sql(sql)