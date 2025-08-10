SELECT "schools"."name", "districts"."name" FROM "schools"
JOIN "districts" ON "districts"."id" = "schools"."district_id"
JOIN "staff_evaluations" ON "staff_evaluations"."district_id" = "districts"."id"
ORDER BY "unsatisfactory" DESC
LIMIT 10;