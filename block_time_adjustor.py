"""
区块出块时间调节器 - 稳定出块速度
功能：根据网络调整难度、稳定区块间隔
"""
import time

class BlockTimeAdjustor:
    def __init__(self, target_interval=10):
        self.target_interval = target_interval
        self.difficulty = 3

    def adjust_difficulty(self, last_block_time):
        spend = time.time() - last_block_time
        if spend < self.target_interval * 0.8:
            self.difficulty += 1
        elif spend > self.target_interval * 1.2:
            self.difficulty = max(1, self.difficulty - 1)
        return self.difficulty

if __name__ == "__main__":
    adjustor = BlockTimeAdjustor()
    print("新难度:", adjustor.adjust_difficulty(time.time() - 5))
