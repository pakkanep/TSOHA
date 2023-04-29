from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = text("SELECT C.name, C.location, C.size, C.price FROM cabins C WHERE C.availability=0")
    result = db.session.execute(sql)
    return result.fetchall()

def add_cabin(name, location, size, price, owner):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("""
    INSERT INTO cabins (name, location, size, price, owner, availability) 
    VALUES (:name, :location, :size, :price, :owner, 0)
    """)
    db.session.execute(sql, {"name":name, "location":location, "size":size, "price":price, "owner":owner, "availability":0})
    db.session.commit()
    return True

def remove_cabin(name, user):
    pass

def reserve_cabin(name, user):
    pass
