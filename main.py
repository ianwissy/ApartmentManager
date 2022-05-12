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


@app.route("/tenants", methods=["GET", "POST", "PUT"])
def tenants():
    if request.method == "GET":
        return render_table("Tenants", "tenants.html")
    elif request.method == "PUT":
        query = "UPDATE Tenants " \
            "SET FirstName='"+request.json['values'][1]+"', LastName='"+request.json['values'][2]+"', " \
            "Age="+request.json['values'][3]+", PhoneNumber="+request.json['values'][4]+", " \
            "Balance="+request.json['values'][5]+" WHERE TenantID="+request.json['values'][0]+";"
        send_query(query)
        return "/tenants"
    elif request.method == "POST":
        query = "INSERT INTO Tenants (FirstName, LastName, Age, PhoneNumber, Balance) " \
                "VALUES ('"+request.json['values'][0]+"', '"+request.json['values'][1]+"', "+request.json['values'][2]+"," \
                " "+request.json['values'][3]+", "+request.json['values'][4]+");"
        send_query(query)
        return "/tenants"


@app.route("/tenants/new")
def tenantnew():
    return render_template("tenantsNew.html")


@app.route("/tenants/update")
def edit_tenant():
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM Tenants WHERE TenantID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("tenantsEdit.html", current=row)


@app.route("/tenants/delete/<id_name>/<id>")
def delete_tenant(id_name, id):
    delete_row("Tenants", id_name, id)
    table = get_table("Tenants")
    return json.dumps(table, default=str)


@app.route("/buildings", methods=["GET", "POST", "PUT"])
def buildings():
    if request.method == "GET":
        return render_table("Buildings", "buildings.html")
    elif request.method == "PUT":
        query = "UPDATE Buildings " \
            "SET BuildingName='"+request.json['values'][1]+"', YTDBuildingRevenue="+request.json['values'][2]+" " \
            "WHERE BuildingID="+request.json['values'][0]+";"
        send_query(query)
        return "/buildings"
    elif request.method == "POST":
        query = "INSERT INTO Buildings (BuildingName, YTDBuildingRevenue) VALUES \
                ('"+request.json['values'][0]+"', "+request.json['values'][1]+");"
        send_query(query)
        return "/buildings"


@app.route("/buildings/new")
def buildingnew():
    return render_template("buildingsNew.html")


@app.route("/buildings/delete/<id_name>/<id>")
def delete_building(id_name, id):
    delete_row("Buildings", id_name, id)
    table = get_table("Buildings")
    return json.dumps(table, default=str)


@app.route("/buildings/update")
def edit_building():
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM Buildings WHERE BuildingID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("buildingsEdit.html", current=row)


@app.route("/unittypes", methods=["GET", "POST", "PUT"])
def unittypes():
    if request.method == "GET":
        return render_table("UnitTypes", "unittypes.html")
    elif request.method == "PUT":
        query = "UPDATE UnitTypes " \
            "SET Type='"+request.json['values'][1]+"' " \
            "WHERE UnitTypeID="+request.json['values'][0]+";"
        send_query(query)
        return "/unittypes"
    elif request.method == "POST":
        query = "INSERT INTO UnitTypes (Type) VALUES \
                ('"+request.json['values'][0]+"');"
        send_query(query)
        return "/unittypes"


@app.route("/unittypes/new")
def typesnew():
    return render_template("unittypesNew.html")


@app.route("/unittypes/update")
def edit_unit_type():
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM UnitTypes WHERE UnitTypeID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("unittypesEdit.html", current=row)


@app.route("/unittypes/delete/<id_name>/<id>")
def delete_unit_type(id_name, id):
    delete_row("UnitTypes", id_name, id)
    table = get_table("UnitTypes")
    return json.dumps(table, default=str)


@app.route("/units", methods=["GET", "POST", "PUT"])
def units():
    if request.method == "GET":
        query = "SELECT UnitId, AptNum, Price, Rented, Note, BuildingName, Type FROM \
                Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID"
        table = get_query(query)
        table = json.dumps(table, default=str)
        return render_template("units.html", table=table)
    elif request.method == "PUT":
        query = "UPDATE Units " \
            "SET AptNum='"+request.json['values'][1]+"', Price="+request.json['values'][2]+", Rented="+request.json['values'][3]+", Note='"+request.json['values'][4]+"', " \
            "BuildingID="+request.json['values'][5]+", UnitTypeID="+request.json['values'][6]+" " \
            "WHERE UnitID="+request.json['values'][0]+";"
        send_query(query)
        return "/units"
    elif request.method == "POST":
        query = "INSERT INTO Units (AptNum, Price, Rented, Note, BuildingID, UnitTypeID) VALUES \
                ("+request.json['values'][0]+", "+request.json['values'][1]+", "+request.json['values'][2]+", \
                '"+request.json['values'][3]+"', "+request.json['values'][4]+", "+request.json['values'][5]+");"
        send_query(query)
        return "/units"


