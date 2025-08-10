CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "people_connections" (
    "id" INTEGER,
    "user_a" INTEGER,
    "user_b" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_a") REFERENCES "users"("id"),
    FOREIGN KEY("user_b") REFERENCES "users"("id"),
    CHECK(user_a != user_b)
);

CREATE TABLE "school_connections" (
    "id" INTEGER,
    "user" INTEGER,
    "school" INTEGER,
    "start_date" NUMERIC,
    "end_date" NUMERIC,
    "degree_type" TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("user") REFERENCES "users"("id"),
    FOREIGN KEY("school") REFERENCES "schools"("id")
);

CREATE TABLE "company_connections" (
    "id" INTEGER,
    "user" INTEGER,
    "company" INTEGER,
    "start_date" NUMERIC,
    "end_date" NUMERIC,
    "title" TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("user") REFERENCES "users"("id"),
    FOREIGN KEY("company") REFERENCES "companies"("id")
);