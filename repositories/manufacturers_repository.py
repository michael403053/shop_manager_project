from db.run_sql import run_sql
from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, contact) VALUES (%s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for result in results:
        manufacturer = Manufacturer(result["name"], result["contact"], result["id"])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    manufacturer = Manufacturer(result["name"], result["contact"], result["id"])
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, contact) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.contact, manufacturer.id]
    run_sql(sql, values)