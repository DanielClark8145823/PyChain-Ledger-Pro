"""
默克尔树交易验证 - 区块链高效交易校验
功能：构建默克尔树、生成根哈希、交易存在性证明
"""
import hashlib

class MerkleTreeTransaction:
    def __init__(self, transactions):
        self.transactions = [self.hash_tx(tx) for tx in transactions]
        self.root = self.build_merkle_root()

    def hash_tx(self, tx):
        return hashlib.sha256(tx.encode()).hexdigest()

    def build_merkle_root(self):
        nodes = self.transactions.copy()
        while len(nodes) > 1:
            temp = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1] if i+1 < len(nodes) else left
                combined = self.hash_tx(left + right)
                temp.append(combined)
            nodes = temp
        return nodes[0] if nodes else None

    def verify_transaction(self, tx):
        return self.hash_tx(tx) in self.transactions

if __name__ == "__main__":
    txs = ["TX001", "TX002", "TX003", "TX004"]
    mt = MerkleTreeTransaction(txs)
    print("默克尔根:", mt.root)
    print("TX002存在:", mt.verify_transaction("TX002"))
