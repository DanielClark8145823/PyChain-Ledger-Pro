"""
区块数据加密器 - 区块内容AES加密存储
功能：加密区块、解密区块、隐私保护
"""
from cryptography.fernet import Fernet

class BlockDataEncryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_block(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_block(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    enc = BlockDataEncryptor()
    encrypted = enc.encrypt_block("PRIVATE_BLOCK_DATA")
    print("解密:", enc.decrypt_block(encrypted))
