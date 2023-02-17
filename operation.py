from account import Account
from signature import Signature


class Operation:
    '''A class that allows creating a payment operation.'''

    def __init__(self) -> None:
        self.sender: Account
        self.receiver: Account
        self.amount: float
        self.signature: Signature

    def verify(self) -> bool:
        raise NotImplementedError


def verify_operation(operation: Operation) -> bool:
    return operation.verify()
