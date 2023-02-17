from account import AccountID
from operation import Operation


class Transaction:
    '''A class that allows to form a transaction containing user payments.'''

    def __init__(self) -> None:
        self.initiator: AccountID
        self.operations: list[Operation]
        self.nonce: int
