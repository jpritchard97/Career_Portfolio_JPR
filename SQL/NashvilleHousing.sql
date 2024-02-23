DROP TABLE IF EXISTS NashvilleHousing;
CREATE TABLE NashvilleHousing (
    UniqueID INT PRIMARY KEY,
    ParcelID VARCHAR(50), -- Change data type to VARCHAR to accommodate the provided values
    LandUse VARCHAR(50),
    PropertyAddress VARCHAR(100),
    SaleDate DATE,
    SalePrice INT,
    LegalReference VARCHAR(100),
    SoldAsVacant VARCHAR(3),
    OwnerName VARCHAR(100),
    OwnerAddress VARCHAR(100),
    Acreage FLOAT,
    TaxDistrict VARCHAR(50),
    LandValue FLOAT,
    BuildingValue FLOAT,
    TotalValue FLOAT,
    YearBuilt INT,
    Bedrooms INT,
    FullBath INT,
    HalfBath INT
);

-- Insert first two entries into employees table
INSERT INTO NashvilleHousing VALUES 
('2045', '007 00 0 125.00', 'SINGLE FAMILY', '1808 FOX CHASE DR, GOODLETTSVILLE', '2013-04-09', 240000, '20130412-0036474', 'No', 'FRAZIER, CYRENTHA LYNETTE', '1808 FOX CHASE DR, GOODLETTSVILLE, TN', 2.3, 'GENERAL SERVICES DISTRICT', 50000.0, 168200.0, 235700.0, 1986, 3, 3, 0),
('16918', '007 00 0 130.00', 'SINGLE FAMILY', '1832 FOX CHASE DR, GOODLETTSVILLE', '2014-06-10', 366000, '20140619-0053768', 'No', 'BONER, CHARLES & LESLIE', '1832 FOX CHASE DR, GOODLETTSVILLE, TN', 3.5, 'GENERAL SERVICES DISTRICT', 50000.0, 264100.0, 319000.0, 1998, 3, 3, 2),
('54582', '007 00 0 138.00', 'SINGLE FAMILY', '1864 FOX CHASE DR, GOODLETTSVILLE', '2016-09-26', 435000, '20160927-0101718', 'No', 'WILSON, JAMES E. & JOANNE', '1864 FOX CHASE DR, GOODLETTSVILLE, TN', 2.9, 'GENERAL SERVICES DISTRICT', 50000.0, 216200.0, 298000.0, 1987, 4, 3, 0),
('43070', '007 00 0 143.00', 'SINGLE FAMILY', '1853 FOX CHASE DR, GOODLETTSVILLE', '2016-01-29', 255000, '20160129-0008913', 'No', 'BAKER, JAY K. & SUSAN E.', '1853 FOX CHASE DR, GOODLETTSVILLE, TN', 2.6, 'GENERAL SERVICES DISTRICT', 50000.0, 147300.0, 197300.0, 1985, 3, 3, 0),
('22714', '007 00 0 149.00', 'SINGLE FAMILY', '1829 FOX CHASE DR, GOODLETTSVILLE', '2014-10-10', 278000, '20141015-0095255', 'No', 'POST, CHRISTOPHER M. & SAMANTHA C.', '1829 FOX CHASE DR, GOODLETTSVILLE, TN', 2.0, 'GENERAL SERVICES DISTRICT', 50000.0, 152300.0, 202300.0, 1984, 4, 3, 0);

-- SELECT statement

-- select all (*) columns from table
SELECT * FROM NashvilleHousing;

-- select some (3) columns of table
SELECT
	SalePrice,
	SaleDate,
	acreage
FROM NashvilleHousing;

-- WHERE clause + AND & OR

-- Select only the sale price that is more than 35k
SELECT *
FROM NashvilleHousing
WHERE SalePrice > 35000;

-- Select all the properties with an acreage greater than 2.5 and a sale price greater than $500,000
SELECT *
FROM NashvilleHousing
WHERE Acreage > 2.5 AND SalePrice > 500000;

-- Select all the properties with a sale price greater than $500,000 or with an acreage greater than 2.5
SELECT *
FROM NashvilleHousing
WHERE SalePrice > 500000 OR Acreage > 2.5;

