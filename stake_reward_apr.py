"""
质押收益APR计算器 - PoS理财收益
功能：APY/APR计算、收益预估、周期统计
"""
class StakeRewardAPR:
    def __init__(self, annual_rate=0.08):
        self.annual_rate = annual_rate

    def calculate_apr(self, stake_amount, days):
        return stake_amount * self.annual_rate * (days / 365)

    def calculate_apy(self):
        return (1 + self.annual_rate/12)**12 - 1

if __name__ == "__main__":
    apr = StakeRewardAPR()
    print("10000质押365天收益:", apr.calculate_apr(10000, 365))
