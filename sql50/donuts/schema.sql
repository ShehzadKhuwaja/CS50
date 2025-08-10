CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "price_per_unit" NUMERIC NOT NULL,
    "unit" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "is_gluten_free" TEXT NOT NULL CHECK("is_gluten_free" IN ("true", "false")),
    "price" NUMERIC NOT NULL CHECK("price" != 0),
    PRIMARY KEY("id")
);

CREATE TABLE "composes" (
    "donut" INTEGER,
    "ingredient" INTEGER,
    PRIMARY KEY("donut", "ingredient"),
    FOREIGN KEY("donut") REFERENCES "donuts"("id"),
    FOREIGN KEY("ingredient") REFERENCES "ingredient"("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "number" INTEGER NOT NULL UNIQUE,
    "customer" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("customer") REFERENCES "customers"("id")
);

CREATE TABLE "order_has_donuts" (
    "order_id" INTEGER,
    "donut_id" INTEGER,
    "quantity" INTEGER NOT NULL,
    PRIMARY KEY("order_id", "donut_id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    PRIMARY KEY("id")
);