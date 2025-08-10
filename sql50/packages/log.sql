
-- *** The Lost Letter ***

-- information available
-- 900 Somerville Avenue - source
-- 2 Finnegan Street, uptown - destination
-- letter

-- source id = 432
SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue';
-- she misspelled Finnigan
SELECT "address" FROM "addresses" WHERE "address" LIKE '2%F%Street%';
-- destination id = 854 AND type is Residential
SELECT "id", "type" FROM "addresses" WHERE "address" = '2 Finnigan Street';
-- finding id of the package = 384
SELECT "id" FROM "packages"
WHERE "contents" LIKE '%letter%' AND "from_address_id" = 432 AND "to_address_id" = 854;
-- package was delivered to its location successfully at 2023-07-11 23:07:04
SELECT "address_id", "action", "timestamp" FROM "scans" WHERE "package_id" = 384;

-- *** The Devious Delivery ***

-- Since the from address is null
-- we get contents = duck debugger
-- delivery address id = 50
-- package id = 5098
SELECT * FROM "packages" WHERE "from_address_id" IS NULL;

-- destination address id = 348
SELECT * FROM "scans" WHERE "package_id" = 5098 AND "action" = 'Drop';

-- destination address type
SELECT "type" FROM "addresses" WHERE "id" = 348;

-- *** The Forgotten Gift ***

-- dest 728 Maple Place
-- source 109 Tileston Street

-- dest id = 4983
SELECT "id" FROM "addresses" WHERE "address" LIKE '%728 Maple Place%';
-- source id = 9873
SELECT "id" FROM "addresses" WHERE "address" LIKE '%109 Tileston Street%';

-- content is Flowers
-- were delivered to address id 9873
-- id 9523 contents
SELECT * FROM "packages" WHERE "from_address_id" = 9873;

-- driver id = 17
SELECT * FROM "scans" WHERE "package_id" = 9523;
-- driver's name
SELECT "name" FROM "drivers" WHERE "id" = 17;


