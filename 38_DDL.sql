SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `Buildings` (
  `BuildingID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `BuildingName` varchar(45) DEFAULT NULL,
  `YTDBuildingRevenue` decimal(12,2) DEFAULT NULL
);

INSERT INTO `Buildings` (`BuildingName`, `YTDBuildingRevenue`) VALUES
('Shady Oaks', '232345.23'),
('The Grizwald', '434234.06'),
('Orange Groves', '123445.23');

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `Tenants` (
  `TenantID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Age` int(3) NOT NULL,
  `PhoneNumber` bigint(11) NOT NULL,
  `Balance` decimal(12,2) DEFAULT NULL
);

INSERT INTO `Tenants` (`FirstName`, `LastName`, `Age`, `PhoneNumber`, `Balance`) VALUES
('Douge', 'Jones', 56, 9323234356, NULL),
('James', 'Cameron', 26, 2342758493, '1600.34'),
('Hope', 'Heeble', 28, 2349990452, '800.00'),
('Horble', 'Florble', 102, 1000000000, '7921.05'),
('Red', 'Rackham', 85, 2450245924, '0.00');

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `UnitTypes` (
  `UnitTypeID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Type` varchar(45) NOT NULL
);

INSERT INTO `UnitTypes` (`Type`) VALUES
('Studio'),
('One Bedroom'),
('Two Bedroom'),
('Garage'),
('Storage');

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `TenantInformation` (
  `TenantID` int(11) NOT NULL PRIMARY KEY,
  `SSN` int(9) DEFAULT NULL,
  `CCN` bigint(16) DEFAULT NULL,
  CONSTRAINT FOREIGN KEY (`TenantID`) REFERENCES Tenants(`TenantID`) ON DELETE CASCADE
);

INSERT INTO `TenantInformation` (`TenantID`, `SSN`, `CCN`) VALUES
(2, 546850954, NULL),
(3, 846058947, 5034585840395943),
(4, 275893901, 4504504250405042),
(5, 342345234, 5849394959493249);

-- --------------------------------------------------------

CREATE OR REPLACE TABLE Units (
  `UnitID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `AptNum` varchar(8) NOT NULL,
  `Price` decimal(12,2) NOT NULL,
  `Note` text DEFAULT NULL,
  `BuildingID` int(11) NOT NULL,
  `UnitTypeID` int(11) NOT NULL,
  CONSTRAINT FOREIGN KEY (BuildingID) REFERENCES Buildings(BuildingID) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (UnitTypeID) REFERENCES UnitTypes(UnitTypeID) ON DELETE CASCADE
);

INSERT INTO `Units` (`AptNum`, `Price`, `Note`, `BuildingID`, `UnitTypeID`) VALUES
('406', '1600.34', '4th floor corner', 1, 1),
('112', '1950.34', '1st floor center no view', 1, 2),
('208', '2400.00', NULL, 2, 3),
('06S', '500.35', NULL, 2, 5),
('302', '2140.00', NULL, 3, 2),
('02G', '800.00', NULL, 3, 4);

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `MaintenanceRequests` (
  `RequestID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `UnitID` int(11) NOT NULL,
  `TenantID` int(11),
  `RequestDate` date NOT NULL,
  `Completed` tinyint(1) NOT NULL,
  `RequestNote` text DEFAULT NULL,
  CONSTRAINT FOREIGN KEY (UnitID) REFERENCES Units(UnitID) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE SET NULL
);

INSERT INTO `MaintenanceRequests` (`UnitID`, `TenantID`, `RequestDate`, `Completed`, `RequestNote`) VALUES
(1, 2, '2020-04-23', 1, 'Sink broken'),
(3, 3, '2021-01-20', 1, NULL),
(5, 4, '2022-04-20', 0, 'Leaky roof');

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `Payments` (
  `PaymentID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Amount` decimal(12,2) NOT NULL,
  `UnitID` int(11),
  `TenantID` int(11),
  CONSTRAINT FOREIGN KEY (`UnitID`) REFERENCES Units(`UnitID`) ON DELETE SET NULL,
  CONSTRAINT FOREIGN KEY (`TenantID`) REFERENCES Tenants(`TenantID`) ON DELETE SET NULL
);

INSERT INTO `Payments` (`Date`, `Amount`, `UnitID`, `TenantID`) VALUES
('2022-04-12', '1600.34', 1, 2),
('2022-03-12', '1600.34', 1, 2),
('2022-03-12', '1501.05', 4, 4),
('2022-03-12', '6420.00', 5, 4);

-- --------------------------------------------------------

CREATE OR REPLACE TABLE `RentedUnits` (
  `RentalID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `UnitID` int(11) NOT NULL,
  `TenantID` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  CONSTRAINT FOREIGN KEY (`TenantID`) REFERENCES Tenants(`TenantID`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`UnitID`) REFERENCES Units(`UnitID`) ON DELETE CASCADE
);

INSERT INTO `RentedUnits` (`UnitID`, `TenantID`, `StartDate`) VALUES
(1, 2, '2018-10-01'),
(1, 1, '2018-10-01'),
(4, 4, '1985-08-01'),
(5, 4, '1982-07-01'),
(3, 3, '2020-02-01');

-- --------------------------------------------------------

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
