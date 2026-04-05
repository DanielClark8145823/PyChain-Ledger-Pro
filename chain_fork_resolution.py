"""
区块链分叉解决 - 最长链规则
功能：分叉检测、链选择、无效链丢弃
"""
class ChainForkResolution:
    def __init__(self):
        self.chains = {}

    def add_chain(self, chain_name, chain_length):
        self.chains[chain_name] = chain_length

    def select_main_chain(self):
        if not self.chains:
            return None
        return max(self.chains, key=self.chains.get)

    def drop_fork_chains(self, main_chain):
        forks = [k for k in self.chains if k != main_chain]
        for f in forks:
            del self.chains[f]
        return forks

if __name__ == "__main__":
    fork = ChainForkResolution()
    fork.add_chain("CHAIN_A", 120)
    fork.add_chain("CHAIN_B", 125)
    main = fork.select_main_chain()
    print("主链:", main)
    print("丢弃分叉:", fork.drop_fork_chains(main))
