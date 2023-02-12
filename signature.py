from cryptography.exceptions import InvalidSignature

from keys import KeyPair, PrivateKey, PublicKey


class Signature():

    def __init__(self, private_key: PrivateKey, data: bytes) -> None:
        self.value = private_key.sign(data)

    @classmethod
    def sign_data(cls, private_key: PrivateKey, data: bytes) -> 'Signature':
        return cls(private_key, data)

    def verify(self, public_key: PublicKey, data: bytes) -> bool:
        try:
            public_key.verify(self.value, data)
        except InvalidSignature:
            return False
        return True

    def __str__(self) -> str:
        return str(self.value)


def test_signature():
    data = b'aishoetna;isuenht;asuenht'
    priv, pub = KeyPair.gen_key_pair()
    sign = Signature.sign_data(priv, data)

    assert sign.verify(pub, data)

    data = b'ashtasht'
    assert sign.verify(pub, data) == False
