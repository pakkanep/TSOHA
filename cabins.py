from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = text("SELECT name, location, size, price, year, availability FROM cabins")
    result = db.session.execute(sql)
    return result.fetchall()

def add_cabin(name, location, size, price, year):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = text("""
            INSERT INTO cabins (name, location, size, price, year, availability, owner_id) 
            VALUES (:name, :location, :size, :price, :year, 0, :owner)
        """)
        db.session.execute(sql, {
            "name":name,
            "location":location,
            "size":size,
            "price":price,
            "year":year,
            "availability":0,
            "owner":user_id
            })
        db.session.commit()
        return True
    except:
        return False

def remove_cabin(name):
    pass

def verify_owner(name):
    user_id = users.user_id()
    try:
        sql = text("SELECT owner_id FROM cabins WHERE name = :name")
        result = db.session.execute(sql, {"name":name})
        owner = result.fetchall()
    except:
        return False
    if owner == user_id:
        return True
    else:
        return False


def reserve_cabin(name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = text("""
            UPDATE cabins set availability = 1 WHERE name = :name;
        """)
        db.session.execute(sql, {"name":name})
        db.session.commit()
        return True
    except:
        return False
    
