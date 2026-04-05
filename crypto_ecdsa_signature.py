"""
ECDSA椭圆曲线数字签名 - 区块链交易签名核心
功能：生成密钥对、交易签名、签名验证、防篡改校验
"""
import ecdsa
import binascii

class ECDSACryptoSignature:
    def __init__(self):
        self.curve = ecdsa.SECP256k1  # 比特币/以太坊标准曲线

    def generate_key_pair(self):
        private_key = ecdsa.SigningKey.generate(curve=self.curve)
        public_key = private_key.get_verifying_key()
        return private_key, public_key

    def sign_transaction(self, private_key, transaction_data):
        signature = private_key.sign(transaction_data.encode('utf-8'))
        return binascii.hexlify(signature).decode()

    def verify_transaction(self, public_key, transaction_data, signature):
        try:
            sig = binascii.unhexlify(signature)
            return public_key.verify(sig, transaction_data.encode('utf-8'))
        except:
            return False

if __name__ == "__main__":
    crypto = ECDSACryptoSignature()
    priv, pub = crypto.generate_key_pair()
    tx_data = "FROM:A TO:B AMOUNT:50"
    sign = crypto.sign_transaction(priv, tx_data)
    print("交易签名:", sign)
    print("签名验证:", crypto.verify_transaction(pub, tx_data, sign))
