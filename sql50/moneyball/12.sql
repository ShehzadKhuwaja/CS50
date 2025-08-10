SELECT "first_name", "last_name" FROM
(
    SELECT "first_name", "last_name" FROM "players"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    JOIN "performances" ON "performances"."year" = "salaries"."year" AND "performances"."player_id" = "salaries"."player_id"
    WHERE "RBI" != 0 AND "salaries"."year" = 2001
    ORDER BY "salary"/"RBI"
    LIMIT 10
) AS "low_rbi"
INTERSECT
SELECT "first_name", "last_name" FROM
(
    SELECT "first_name", "last_name" FROM "players"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    JOIN "performances" ON "performances"."year" = "salaries"."year" AND "performances"."player_id" = "salaries"."player_id"
    WHERE "H" != 0 AND "salaries"."year" = 2001
    ORDER BY "salary"/"H"
    LIMIT 10
) AS "low_h"
ORDER BY "last_name";