SELECT "city", COUNT("name") AS "Total Public Schools" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
ORDER BY "Total Public Schools" DESC, "city"
LIMIT 10;