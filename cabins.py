from db import db
from sqlalchemy.sql import text
import users
from datetime import datetime, timedelta


def show_localities():
    sql = text("SELECT locality, amount FROM localities")
    result = db.session.execute(sql)
    return result.fetchall()


def clear_old_reservations():
    sql = text("SELECT cabin_id, start_date, end_date FROM reservations")
    result = db.session.execute(sql)
    dates = result.fetchall()
    for date in dates:
        if date[2] < datetime.now():
            release_cabin(date[0])


def release_cabin(cabin_id):
    sql = text("""
        UPDATE cabins set availability=0 WHERE id=:cabin_id;
    """)
    db.session.execute(sql, {"cabin_id":cabin_id})
    db.session.commit()

    sql = text("DELETE FROM reservations WHERE cabin_id=:cabin_id")
    db.session.execute(sql, {"cabin_id":cabin_id})
    db.session.commit()


def get_list_all():
    sql = text("""
        SELECT id, name, location, size, price, year, availability
        FROM cabins
    """)
    result = db.session.execute(sql)
    return result.fetchall()

def get_list_free():
    sql = text("""
        SELECT id, name, location, size, price, year, availability
        FROM cabins
        WHERE availability=0
    """)
    result = db.session.execute(sql)
    return result.fetchall()


def get_list_reserved():
    sql = text("""
        SELECT C.id, C.name, C.location, C.size, C.price,
        C.year, C.availability, R.start_date, r.end_date 
        FROM cabins C, reservations R
        WHERE C.id=R.cabin_id AND C.availability=1
    """)
    result = db.session.execute(sql)
    return result.fetchall()


def getreviews():
    sql = text("""
        SELECT R.comment, R.grade, U.username, C.name
        FROM reviews R, users U, cabins C
        WHERE R.user_id=U.id AND R.cabin_id=C.id
    """)
    result = db.session.execute(sql)
    return result.fetchall()
    

def add_review(grade, cabin_id, comment):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("""
        INSERT INTO reviews (user_id, cabin_id, comment, grade)
        VALUES (:user_id, :cabin_id, :comment, :grade)
    """)
    db.session.execute(sql, {
        "user_id":user_id,
        "cabin_id":cabin_id,
        "comment":comment,
        "grade":grade
    })
    db.session.commit()
    return True


def add_locality(locality):
    amount = get_one_locality(locality)
    if amount == []:
        sql = text("""
            INSERT INTO localities (locality, amount) VALUES (:locality, :amount)
        """)
        db.session.execute(sql, {"locality":locality, "amount":1})
        db.session.commit()
    else:
        add_locality_fail(locality, int(amount[0][0]))


def add_locality_fail(locality, amount):
    amount += 1
    sql = text("""
        UPDATE localities set amount = :amount WHERE locality = :locality
    """)
    db.session.execute(sql, {"amount":amount, "locality":locality})
    db.session.commit()


def get_one_locality(locality):
    sql = text("SELECT amount FROM localities WHERE locality=:locality")
    result = db.session.execute(sql, {"locality":locality})
    return result.fetchall()

def add_cabin(name, location, size, price, year):
    user_id = users.user_id()
    if user_id == 0:
        return False
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


def reserve_cabin(name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("""
        UPDATE cabins set availability=1 WHERE name=:name;
    """)
    db.session.execute(sql, {"name":name})
    db.session.commit()
    return True


def add_reservation(cabin_id, length):
    user_id = users.user_id()
    today = datetime.now()
    end_date = today + timedelta(days=length)
    if user_id == 0:
        return False

    sql = text("""
        INSERT INTO reservations (cabin_id, user_id, start_date, end_date)
        values(:cabin_id, :user_id, :today, :end_date) 
    """)
    db.session.execute(sql, {
            "cabin_id":cabin_id,
            "user_id":user_id,
            "today":today,
            "end_date":end_date
    })

    db.session.commit()
    return True

