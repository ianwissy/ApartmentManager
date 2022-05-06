-- 1. Main 

-- search by tenant name
SELECT FirstName, LastName, Type, BuildingName, Price 
FROM Tenants INNER JOIN RentedUnits
ON Tenants.TenantID = RentedUnits.TenantID 
INNER JOIN Units 
ON RentedUnits.UnitID = Units.UnitID 
INNER JOIN Buildings 
ON Units.BuildingID = Buildings.BuildingID 
INNER JOIN UnitTypes 
ON Units.UnitTypeID = UnitTypes.UnitTypeID 
WHERE FirstName=:first_name AND LastName=:last_name

-- 2. Buildings

-- populate Buildings table
SELECT * from Buildings;

-- insert into Buldings;
INSERT INTO `Buildings` (`BuildingName`, `YTDBuildingRevenue`)
VALUES (:bnameInput, :ytdbuildingRevenueInput);

-- delete a Building
DELETE FROM Buildings WHERE BuildingID=:ID;

-- edit a Building
UPDATE Buildings
SET BuildingName=:bnameInput, YTDBuildingRevenue=:ytdbuildingRevenueInput
WHERE BuildingsID=:ID;

-- get Building keys
SELECT BuildingID, BuildingName FROM Buildings;

-- 3. Tenants

-- populate Tenants table
SELECT * from Tenants;

-- insert into Tenants
INSERT INTO Tenants (FirstName, LastName, Age, PhoneNumber, Balance)
 VALUES (:fnameInput, :lnameInput, :ageInput, :pnumberInput, :balanceInput);

-- delete a Tenant
DELETE FROM Tenants WHERE TenantID=:ID;

-- edit a Tenant
UPDATE Buildings
SET FirstName=:fnameInput, LastName=:lnameInput, Age=:ageInput, PhoneNumber=:pnumberInput, Balance=:balanceInput
WHERE TenantID=:ID;

-- get Tenant keys
SELECT TenantID, FirstName, LastName FROM Tenants;

-- 4. Units 

-- populate Units table
SELECT * from Units;

-- insert into Units
INSERT INTO Units (Price, Rented, Note, BuildingID, UnitTypeID) VALUES
(:priceInput, :rentedInput, :noteInput, :bidInput, :uidInput);

-- delete a Unit
DELETE FROM Units WHERE UnitID=:ID;

-- edit a Unit
UPDATE Units
SET Price=:priceInput, Rented=:rentedInput, Note=:noteInput, BuildingID=:bidInput, UnitTypeID=:uidInput
WHERE TenantID=:ID;

-- 5. Unit Types

-- populate Unit Types table
SELECT * from UnitsTypes;

-- insert into UnitTypes
INSERT INTO UnitTypes (Type) 
VALUES(:typeInput);

-- delete a Unit
DELETE FROM UnitTypes WHERE UnitTypeID=:ID;

-- edit a Unit
UPDATE UnitTypes
SET Type=:typeInput
WHERE UnitTypeID=:ID;

-- get types keys
SELECT UnitTypeID, TYPE FROM UnitTypes;

-- 6. Payments

-- populate Payments table
SELECT * from Payments;

-- insert into Payments
INSERT INTO `Payments` (`Date`, `Amount`, `UnitID`, `TenantID`) VALUES
(:dateInput, :amountInput, :uidInput, :tidInput);

-- delete a Payment
DELETE FROM Payments WHERE PaymentID=:ID;

-- edit a Payment
UPDATE Payments
SET Date=:dateInput, Amount=:amountInput, UnitID=:uidInput, TenantID=:tidInput
WHERE PaymentID=:ID;

-- 7. Rented Units

-- populate Rented Units table
SELECT * from RentedUnits;

-- insert into RentedUnits
INSERT INTO `RentedUnits` (`UnitID`, `TenantID`, `StartDate`) VALUES
(:uidInput, :tidInput, :sdateinput)

-- delete a RentedUnit
DELETE FROM RentedUnits WHERE RentalID=:ID;

-- edit a Rented Unit
UPDATE RentedUnits
SET UnitID=:uidInput, `TenantID`=:tidInput, `StartDate`=:sdateinput
WHERE RentalID=:ID;

-- 8. Maintenance Requests

-- populate Maintenance table
SELECT * from MaintenanceRequests;

-- insert into MaintenanceRequests
INSERT INTO `MaintenenceRequests` (`UnitID`, `TenantID`, `RequestDate`, `Completed`, `RequestNote`) VALUES
(:uidInput, :tidInput, :rdateInput, :completedInput, :rnoteInput);

-- delete a MaintenanceRequest
DELETE FROM MaintenanceRequests WHERE RequestID=:ID;

-- edit a MaintenanceRequest
UPDATE MaintenanceRequest
SET UnitID=:uidInput, TenantID=:tidInput, RequestDate=:rdateInput, Completed=:completedInput, RequestNote=:rnoteInput
WHERE RequestID=:ID;

-- 9. Tenant Information

-- populate Tenant Information table
SELECT * from MaintenanceRequests;

-- insert into MaintenanceRequests
INSERT INTO `TenantInformation` (`TenantID`, `SSN`, `CCN`)
VALUES (:tidInput, :ssnInput, :ccnInput);


-- delete Tenant Informaiton
DELETE FROM TenantInformation WHERE TenantID=:ID;

-- edit Tenant Information
UPDATE TenantInformation
SET TenantID=:tidInput, SSN=:ssnInput, CCN=:ccnInput
WHERE RequestID=:ID;
