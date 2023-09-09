from check_balance import Wallet
from transaction import Transaction
from time import sleep
from os import system


class Main:
    def __init__(self) -> None:
        pass

    def main(self):
        while True:
            wallet = Wallet.get_id()
            system('cls')
            balance = wallet.balance()
            print(f'Your current balance is: {balance} ETH')
            choice = input('Do you want to make a transaction? [Y/N]').upper()
            if choice == 'Y':
                private = Transaction.get_private()
                estrangeira = Transaction.get_estrangeira()
                value = Transaction.get_value()
                if value > balance:
                    print('Error: Insufficient funds in wallet for transaction.')
                    sleep(2)
                else:
                    transaction = Transaction(private, estrangeira, value)
                    transaction.transaction()
                    sleep(2)
            else:
                break



# verifications:
# print(wallet.verification())
# print(wallet.id)