@app.route("/units/new")
def new_unit():
    types = json.dumps(types_keys(), default=str)
    buildings = json.dumps(building_keys(), default=str)
    return render_template("unitsNew.html", buildings=buildings, types=types)


@app.route("/units/update")
def edit_unit():
    types = json.dumps(types_keys(), default=str)
    buildings = json.dumps(building_keys(), default=str)
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM Units WHERE UnitID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("unitsEdit.html", current=row, types=types, buildings=buildings)


@app.route("/units/delete/<id_name>/<id>")
def delete_unit(id_name, id):
    delete_row("Units", id_name, id)
    table = get_query("SELECT UnitId, AptNum, Price, Rented, Note, BuildingName, Type FROM \
                Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID")
    return json.dumps(table, default=str)


@app.route("/rentedunits", methods=["POST", "GET", "PUT"])
def rentedunits():
    if request.method == "GET":
        query = "SELECT RentalID, AptNum, BuildingName, Type, FirstName, LastName, StartDate FROM \
                    Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                    INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
                    INNER JOIN RentedUnits ON Units.UnitID=RentedUnits.UnitID \
                    INNER JOIN Tenants ON RentedUnits.TenantID=Tenants.TenantID"
        table = get_query(query)
        table = json.dumps(table, default=str)
        return render_template("rentedunits.html", table=table)
    elif request.method == "PUT":
        query = "UPDATE RentedUnits " \
            "SET UnitID="+request.json['values'][1]+", `TenantID`="+request.json['values'][2]+", `StartDate`='"+request.json['values'][3]+"' " \
            "WHERE RentalID="+request.json['values'][0]+";"
        send_query(query)
        return "/rentedunits"
    elif request.method == "POST":
        query = "INSERT INTO `RentedUnits` (`UnitID`, `TenantID`, `StartDate`) VALUES" \
            "(" + request.json['values'][0] + ", " + request.json['values'][1] + ", '" + request.json['values'][2] + "')"
        send_query(query)
        return "/rentedunits"


@app.route("/rentedunits/new")
def rentednew():
    tenants = json.dumps(tenants_keys(), default=str)
    units = json.dumps(units_keys(), default=str)
    return render_template("rentedunitsNew.html", tenants=tenants, units=units)


@app.route("/rentedunits/update")
def edit_rental():
    tenants = json.dumps(tenants_keys(), default=str)
    units = json.dumps(units_keys(), default=str)
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM RentedUnits WHERE RentalID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("rentedunitsEdit.html", current=row, tenants=tenants, units=units)


