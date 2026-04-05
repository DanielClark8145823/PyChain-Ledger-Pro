"""
区块奖励分发 - 矿工/验证者激励
功能：奖励计算、分配、减半机制
"""
class RewardDistribution:
    def __init__(self, base_reward=50):
        self.base_reward = base_reward
        self.halving_cycle = 210000

    def get_reward(self, height):
        halvings = height // self.halving_cycle
        return self.base_reward / (2 ** halvings)

    def distribute(self, node_list, reward):
        per_node = reward / len(node_list)
        return {n: per_node for n in node_list}

if __name__ == "__main__":
    reward = RewardDistribution()
    print("高度100万奖励:", reward.get_reward(1000000))
