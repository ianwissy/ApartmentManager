from flask import Flask, render_template, request
from databaseconnection import connect_to_database as connect, get_table
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tenants")
def tenants():
    table = get_table("Tenants", connect())
    table = json.dumps(table,default=str)
    return render_template("tenants.html", table=table)


@app.route("/buildings")
def buildings():
    return render_template("buildings.html")


@app.route("/unittypes")
def unittypes():
    return render_template("unittypes.html")


@app.route("/units")
def units():
    return render_template("units.html")


@app.route("/rentedunits")
def rentedunits():
    return render_template("rentedunits.html")


@app.route("/payments")
def payments():
    return render_template("payments.html")


@app.route("/maintenancerequests")
def maintenancerequests():
    return render_template("maintenancerequests.html")


@app.route("/tenantinformation")
def tenantinformation():
    return render_template("tenantinformmation.html")


app.run("127.0.0.1", 2000)
