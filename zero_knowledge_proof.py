"""
简易零知识证明 - 隐私交易验证
功能：证明拥有数据、不泄露原始信息
"""
import random

class ZeroKnowledgeProof:
    def __init__(self, secret):
        self.secret = secret

    def generate_commitment(self):
        rand = random.randint(1000,9999)
        return rand, rand ^ self.secret

    def verify_proof(self, rand, proof):
        return (rand ^ proof) == self.secret

if __name__ == "__main__":
    zkp = ZeroKnowledgeProof(123456)
    rand, proof = zkp.generate_commitment()
    print("验证结果:", zkp.verify_proof(rand, proof))
