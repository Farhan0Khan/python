def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due : {amount_due}")
        insert_coin = int(input('Insert Coin : '))
        amount_due = check_due(insert_coin, amount_due)
    print('Change owed', amount_due)

def check_due(coin, due):
    due = due - coin
    return due


main()