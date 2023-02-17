from typing import TypeAlias

from transaction import Transaction


class Block:
    '''A class that allows to form a block with transactions.'''

    def __init__(self, prev_hash: bytes, transactions: list[Transaction]) -> None:
        self.prev_hash = prev_hash
        self.transacions = transactions
        self.block_id = self.generate_block_id()

    def generate_block_id(self) -> bytes:
        raise NotImplementedError
