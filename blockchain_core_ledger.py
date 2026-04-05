"""
区块链核心账本 - 去中心化不可篡改账本实现
功能：创建创世区块、添加区块、哈希校验、账本完整性验证
"""
import hashlib
import time
import json

class CoreBlockchainLedger:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "GENESIS_BLOCK_CHAIN_INIT",
            "previous_hash": "0",
            "nonce": 8888,
            "hash": self.calculate_hash(0, time.time(), "GENESIS_BLOCK_CHAIN_INIT", "0", 8888)
        }
        self.chain.append(genesis_block)

    def calculate_hash(self, index, timestamp, data, previous_hash, nonce):
        block_string = f"{index}{timestamp}{data}{previous_hash}{nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_new_block(self, data, nonce):
        last_block = self.chain[-1]
        new_block = {
            "index": last_block["index"] + 1,
            "timestamp": time.time(),
            "data": data,
            "previous_hash": last_block["hash"],
            "nonce": nonce,
            "hash": self.calculate_hash(last_block["index"] + 1, time.time(), data, last_block["hash"], nonce)
        }
        self.chain.append(new_block)
        return new_block

    def verify_ledger_integrity(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current["hash"] != self.calculate_hash(current["index"], current["timestamp"], current["data"], current["previous_hash"], current["nonce"]):
                return False
            if current["previous_hash"] != previous["hash"]:
                return False
        return True

if __name__ == "__main__":
    ledger = CoreBlockchainLedger()
    ledger.add_new_block("USER_TRANSFER_100_TOKEN", 12345)
    ledger.add_new_block("NODE_VALIDATION_COMPLETE", 67890)
    print(json.dumps(ledger.chain, indent=2))
    print("账本完整性:", ledger.verify_ledger_integrity())
