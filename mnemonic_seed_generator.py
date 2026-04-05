"""
助记词钱包种子 - BIP39简化版
功能：随机种子、助记词生成、密钥推导
"""
import random
import hashlib

class MnemonicSeedGenerator:
    WORDS = ["apple", "banana", "cat", "dog", "egg", "fish", "goat", "horse"]

    @staticmethod
    def generate_seed():
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    @staticmethod
    def generate_mnemonic():
        return " ".join(random.choice(MnemonicSeedGenerator.WORDS) for _ in range(12))

if __name__ == "__main__":
    print("助记词:", MnemonicSeedGenerator.generate_mnemonic())
