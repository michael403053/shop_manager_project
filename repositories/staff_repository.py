from db.run_sql import run_sql
from models.staff import Staff

def save(staff):
    sql = "INSERT INTO staff (name, shift) VALUES (%s, %s) RETURNING id"
    values = [staff.name, staff.shift]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id

def select_all():
    staff = []
    sql = "SELECT * FROM staff"
    results = run_sql(sql)
    for result in results:
        new_staff = Staff(result["name"], result["shift"], result["id"])
        staff.append(new_staff)
    return staff

def select(id):
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    staff = Staff(result["name"], result["shift"], result["id"])
    return staff


def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(staff):
    sql = "UPDATE staff SET (name, shift) = (%s, %s) WHERE id = %s"
    values = [staff.name, staff.shift, staff.id]
    run_sql(sql, values)