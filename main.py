from flask import Flask, render_template
from databaseconnection import *
import json


app = Flask(__name__)


def render_table(table, html):
    table = get_table(table)
    table = json.dumps(table, default=str)
    return render_template(html, table=table)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tenants")
def tenants():
    return render_table("Tenants", "tenants.html")


@app.route("/tenants/delete/<id_name>/<id>")
def delete_tenant(id_name, id):
    delete_row("Tenants", id_name, id)
    table = get_table("Tenants")
    return json.dumps(table, default=str)


@app.route("/buildings")
def buildings():
    return render_table("Buildings", "buildings.html")


@app.route("/buildings/delete/<id_name>/<id>")
def delete_building(id_name, id):
    delete_row("Buildings", id_name, id)
    table = get_table("Buildings")
    return json.dumps(table, default=str)


@app.route("/unittypes")
def unittypes():
    return render_table("UnitTypes", "unittypes.html")


@app.route("/unittypes/delete/<id_name>/<id>")
def delete_unit_type(id_name, id):
    delete_row("UnitTypes", id_name, id)
    table = get_table("UnitTypes")
    return json.dumps(table, default=str)


@app.route("/units")
def units():
    return render_table("Units", "units.html")


@app.route("/units/delete/<id_name>/<id>")
def delete_unit(id_name, id):
    delete_row("Units", id_name, id)
    table = get_table("Units")
    return json.dumps(table, default=str)


@app.route("/rentedunits")
def rentedunits():
    return render_table("RentedUnits", "rentedunits.html")


@app.route("/rentedunits/delete/<id_name>/<id>")
def delete_rented_unit(id_name, id):
    delete_row("RentedUnits", id_name, id)
    table = get_table("RentedUnits")
    return json.dumps(table, default=str)


@app.route("/payments")
def payments():
    return render_table("Payments", "payments.html")


@app.route("/payments/delete/<id_name>/<id>")
def delete_payment(id_name, id):
    delete_row("Payments", id_name, id)
    table = get_table("Payments")
    return json.dumps(table, default=str)


@app.route("/maintenance")
def maintenancerequests():
    return render_table("MaintenanceRequests", "maintenance.html")


@app.route("/maintenance/delete/<id_name>/<id>")
def delete_maintenance(id_name, id):
    delete_row("MaintenanceRequests", id_name, id)
    table = get_table("MaintenaceRequests")
    return json.dumps(table, default=str)


@app.route("/tenantinformation")
def tenantinformation():
    return render_table("TenantInformation", "tenantinformation.html")


@app.route("/tenantinformation/delete/<id_name>/<id>")
def delete_tenant_info(id_name, id):
    delete_row("TenantInformation", id_name, id)
    table = get_table("TenantInformation")
    return json.dumps(table, default=str)


@app.route("/tenants/new")
def tenantnew():
    return render_template("tenantsNew.html")


@app.route("/buildings/new")
def buildingnew():
    return render_template("buildingsNew.html")


@app.route("/unittypes/new")
def typesnew():
    return render_template("unittypesNew.html")


@app.route("/units/new")
def unitsnew():
    return render_template("unitsNew.html")


@app.route("/rentedunits/new")
def rentednew():
    return render_template("rentedunitsNew.html")


@app.route("/payments/new")
def paymentsnew():
    return render_template("paymentsNew.html")


@app.route("/maintenance/new")
def maintenancenew():
    return render_template("maintenanceNew.html")


@app.route("/tenantinformation/new")
def infonew():
    return render_template("tenantinformationNew.html")


app.run("127.0.0.1", 2000)
