"""
交易池Mempool - 待打包交易管理
功能：添加交易、剔除交易、获取可打包交易列表
"""
import time

class TransactionPoolMempool:
    def __init__(self):
        self.pool = []

    def add_transaction(self, tx_data):
        transaction = {
            "tx_id": hash(tx_data),
            "data": tx_data,
            "time": time.time()
        }
        self.pool.append(transaction)
        return True

    def get_packable_transactions(self, max_count=10):
        return self.pool[:max_count]

    def remove_transactions(self, tx_ids):
        self.pool = [tx for tx in self.pool if tx["tx_id"] not in tx_ids]

if __name__ == "__main__":
    pool = TransactionPoolMempool()
    pool.add_transaction("A->B:10")
    pool.add_transaction("C->D:25")
    print("可打包交易:", pool.get_packable_transactions())
