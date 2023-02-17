from account import Account
from keys import KeyPair
from operation import Operation
from signature import Signature
from transaction import Transaction


class Wallet:
    '''Class to create and manage keys'''

    def __init__(self) -> None:
        self.accounts: list[KeyPair]
        self.transactions: list[Transaction]  # or dict[Hash, Transaction]

    def generate_new_key_pair(self) -> None:
        '''Generate a new key pair.
        Send the public key to be added to the user's account via a transaction.
        Write the private key to a separate secure storage.
        In addition, it can initiate a search for transactions related to the new public key.
        '''

    def create_transaction(self) -> None:
        '''Forms, complete, sign, initiate the propagation of a transaction
        through a full network node.'''

    def get_balance(self) -> float:
        '''Access the transaction history of the current wallet,
        calculate the current balance and return as a number.
        Or make an appropriate request to the full node of the network
        to obtain the current balance by accountID'''
        raise NotImplementedError

    def sign_data(self, data: bytes) -> Signature:
        '''Receive transaction (or any other data), private key and return the signature for that data.'''
        raise NotImplementedError

    def create_operation(self, recipient: Account) -> Operation:
        '''Form the body of the transaction, sign that transaction body and send it to some full node in the network.'''
        raise NotImplementedError
