from db.run_sql import run_sql
from models.reciept import Reciept



def delete_all():
    sql = "DELETE FROM reciept"
    run_sql(sql)