@app.route("/rentedunits/delete/<id_name>/<id>")
def delete_rented_unit(id_name, id):
    delete_row("RentedUnits", id_name, id)
    table = get_query("SELECT RentalID, AptNum, BuildingName, Type, FirstName, LastName, StartDate FROM \
            Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
            INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
            INNER JOIN RentedUnits ON Units.UnitID=RentedUnits.UnitID \
            INNER JOIN Tenants ON RentedUnits.TenantID=Tenants.TenantID")
    return json.dumps(table, default=str)


@app.route("/payments", methods=["GET", "POST", "PUT"])
def payments():
    if request.method == "GET":
        query = "SELECT PaymentID, Date, Amount, AptNum, BuildingName, FirstName, LastName FROM \
            Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
            INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
            INNER JOIN Payments ON Units.UnitID=Payments.UnitID \
            INNER JOIN Tenants ON Payments.TenantID=Tenants.TenantID"
        table = get_query(query)
        table = json.dumps(table, default=str)
        return render_template("payments.html", table=table)
    elif request.method == "PUT":
        query = "UPDATE Payments " \
            "SET Date='" + request.json['values'][1] + "', Amount=" + request.json['values'][2] + "" \
                    ", UnitID=" + request.json['values'][3] + ", TenantID=" + request.json['values'][4] + " " \
                    "WHERE PaymentID=" + request.json['values'][0] + ";"
        send_query(query)
        return "/payments"
    elif request.method == "POST":
        query = "INSERT INTO Payments (Date, Amount, UnitID, TenantID) VALUES \
                 ('" + request.json['values'][0] + "', " + request.json['values'][1] + "," \
                " " + request.json['values'][2] + ", " + request.json['values'][3] + ");"
        send_query(query)
        return "/payments"


@app.route("/payments/new")
def paymentsnew():
    tenants = json.dumps(tenants_keys(), default=str)
    units = json.dumps(units_keys(), default=str)
    return render_template("paymentsNew.html", tenants=tenants, units=units)


@app.route("/payments/update")
def edit_payment():
    tenants = json.dumps(tenants_keys(), default=str)
    units = json.dumps(units_keys(), default=str)
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM Payments WHERE PaymentID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("paymentsEdit.html", current=row, tenants=tenants, units=units)


@app.route("/payments/delete/<id_name>/<id>")
def delete_payment(id_name, id):
    delete_row("Payments", id_name, id)
    table = get_query("SELECT PaymentID, Date, Amount, AptNum, BuildingName, FirstName, LastName FROM \
                        Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                        INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
                        INNER JOIN Payments ON Units.UnitID=Payments.UnitID \
                        INNER JOIN Tenants ON Payments.TenantID=Tenants.TenantID")
    return json.dumps(table, default=str)


@app.route("/maintenance", methods=["GET", "POST", "PUT"])
def maintenancerequests():
    if request.method == "GET":
        query = "SELECT RequestID, AptNum, BuildingName, FirstName, LastName, RequestDate, Completed, RequestNote FROM \
                            Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                            INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
                            INNER JOIN MaintenanceRequests ON Units.UnitID=MaintenanceRequests.UnitID \
                            INNER JOIN Tenants ON MaintenanceRequests.TenantID=Tenants.TenantID"
        table = get_query(query)
        table = json.dumps(table, default=str)
        return render_template("maintenance.html", table=table)
    elif request.method == "PUT":
        query = "UPDATE MaintenanceRequests " \
            "SET UnitID=" + request.json['values'][1] + ", TenantID=" + request.json['values'][2] + "" \
            ", RequestDate='" + request.json['values'][3] + "', Completed=" + request.json['values'][4] + ", " \
            "RequestNote='" + request.json['values'][5] + "' WHERE RequestID=" + request.json['values'][0] + ";"
        send_query(query)
        return "/maintenance"
    elif request.method == "POST":
        query = "INSERT INTO `MaintenanceRequests` (`UnitID`, `TenantID`, `RequestDate`, `Completed`, `RequestNote`)" \
                "VALUES (" + request.json['values'][0] + ", " + request.json['values'][1] + "," \
                " '" + request.json['values'][2] + "', " + request.json['values'][3] + ", '" + request.json['values'][4] + "');"
        send_query(query)
        return "/maintenance"


@app.route("/maintenance/new")
def maintenancenew():
    units = json.dumps(units_keys(), default=str)
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("maintenanceNew.html", tenants=tenants, units=units)


@app.route("/maintenance/update")
def edit_maintenance():
    units = json.dumps(units_keys(), default=str)
    tenants = json.dumps(tenants_keys(), default=str)
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM MaintenanceRequests WHERE RequestID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("maintenanceEdit.html", current=row, units=units, tenants=tenants)


@app.route("/maintenance/delete/<id_name>/<id>")
def delete_maintenance(id_name, id):
    delete_row("MaintenanceRequests", id_name, id)
    table = get_query("SELECT RequestID, AptNum, BuildingName, FirstName, LastName, RequestDate, Completed, RequestNote FROM \
                            Units INNER JOIN Buildings ON Units.BuildingID=Buildings.BuildingID \
                            INNER JOIN UnitTypes ON Units.UnitTypeID=UnitTypes.UnitTypeID \
                            INNER JOIN MaintenanceRequests ON Units.UnitID=MaintenanceRequests.UnitID \
                            INNER JOIN Tenants ON MaintenanceRequests.TenantID=Tenants.TenantID")
    return json.dumps(table, default=str)


@app.route("/tenantinformation", methods=["GET", "POST", "PUT"])
def tenantinformation():
    if request.method == "GET":
        query = "SELECT Tenants.TenantID, FirstName, LastName, SSN, CCN FROM Tenants \
            INNER JOIN TenantInformation ON Tenants.TenantID=TenantInformation.TenantID"
        table = get_query(query)
        table = json.dumps(table, default=str)
        return render_template("tenantinformation.html", table=table)
    elif request.method == "PUT":
        query = "UPDATE TenantInformation " \
            "SET SSN=" + request.json['values'][1] + ", CCN=" + request.json['values'][2] + "" \
            " WHERE TenantID=" + request.json['values'][0] + ";"
        send_query(query)
        return "/tenantinformation"
    elif request.method == "POST":
        query = "INSERT INTO `TenantInformation` (`TenantID`, `SSN`, `CCN`)" \
                "VALUES (" + request.json['values'][0] + ", " + request.json['values'][1] + "," \
                " " + request.json['values'][2] + ");"
        send_query(query)
        return "/tenantinformation"


@app.route("/tenantinformation/new")
def infonew():
    tenants = json.dumps(tenants_keys(), default=str)
    return render_template("tenantinformationNew.html", tenants=tenants)



@app.route("/tenantinformation/update")
def edit_tenantinformation():
    tenants = json.dumps(tenants_keys(), default=str)
    id = request.args.get("data")
    row = list(get_query("SELECT * FROM TenantInformation WHERE TenantID=" + id)[0])
    row = json.dumps(row, default=str)
    return render_template("tenantinformationEdit.html", current=row, tenants=tenants)


@app.route("/tenantinformation/delete/<id_name>/<id>")
def delete_tenant_info(id_name, id):
    delete_row("TenantInformation", id_name, id)
    table = get_query("SELECT Tenants.TenantID, FirstName, LastName, SSN, CCN FROM Tenants \
            INNER JOIN TenantInformation ON Tenants.TenantID=TenantInformation.TenantID")
    return json.dumps(table, default=str)


app.run("127.0.0.1", 2000)