-- Select all the properties with a sale price greater than $500,000, an acreage greater than 2.5, and built in the year 1986
SELECT *
FROM NashvilleHousing
WHERE SalePrice > 500000 AND Acreage > 2.5 AND YearBuilt = 1986;

-- Select all the properties with a sale price greater than $500,000, an acreage greater than 2.5, or built in the year 1986
SELECT *
FROM NashvilleHousing
WHERE SalePrice > 500000 OR Acreage > 2.5 OR YearBuilt = 1986;

--=======================================================

-- IN, NOT IN, IS NULL, BETWEEN

-- Select all rows from the NashvilleHousing table where the LandUse is "SINGLE FAMILY"
SELECT *
FROM NashvilleHousing
WHERE LandUse = 'SINGLE FAMILY';

-- Select all rows from the NashvilleHousing table where the LandUse is NOT "SINGLE FAMILY"
SELECT *
FROM NashvilleHousing
WHERE LandUse <> 'SINGLE FAMILY';

-- Select all properties with a LandUse of "SINGLE FAMILY" or "MULTI FAMILY"
SELECT *
FROM NashvilleHousing
WHERE LandUse IN ('SINGLE FAMILY', 'MULTI FAMILY');

-- Select all properties with a LandUse that is neither "SINGLE FAMILY" nor "MULTI FAMILY"
SELECT *
FROM NashvilleHousing
WHERE LandUse NOT IN ('SINGLE FAMILY', 'MULTI FAMILY');

-- Select all properties with a SaleDate that is missing
SELECT *
FROM NashvilleHousing
WHERE SaleDate IS NULL;

-- Select all properties with a SaleDate that is not missing
SELECT *
FROM NashvilleHousing
WHERE SaleDate IS NOT NULL;

-- Select all properties with a SalePrice between $250,000 and $500,000
SELECT *
FROM NashvilleHousing
WHERE SalePrice BETWEEN 250000 AND 500000;

-- ===============================================

-- ORDER BY, LIMIT, DISTINCT, Renaming columns

-- Order by SalePrice ascending 
SELECT
    UniqueID,
    ParcelID,
    LandUse,
    PropertyAddress,
    SaleDate,
    SalePrice
FROM NashvilleHousing
ORDER BY SalePrice;

-- Order by SalePrice descending 
SELECT
    UniqueID,
    ParcelID,
    LandUse,
    PropertyAddress,
    SaleDate,
    SalePrice
FROM NashvilleHousing
ORDER BY SalePrice DESC;

-- Top 10 highest SalePrice properties
SELECT
    UniqueID,
    ParcelID,
    LandUse,
    PropertyAddress,
    SaleDate,
    SalePrice
FROM NashvilleHousing
ORDER BY SalePrice DESC
LIMIT 10;

-- Return all unique LandUse values
SELECT DISTINCT LandUse
FROM NashvilleHousing;

-- Return all unique TaxDistrict values
SELECT DISTINCT TaxDistrict
FROM NashvilleHousing;

-- Renaming columns
SELECT
    OwnerName AS email,
    OwnerName AS email_address,
    SaleDate AS hire_date,
    SaleDate AS date_joined,
    SalePrice AS salary,
    SalePrice AS pay
FROM NashvilleHousing
WHERE UniqueID IN (16918, 54582, 43070, 22714, 2045);

-- EXTRACT

SELECT
    SaleDate AS date,
    EXTRACT(YEAR FROM SaleDate) AS year,
    EXTRACT(MONTH FROM SaleDate) AS month,
    EXTRACT(DAY FROM SaleDate) AS day
FROM NashvilleHousing;

--=========================================================

-- UPPER, LOWER, LENGTH, TRIM

-- Uppercase first and last names
SELECT
    OwnerName,
    UPPER(OwnerName) AS OwnerName_upper,
    PropertyAddress,
    UPPER(PropertyAddress) AS PropertyAddress_upper
FROM NashvilleHousing;

-- Lowercase first and last names
SELECT
    OwnerName,
    LOWER(OwnerName) AS OwnerName_lower,
    PropertyAddress,
    LOWER(PropertyAddress) AS PropertyAddress_lower
