"""
PoS权益证明共识算法 - 无需挖矿的节能共识
功能：质押记账、验证者选举、区块生成权限分配
"""
import random

class PoSStakingConsensus:
    def __init__(self):
        self.stakers = {}

    def add_staker(self, address, stake_amount):
        self.stakers[address] = stake_amount

    def elect_validator(self):
        total_stake = sum(self.stakers.values())
        if total_stake == 0:
            return None
        rand = random.uniform(0, total_stake)
        current = 0
        for addr, stake in self.stakers.items():
            current += stake
            if current >= rand:
                return addr
        return None

    def generate_block_by_validator(self, validator):
        if validator in self.stakers:
            return f"VALIDATOR_{validator}_GENERATED_NEW_BLOCK"
        return "NO_PERMISSION"

if __name__ == "__main__":
    pos = PoSStakingConsensus()
    pos.add_staker("NODE001", 1000)
    pos.add_staker("NODE002", 3000)
    pos.add_staker("NODE003", 5000)
    validator = pos.elect_validator()
    print("当选验证者:", validator)
    print(pos.generate_block_by_validator(validator))
