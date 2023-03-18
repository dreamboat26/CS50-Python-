def main():

    change(get_coin())



def get_coin():

    debt =50

    while debt> 0:

        print(f"Amount Due: {debt}")

        money = int(input("Insert Coin: ").strip())

        if money == 5 or money == 10 or money == 25:

            debt = debt - money

        else:

            continue

        if debt<= 0:

            break

    return debt



def change(debt):
    if debt == 0:
        print("Change Owed: 0")
    else:
        print(f"Change Owed: {-1*debt}")



main()