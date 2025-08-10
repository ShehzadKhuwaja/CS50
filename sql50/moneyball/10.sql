SELECT "first_name", "last_name", "salary", "salaries"."year", "HR" FROM "players"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
JOIN "performances" ON "performances"."year" = "salaries"."year" AND "performances"."player_id" = "salaries"."player_id"
ORDER BY "players"."id", "salaries"."year" DESC, "HR" DESC, "salary" DESC;