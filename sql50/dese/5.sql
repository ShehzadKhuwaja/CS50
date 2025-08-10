SELECT COUNT("name") AS "Total Public Schools", "city" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
HAVING "Total Public Schools" <= 3
ORDER BY "Total Public Schools" DESC, "city";