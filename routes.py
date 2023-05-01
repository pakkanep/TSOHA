from app import app
from flask import render_template, request, redirect, flash
import cabins, users


@app.route("/")
def index():
    if not cabins.clear_old_reservations():
        return render_template("error.html", message="vanhojen varausten poistamisessa ongelma")
    cabinlist = cabins.get_list_free()
    reservedlist = cabins.get_list_reserved()
    return render_template(
        "index.html",
        count_free=len(cabinlist),
        cabins_free=cabinlist,
        count_reserved=len(reservedlist),
        cabins_reserved=reservedlist
        )

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/readreviews")
def showreviews():
    reviewlist = cabins.getreviews()
    if reviewlist == False:
        return render_template("error.html", message="Arvosteluja ei vielä ole")
    else:
        return render_template("showreviews.html", amount=len(reviewlist), reviews=reviewlist)


@app.route("/reserve", methods=["POST", "GET"])
def reserve():
    cabinlist = cabins.get_list_free()
    return render_template("reserve.html", count=len(cabinlist), cabins=cabinlist)


@app.route("/reservecabin", methods=["POST"])
def reserve_cabin():
    users.check_csrf()
    try:
        info = request.form["cabin"]
    except:
        return render_template("error.html", message="Mökin varaus epäonnistui")
    result = info.split(",")
    name = str(result[0])
    cabin_id = int(result[1])
    length = int(request.form["length"])
    if cabins.reserve_cabin(name) and cabins.add_reservation(cabin_id, length):
        return redirect("/")
    else:
        return render_template("error.html", message="Mökin vuokraaminen ei onnistunut")    


@app.route("/review", methods=["POST", "GET"])
def review():
    cabinlist = cabins.get_list_all()
    return render_template("review.html", count=len(cabinlist), cabins=cabinlist)


@app.route("/addreview", methods=["POST", "GET"])
def add_review():
    users.check_csrf()
    try:
        grade = request.form["grade"]
        cabin_id = request.form["cabin_id"]
        comment = request.form["comment"]
    except:
        return render_template("error.html", message="Arvostelun lisääminen ei onnistunut")
    if cabins.add_review(grade, cabin_id, comment):
        return redirect("/")
    else:
        return render_template("error.html", message="Arvostelun lisääminen ei onnistunut")

@app.route("/add", methods=["POST", "GET"])
def add_cabin():
    users.check_csrf()
    name = request.form["name"]
    location = request.form["location"]
    size = request.form["size"]
    price = request.form["price"]
    year = request.form["year"]
    
    if cabins.add_cabin(name, location, size, price, year):
        return redirect("/")
    else:
        return render_template("error.html", message="Mökin lisääminen ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "":
            return render_template("error.html", message="Käyttäjänimi puuttuu!")

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
        if len(username) < 3 or len(username) > 18:
            return render_template(
                "error.html",
                message="Käyttäjätunnuksen tulee olla 3-18 merkkiä pitkä"
                )        

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eivät täsmää")
        
        if len(password1) < 4 or len(password1) > 20:
            return render_template(
                "error.html",
                message="Salasanan pituus tulee olla 4-20 merkkiä pitkä"
                )

        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")