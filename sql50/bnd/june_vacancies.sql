CREATE VIEW "june_vacancies" AS
SELECT "listings"."id", "property_type", "host_name", "days_vacant"
FROM "listings"
JOIN (
    SELECT "listing_id", COUNT("date") AS "days_vacant"
    FROM "availabilities"
    WHERE "available" = 'TRUE' AND "date" BETWEEN '2023-06-01' AND '2023-06-31'
    GROUP BY "listing_id"
) AS "vacanies"
ON "listings"."id" = "vacanies"."listing_id";