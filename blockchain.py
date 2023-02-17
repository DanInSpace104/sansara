from account import Account, Balance
from block import Block
from transaction import Transaction


class Blockchain:
    '''A class that allows to form a blockchain, a database of coins and existing transactions.'''

    def __init__(self) -> None:
        self.coin_database: dict[Account, Balance]
        self.block_history: list[Block]
        self.tx_database: list[Transaction]
        self.faucet_coins: int

    def init_blockchain(self) -> None:
        '''Create genesis block and add to history'''

    def get_token_from_faucet(self, account: Account, amount: int) -> None:
        '''Get coins from the faucet.
        Update the state of coin_database and the balance of the account.'''
