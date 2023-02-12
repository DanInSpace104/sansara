from pathlib import Path

import click
from cryptography.exceptions import InvalidSignature

from keys import KeyPair, PrivateKey, PublicKey, load_public_key
from utils import ReadableFile


class Signature:

    @staticmethod
    def sign_data(private_key: PrivateKey, data: bytes) -> bytes:
        return private_key.sign(data)

    @staticmethod
    def verify(signature: bytes, data: bytes, public_key: PublicKey) -> bool:
        try:
            public_key.verify(signature, data)
        except InvalidSignature:
            return False
        return True

    @staticmethod
    def sign_file(private_key: PrivateKey, path: Path) -> bytes:
        with path.open('rb') as fl:
            return Signature.sign_data(private_key, fl.read())

    @staticmethod
    def verify_file(signature: bytes, path: Path, public_key: PublicKey) -> bool:
        with path.open('rb') as fl:
            return Signature.verify(signature, fl.read(), public_key)


@click.group(help='Sign and verify files')
def signature():
    pass


@signature.command(help='Sign file with private key file')
@click.argument('private_key_file', type=ReadableFile)
@click.argument('datafile', type=ReadableFile)
def sign_file(private_key_file: Path, datafile: Path):
    priv, _ = KeyPair.load(private_key_file)
    print(Signature.sign_file(priv, datafile).hex())

@signature.command(help='Verify file with signature')
@click.argument('signature')
@click.argument('datafile', type=ReadableFile)
@click.argument('public_key_file', type=ReadableFile)
def verify_file(signature: str, datafile: Path, public_key_file: Path):
    public_key = load_public_key(public_key_file)
    try:
        result = Signature.verify_file(bytes.fromhex(signature), datafile, public_key)
    except ValueError:
        result = False
    if result:
        print('Signature is valid')
    else:
        print('Invalid signature!')


def test_signature():
    data = b'aishoetna;isuenht;asuenht'
    priv, pub = KeyPair.gen_key_pair()
    sign = Signature.sign_data(priv, data)

    assert Signature.verify(sign, data, pub)

    data = b'ashtasht'
    assert Signature.verify(sign, data, pub) == False
