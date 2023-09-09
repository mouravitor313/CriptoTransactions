from time import sleep # import the sleep function from the time module
from os import system # import the system function from the os module
from web3 import Web3 # import the Web3 library
sepolia_url = "https://eth-sepolia.g.alchemy.com/v2/pvpIq7da_oW19Vyvv0lJaQ2XlYQpskIa" # link to the infura service with the api key to connect to the ethereum blockchain
web3 = Web3(Web3.HTTPProvider(sepolia_url)) # access the url and transform it into a variable for easier access


class Wallet: # define a class for a wallet
    def __init__(self, id): # define the constructor method
        self.id = id # assign the id parameter to the instance attribute

    def verification(cls): # define a method for verifying the connection and block number
        print('Checking...') # print a message
        sleep(1) # wait for one second
        system('cls') # clear the screen
        return f'Is connected? {web3.is_connected()}\nBlock number: {web3.eth.block_number}' # return a formatted string with the connection status and block number

    def balance(self): # define a method for checking the balance of the wallet
            sleep(2) # wait for two seconds
            system('cls') # clear the screen
            balance = web3.eth.get_balance(self.id) # get the balance of the wallet using the web3 library
            return web3.from_wei(balance,"ether") # return the balance in ether units

    @classmethod # use a decorator to indicate that this is a class method
    def get_id(cls): # define a class method for getting the public id from the user input
        id = input('Enter your public id:\n') # prompt the user to enter their public id
        return cls(id) # return an instance of the class with the given id


