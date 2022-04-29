from flask import Flask, render_template, request
from databaseconnection import connect_to_database as connect, get_table
import json


app = Flask(__name__)

def render_table(table, html):
    table = get_table(table, connect())
    table = json.dumps(table, default=str)
    return render_template(html, table=table)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tenants")
def tenants():
    return render_table("Tenants", "tenants.html")


@app.route("/buildings")
def buildings():
    return render_table("Buildings", "buildings.html")


@app.route("/unittypes")
def unittypes():
    return render_table("UnitTypes", "unittypes.html")


@app.route("/units")
def units():
    return render_table("Units", "units.html")


@app.route("/rentedunits")
def rentedunits():
    return render_table("RentedUnits", "rentedunits.html")


@app.route("/payments")
def payments():
    return render_table("Payments", "payments.html")


@app.route("/maintenance")
def maintenancerequests():
    return render_table("MaintenanceRequests", "maintenance.html")


@app.route("/tenantinformation")
def tenantinformation():
    return render_table("TenantInformation", "tenantinformation.html")


app.run("127.0.0.1", 2000)
