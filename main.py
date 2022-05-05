from flask import Flask, render_template, request
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


@app.route("/search/<first_name>/<last_name>")
def searching(first_name, last_name):
    return json.dumps(search(first_name, last_name), default=str)


@app.route("/tenants")
def tenants():
    return render_table("Tenants", "tenants.html")


@app.route("/tenants/update")
def edit_tenant():
    current = request.args.get("data")
    return render_template("tenantsEdit.html", current=current)


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


@app.route("/buildings/update")
def edit_building():
    current = request.args.get("data")
    return render_template("buildingsEdit.html", current=current)


@app.route("/unittypes")
def unittypes():
    return render_table("UnitTypes", "unittypes.html")


@app.route("/unittypes/update")
def edit_unit_type():
    current = request.args.get("data")
    return render_template("unittypesEdit.html", current=current)


@app.route("/unittypes/delete/<id_name>/<id>")
def delete_unit_type(id_name, id):
    delete_row("UnitTypes", id_name, id)
    table = get_table("UnitTypes")
    return json.dumps(table, default=str)


@app.route("/units")
def units():
    return render_table("Units", "units.html")


@app.route("/units/update")
def edit_unit():
    current = request.args.get("data")
    types = json.dumps(types_keys(), default=str)
    buildings = json.dumps(building_keys(), default=str)
    return render_template("unitsEdit.html", current=current, buildings=buildings, types=types)


@app.route("/units/delete/<id_name>/<id>")
def delete_unit(id_name, id):
    delete_row("Units", id_name, id)
    table = get_table("Units")
    return json.dumps(table, default=str)


@app.route("/rentedunits")
def rentedunits():
    return render_table("RentedUnits", "rentedunits.html")


@app.route("/rentedunits/update")
def edit_rental():
    tenants = json.dumps(tenants_keys(), default=str)
    current = request.args.get("data")
    return render_template("rentedunitsEdit.html", current=current, tenants=tenants)


@app.route("/rentedunits/delete/<id_name>/<id>")
def delete_rented_unit(id_name, id):
    delete_row("RentedUnits", id_name, id)
    table = get_table("RentedUnits")
    return json.dumps(table, default=str)


@app.route("/payments")
def payments():
    return render_table("Payments", "payments.html")


@app.route("/payments/update")
def edit_payment():
    tenants = json.dumps(tenants_keys(), default=str)
    current = request.args.get("data")
    return render_template("paymentsEdit.html", current=current, tenants=tenants)


@app.route("/payments/delete/<id_name>/<id>")
def delete_payment(id_name, id):
    delete_row("Payments", id_name, id)
    table = get_table("Payments")
    return json.dumps(table, default=str)


@app.route("/maintenance")
def maintenancerequests():
    return render_table("MaintenanceRequests", "maintenance.html")


@app.route("/maintenance/update")
def edit_maintenance():
    current = request.args.get("data")
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("maintenanceEdit.html", current=current, tenants=tenants)


@app.route("/maintenance/delete/<id_name>/<id>")
def delete_maintenance(id_name, id):
    delete_row("MaintenanceRequests", id_name, id)
    table = get_table("MaintenaceRequests")
    return json.dumps(table, default=str)


@app.route("/tenantinformation")
def tenantinformation():
    return render_table("TenantInformation", "tenantinformation.html")


@app.route("/tenantinformation/update")
def edit_tenantinformation():
    current = request.args.get("data")
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("tenantinformationEdit.html", current=current, tenants=tenants)


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
    types = json.dumps(types_keys(), default=str)
    buildings = json.dumps(building_keys(), default=str)
    return render_template("unitsNew.html", buildings=buildings, types=types)


@app.route("/rentedunits/new")
def rentednew():
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("rentedunitsNew.html", tenants=tenants)


@app.route("/payments/new")
def paymentsnew():
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("paymentsNew.html", tenants=tenants)


@app.route("/maintenance/new")
def maintenancenew():
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("maintenanceNew.html", tenants=tenants)


@app.route("/tenantinformation/new")
def infonew():
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("tenantinformationNew.html", tenants=tenants)


app.run("127.0.0.1", 2000)
