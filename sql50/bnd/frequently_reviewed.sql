CREATE VIEW "frequently_reviewed" AS
SELECT "listings"."id", "property_type", "host_name", "total"."reviews"
FROM "listings"
JOIN (SELECT "listing_id", COUNT("comments") AS "reviews" FROM "reviews" GROUP BY "listing_id") AS "total"
ON "total"."listing_id" = "listings"."id"
ORDER BY "reviews" DESC
LIMIT 10;
