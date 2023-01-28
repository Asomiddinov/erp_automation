from __init__ import app, db
from flask import render_template, request, flash, redirect, url_for
from forms import QRCodeData, Mine, User
import secrets
import qrcode
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home Page")


@app.route("/info")
def layout():
    return render_template("info.html")


@app.route("/generator", methods=["GET", "POST"])
def generator():
    form = QRCodeData()
    if request.method == "POST":
        if form.validate_on_submit():
            dat = form.dat.data
            image_name = f"{secrets.token_hex(10)}.png"
            qrcode_location = f"{app.config['UPLOAD_PATH']}/{image_name}"
            try:
                my_qrcode = qrcode.make(
                    str(dat)).save(qrcode_location)
            except Exception as e:
                print(e)
            return render_template("generated.html", title="Generated 🔢", image=image_name)
    else:
        return render_template("generator.html", title="🔢", form=form)


@app.route("/mine", methods=["GET", "POST"])
def mine():
    form = Mine()
    client = form.client.data
    address = form.address.data
    quantity = form.quantity.data
    mark = form.mark.data
    price = form.price.data
    currency = form.currency.data
    paid = form.paid.data
    driver = form.driver.data
    date = form.date.data
    approve = form.approve.data
    return render_template("act.html", form=form, client=client, address=address, quantity=quantity, mark=mark, price=price, currency=currency, paid=paid, driver=driver, date=date, approve=approve)


@app.route("/acted", methods=["GET", "POST"])
def acted():
    form = Mine()
    return render_template("acted.html", form=form, client=form.client.data, address=form.address.data, qantity=form.quantity.data, mark=form.mark.data,
                           price=form.price.data, currency=form.currency.data, paid=form.paid.data, driver=form.driver.data, date=form.date.data,
                           approve=form.approve.data)


@app.route("/user")
def users():
    return render_template("users.html", users=User.query.all())


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        fullname = request.form.get("fullname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        comment = str(password1)
        if len(email) < 5:
            flash("At least 6 characters for email, please!", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif len(password1) < 5:
            flash("At least 6 characters for password, please", category="error")
        else:
            new_user = User(email=email, fullname=fullname, comment=comment, password=generate_password_hash(
                password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully!", category="success")
            redirect(url_for("index"))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
