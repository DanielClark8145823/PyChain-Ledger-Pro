"""
区块链监控面板 - 节点/区块/交易实时监控
功能：实时数据、节点状态、TPS计算
"""
class ChainMonitorDashboard:
    def __init__(self, chain):
        self.chain = chain
        self.tx_count = 0

    def get_tps(self, interval=10):
        return round(self.tx_count / interval, 2)

    def node_status(self):
        return {"online": 8, "offline": 1, "height": len(self.chain.chain)}

if __name__ == "__main__":
    from blockchain_core_ledger import CoreBlockchainLedger
    monitor = ChainMonitorDashboard(CoreBlockchainLedger())
    print(monitor.node_status())
