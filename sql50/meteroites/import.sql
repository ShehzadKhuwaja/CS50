CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT CHECK ("name" != ''),
    "class" TEXT CHECK ("nametype" != 'Relict'),
    "mass" NUMERIC,
    "discovery" TEXT CHECK ("discovery" IN ("Fell", "Found")),
    "year" NUMERIC CHECK ("year" != ''),
    "lat" NUMERIC CHECK ("lat" != ''),
    "long" NUMERIC CHECK ("long" != ''),
    PRIMARY KEY("id")
);

CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" TEXT,
    "discovery" TEXT,
    "year" TEXT,
    "lat" TEXT,
    "long" TEXT
);

.import --csv --skip 1 meteorites.csv meteorites_temp

UPDATE "meteorites_temp" SET "mass" = NULL WHERE "mass" = '';
UPDATE "meteorites_temp" SET "year" = NULL WHERE "year" = '';
UPDATE "meteorites_temp" SET "lat" = NULL WHERE "lat" = '';
UPDATE "meteorites_temp" SET "long" = NULL WHERE "long" = '';

UPDATE "meteorites_temp" SET "mass" = ROUND("mass", 2), "lat" = ROUND("lat", 2), "long" = ROUND("long", 2);

DELETE FROM "meteorites_temp" WHERE "nametype" = 'Relict';

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long" FROM "meteorites_temp"
ORDER BY "year", "name";

DROP TABLE "meteorites_temp";