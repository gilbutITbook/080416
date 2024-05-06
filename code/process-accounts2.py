import re
import sys
import monkey_plus  # noqa W0611

def get_5k_balances(rows):
    for row in rows:
        if re.match(r"5\d{3}\.\d{2}", row):
            balance, account_num, owner = row.split(",")
            yield (f"Account: {account_num}\n"
                   f"  Owner: {owner.strip()}\n"
                   f"Balance: ${float(balance):,.2f}\n")

# ... 더 많은 함수 ...

if __name__ == "__main__":
    for account in get_5k_balances(open(sys.argv[1])):
        print(account)
