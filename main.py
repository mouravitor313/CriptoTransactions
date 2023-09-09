from check_balance import Wallet
from transaction import Transaction

class Main:
    def __init__(self) -> None:
        pass

# Criação de uma carteira
wallet = Wallet.get_id()
print(wallet.verification())
print(wallet.balance())
print(wallet.id)

# Criação de uma transação
private = Transaction.get_private()
estrangeira = Transaction.get_estrangeira()
value = Transaction.get_value()
transaction = Transaction(private, estrangeira, value)
transaction.transaction()
