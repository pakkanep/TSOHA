from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, url_for, flash
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:YdR3AG88Qm@localhost:5432/postgres"

db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT name FROM cabins"))
    cabins = result.fetchall()
    return render_template("index.html", count=len(cabins), cabins=cabins) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        flash("Signed in")
        return redirect(url_for("redirect_"))
    else:
        return render_template("login.html")

@app.route("/new_user", methods = ["POST", "GET"])
def new_user():
    return render_template("new_user.html")

@app.route("/redirect_", methods = ["POST", "GET"])
def redirect_():
    return redirect(url_for("index"))

@app.route("/haku")
def haku():
    return render_template("haku.html")

@app.route("/result", methods = ["POST"])
def result():
    location = request.form.getlist("location")
    count = len(request.form.getlist("location"))
    ehto = location[0]
    sql = text("SELECT name FROM cabins WHERE name = :ehto")
    result = db.session.execute(sql, {"ehto":ehto})
    
    cabins = result.fetchall()
    
    return render_template("result.html", locations=location, count=count, cabins=cabins)
    

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    sql = text("INSERT INTO cabins (name) VALUES (:name)")
    db.session.execute(sql, {"name":name})
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run()
