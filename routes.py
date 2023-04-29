from app import app
from flask import render_template, request, redirect
import cabins, users

@app.route("/")
def index():
    
    cabinlist = cabins.get_list()
    return render_template("index.html", count=len(cabinlist), cabins=cabinlist)

@app.route("/new")
def new():
    
    return render_template("new.html")

@app.route("/reserve", methods=["POST", "GET"])
def reserve():
    
    cabinlist = cabins.get_list()
    return render_template("reserve.html", cabins=cabinlist)


@app.route("/reservecabin", methods=["POST", "GET"])
def reserve_cabin():
    name = request.form["cabin"]
    user = users.user_id()
    if cabins.reserve_cabin(name, user):
        return redirect("/")
    else:
        return render_template("error.html", message="Mökin vuokraaminen ei onnistunut")    


@app.route("/add", methods=["POST", "GET"])
def add_cabin():
    print("ollaan /add")
    name = request.form["name"]
    location = request.form["location"]
    size = request.form["size"]
    price = request.form["price"]
    owner = request.form["owner"]
    if cabins.add_cabin(name, location, size, price, owner):
        return redirect("/")
    else:
        return render_template("error.html", message="Mökin lisääminen ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    print("ollaaan /login")
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")