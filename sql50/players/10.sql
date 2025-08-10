SELECT AVG("height") as "Average Height" FROM "players"
WHERE "birth_country" = 'USA' AND "bats" IS NOT NULL
GROUP BY "bats"
ORDER BY "first_name";