"""
恶意交易检测器 - 双花/重放防护
功能：双花检测、交易去重、风险标记
"""
class MaliciousTxDetector:
    def __init__(self):
        self.processed_tx = set()

    def is_double_spend(self, tx):
        return tx["from"] in self.processed_tx

    def check_replay(self, tx_id):
        if tx_id in self.processed_tx:
            return True
        self.processed_tx.add(tx_id)
        return False

if __name__ == "__main__":
    detect = MaliciousTxDetector()
    print("重放:", detect.check_replay(12345))
