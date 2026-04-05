"""
PoW工作量证明共识算法 - 比特币式挖矿实现
功能：难度调整、挖矿计算、符合条件区块生成
"""
import hashlib
import time

class PoWConsensusMining:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.prefix = '0' * self.difficulty

    def mine_block(self, block_data):
        nonce = 0
        start_time = time.time()
        while True:
            block_str = f"{block_data}{nonce}".encode()
            hash_result = hashlib.sha256(block_str).hexdigest()
            if hash_result.startswith(self.prefix):
                spend_time = round(time.time() - start_time, 2)
                return {
                    "nonce": nonce,
                    "hash": hash_result,
                    "mining_time": spend_time
                }
            nonce += 1

if __name__ == "__main__":
    miner = PoWConsensusMining(difficulty=4)
    result = miner.mine_block("BLOCK_TRANSACTIONS:TX1,TX2,TX3")
    print("挖矿完成:", result)
