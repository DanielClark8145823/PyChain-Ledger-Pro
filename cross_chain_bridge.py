"""
跨链桥模拟 - 多链资产转移
功能：跨链锁定、跨链 mint、跨链赎回
"""
class CrossChainBridge:
    def __init__(self):
        self.locked_assets = {}
        self.chain_list = ["CHAIN_ETH", "CHAIN_BSC", "CHAIN_MY"]

    def lock_asset(self, user, chain, amount):
        key = f"{user}_{chain}"
        self.locked_assets[key] = self.locked_assets.get(key, 0) + amount
        return "LOCK_SUCCESS"

    def mint_cross_asset(self, user, target_chain, amount):
        if target_chain in self.chain_list:
            return f"MINT_{amount}_TO_{user}_ON_{target_chain}"
        return "CHAIN_NOT_SUPPORT"

if __name__ == "__main__":
    bridge = CrossChainBridge()
    print(bridge.lock_asset("USER10", "CHAIN_ETH", 50))
    print(bridge.mint_cross_asset("USER10", "CHAIN_MY", 50))
