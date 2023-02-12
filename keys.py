'''A module for working with keys.'''
from pathlib import Path
from typing import NamedTuple, Tuple, TypeAlias

import click
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat
)

PublicKey: TypeAlias = Ed25519PublicKey
PrivateKey: TypeAlias = Ed25519PrivateKey

def load_public_key(path: Path) -> PublicKey:
    '''Load public key from file.'''
    with path.open('rb') as fl:
        return PublicKey.from_public_bytes(fl.read())

class KeyPair(NamedTuple):
    # let private key hide its own secrets
    private_key: PrivateKey
    public_key: PublicKey

    @classmethod
    def gen_key_pair(cls) -> 'KeyPair':
        private_key = PrivateKey.generate()
        return cls(private_key, private_key.public_key())

    def save(self, path: Path) -> Tuple[Path, Path]:
        '''Save private and public keys to files.
        Does not use encryption for simplicity.'''

        with path.open('wb') as fl:
            bts = self.private_key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption())
            fl.write(bts)

        # stupid typechecker thinks that str != Literal[str]
        public_key_path = path.with_suffix(path.suffix + str('.pub'))
        with public_key_path.open('wb') as fl:
            bts = self.public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
            fl.write(bts)

        return path, public_key_path


    @classmethod
    def load(cls, path: Path) -> 'KeyPair':
        with path.open('rb') as fl:
            private_key = PrivateKey.from_private_bytes(fl.read())
        return cls(private_key, private_key.public_key())


@click.group(help='Manage keys')
def keys():
    pass


@keys.command(help='Generate key pair and save it to files')
def generate():
    print('Generating Key Pair...')
    default_filename = 'secret.key'
    filename = input(f'Enter file in which to save the key ({default_filename}):')
    filename = filename or default_filename
    key_pair = KeyPair.gen_key_pair()
    priv_path, pub_path = key_pair.save(Path(filename))
    print('Your private key has been saved in', priv_path)
    print('Your public key has been saved in', pub_path)