FROM NashvilleHousing;

-- Return the OwnerName and the length of OwnerName
SELECT
    OwnerName,
    LENGTH(OwnerName) AS OwnerName_length
FROM NashvilleHousing;

--=========================================================

-- GROUP BY & HAVING

-- Return the number of properties for each LandUse
SELECT
    LandUse,
    COUNT(*) as num_of_properties
FROM NashvilleHousing
GROUP BY LandUse;

-- Return the total sale prices for each LandUse
SELECT
    LandUse,
    SUM(SalePrice) as total_sales
FROM NashvilleHousing
GROUP BY LandUse;

-- Return the number of properties, the avg & min & max & total sale prices for each LandUse
SELECT
    LandUse,
    COUNT(*) as num_of_properties,
    ROUND(AVG(SalePrice), 0) as avg_sale_price,
    MIN(SalePrice) as min_sale_price,
    MAX(SalePrice) as max_sale_price,
    SUM(SalePrice) as total_sales
FROM NashvilleHousing
GROUP BY LandUse
ORDER BY num_of_properties DESC;

-- HAVING
-- After GROUP BY, return only the LandUses with more than 100 properties
SELECT
    LandUse,
    COUNT(*) as num_of_properties,
    ROUND(AVG(SalePrice), 0) as avg_sale_price,
    MIN(SalePrice) as min_sale_price,
    MAX(SalePrice) as max_sale_price,
    SUM(SalePrice) as total_sales
FROM NashvilleHousing
GROUP BY LandUse
HAVING COUNT(*) > 100
ORDER BY num_of_properties DESC;

--===========================================================

-- CASE, CASE with GROUP BY, and CASE for transposing data

-- CASE
-- If the property is sold as vacant, then 'Sold as Vacant', otherwise 'Not Sold as Vacant'
SELECT
    PropertyAddress,
    CASE
        WHEN SoldAsVacant = 'Yes' THEN 'Sold as Vacant'
        ELSE 'Not Sold as Vacant'
    END as sold_status
FROM NashvilleHousing;

-- If Acreage is less than 1, then 'Small Property'
-- if between 1-5 inclusive, then 'Medium Property'
-- if over 5, then 'Large Property'
SELECT
    PropertyAddress,
    CASE
        WHEN Acreage < 1 THEN 'Small Property'
        WHEN Acreage BETWEEN 1 AND 5 THEN 'Medium Property'
        WHEN Acreage > 5 THEN 'Large Property'
        ELSE 'Unknown'
    END as property_size_category
FROM NashvilleHousing
ORDER BY Acreage;

-- CASE & GROUP BY 
-- Return the count of properties in each property size category
SELECT 
    property_size_category,
    COUNT(*) as num_of_properties
FROM (
    SELECT
        PropertyAddress,
        CASE
            WHEN Acreage < 1 THEN 'Small Property'
            WHEN Acreage BETWEEN 1 AND 5 THEN 'Medium Property'
            WHEN Acreage > 5 THEN 'Large Property'
            ELSE 'Unknown'
        END as property_size_category
    FROM NashvilleHousing
) a
GROUP BY property_size_category;

-- Transpose above
SELECT
    SUM(CASE WHEN Acreage < 1 THEN 1 ELSE 0 END) AS small_properties,
    SUM(CASE WHEN Acreage BETWEEN 1 AND 5 THEN 1 ELSE 0 END) AS medium_properties,
    SUM(CASE WHEN Acreage > 5 THEN 1 ELSE 0 END) AS large_properties
FROM NashvilleHousing;

--================================================

-- JOIN

-- Inserting values just for JOIN exercises
INSERT INTO locations VALUES (4, 'Paris', 'France');

-- Checking the values we inserted
SELECT * FROM locations;

-- INNER JOIN
SELECT 
    n.PropertyAddress,
    l.city,
    l.country
FROM NashvilleHousing as n
INNER JOIN locations as l
ON n.TaxDistrict = l.country;

-- Delete the values we created just for the JOIN exercises
DELETE FROM locations WHERE city = 'Paris';

--========================================================
