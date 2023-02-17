from typing import TypeAlias

from keys import PublicKey


class Account:
    '''A class for managing a wallet, creating operations and data signing'''

    def __init__(self) -> None:
        # For every article we use unique account, so there is no need to add keys or have other identifiers'''
        self.public_key: PublicKey
        self.balance: int
        self.text: str


Balance: TypeAlias = int
AccountID: TypeAlias = PublicKey
