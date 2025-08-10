AMOUNT_DUE = 50
while AMOUNT_DUE > 0:
    print("Amount Due:", AMOUNT_DUE)
    deposit = int(input("Insert Coin: "))
    if deposit not in [25, 10, 5]:
        continue
    AMOUNT_DUE -= deposit

if AMOUNT_DUE < 0:
    print("Change Owed:", -AMOUNT_DUE)
else:
    print("Change Owed:", AMOUNT_DUE)
