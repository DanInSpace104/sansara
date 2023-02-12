'''A module for working with keys.'''
from typing import NamedTuple, TypeAlias

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)

PublicKey: TypeAlias = Ed25519PublicKey
PrivateKey: TypeAlias = Ed25519PrivateKey


class KeyPair(NamedTuple):
    # let private key hide its own secrets
    private_key: PrivateKey
    public_key: PublicKey

    @classmethod
    def gen_key_pair(cls) -> 'KeyPair':
        private_key = Ed25519PrivateKey.generate()
        return cls(private_key, private_key.public_key())
