from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField, FloatField
from wtforms.fields import DateField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from __init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class QRCodeData(FlaskForm):
    dat = StringField("Data", validators=[
                      DataRequired(), Length(min=3, max=500)])
    submit = SubmitField("Generate QRCode")


class Mine(FlaskForm):
    client_id = IntegerField("client_id", validators=[DataRequired()])
    client = StringField("Client", validators=[
                         DataRequired(), Length(min=3, max=500)])
    address = StringField("Address", validators=[
                          DataRequired(), Length(min=3, max=500)])
    quantity = FloatField("Quantity", validators=[
        DataRequired()])
    mark = StringField("Mark", validators=[
                       DataRequired(), Length(min=3, max=100)])
    price = IntegerField("Price", validators=[DataRequired()])
    currency = SelectField("Currency", choices=["UZS", "USD", "EUR", "RUB"])
    paid = IntegerField("Paid", validators=[DataRequired()])
    driver = SelectField("Driver", choices=[
                         "No", "861", "862", "863", "864", "145", "146"])
    date = DateField("Date", validators=[DataRequired()])
    approve = SelectField("Agreement", choices=[
                          "✅", "❌"])
    user_fullname = StringField("User_fullname", validators=[DataRequired()])
    submit = SubmitField("Confirm")


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# User Class:
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(150))
    fullname = db.Column(db.String(250))
    comment = db.Column(db.String(250))
    notes = db.relationship("Note")
    reg = db.relationship("Reg", backref="user")


class Reg(db.Model):
    __tablename__ = "reg"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    client = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    quantity = db.Column(db.Float)
    mark = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    paid = db.Column(db.Integer)
    currency = db.Column(db.String())
    driver = db.Column(db.String(1000))
    date = db.Column(db.String())
    approve = db.Column(db.String())
    user_fullname = db.Column(db.String(), db.ForeignKey("user.fullname"))

    def __init__(self, client, address, quantity, mark, price, paid, currency, driver, date, approve, user_fullname, client_id):
        self.client = client
        self.address = address
        self.quantity = quantity
        self.mark = mark
        self.price = price
        self.paid = paid
        self.currency = currency
        self.driver = driver
        self.date = date
        self.approve = approve
        self.user_fullname = user_fullname
        self.client_id = client_id
