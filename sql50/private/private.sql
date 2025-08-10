CREATE TABLE "secret_sentences" (
    "id",
    "sentence" TEXT,
    "clue" TEXT DEFAULT NULL,
    PRIMARY KEY("id")
);

INSERT INTO "secret_sentences" ("id", "sentence")
SELECT "id", "sentence" FROM "sentences"
WHERE "id" IN (14, 114, 618, 630, 932, 2230, 2346, 3041);

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 98, 4) FROM "sentences"
    WHERE "id" = 14
) WHERE "id" = 14;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 3, 5) FROM "sentences"
    WHERE "id" = 114
) WHERE "id" = 114;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 72, 9) FROM "sentences"
    WHERE "id" = 618
) WHERE "id" = 618;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 7, 3) FROM "sentences"
    WHERE "id" = 630
) WHERE "id" = 630;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 12, 5) FROM "sentences"
    WHERE "id" = 932
) WHERE "id" = 932;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 50, 7) FROM "sentences"
    WHERE "id" = 2230
) WHERE "id" = 2230;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 44, 10) FROM "sentences"
    WHERE "id" = 2346
) WHERE "id" = 2346;

UPDATE "secret_sentences"
SET "clue" = (
    SELECT substr("sentence", 14, 5) FROM "sentences"
    WHERE "id" = 3041
) WHERE "id" = 3041;

CREATE VIEW "message" AS
SELECT "clue" AS "phrase" FROM "secret_sentences";
