from check_balance import Wallet # import the Wallet class from the check_balance module
from web3 import Web3 # import the Web3 library
import requests # import the requests library

sepolia_url = "https://eth-sepolia.g.alchemy.com/v2/pvpIq7da_oW19Vyvv0lJaQ2XlYQpskIa" # link to the infura service with the api key to connect to the ethereum blockchain
web3 = Web3(Web3.HTTPProvider(sepolia_url)) # access the url and transform it into a variable for easier access

class Transaction(): # define a class for a transaction
    def __init__(self, private, estrangeira, value): # define the constructor method
        self.private = private # assign the private parameter to the instance attribute
        self.estrangeira = estrangeira # assign the estrangeira parameter to the instance attribute
        self.value = value # assign the value parameter to the instance attribute

    @classmethod # use a decorator to indicate that this is a class method
    def get_private(cls): # define a class method for getting the private key from the user input
        private = input('Enter your private key:\n') # prompt the user to enter their private key
        return cls(private)    

    @classmethod # use a decorator to indicate that this is a class method
    def get_estrangeira(cls): # define a class method for getting the public id from the user input
        estrangeira = input('Enter the key:\n') # prompt the user to enter their public id
        return cls(estrangeira)

    @classmethod # use a decorator to indicate that this is a class method
    def get_value(cls): # define a class method for getting the transaction value from the user input
        value = float(input('Enter the value of transaction:\n')) # prompt the user to enter their transaction value and convert it to a float
        return value

    def transaction(self): # define a method for performing a transaction
        wallet = Wallet.get_id() # create a wallet object using the class method
        id = wallet.id # get the id of the wallet object
        wallet.balance() # check the balance of the wallet object
        account_1 = id  # assign the id of the wallet object to account_1 
        account_2 = self.estrangeira # assign estrangeira to account_2 
        private_key = self.private # assign private to private_key

        nonce = web3.eth.get_transaction_count(account_1) # get the nonce for account_1 using web3 library
        print("Nonce:", nonce) 

        tx = {  # build a transaction dictionary 
            'nonce': nonce, 
            'to': account_2, 
            'value': web3.to_wei(self.value, 'ether'), 
            'gas': 2000000, 
            'gasPrice': web3.to_wei('50', 'gwei') 
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)  # sign the transaction using web3 library

        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)  # send raw transaction using web3 library and get transaction hash

        print("Transaction Hash:", tx_hash.hex())  # print transaction hash in hexadecimal format

