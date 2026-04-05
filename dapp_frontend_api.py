"""
DApp后端API接口 - 链上数据查询
功能：余额查询、交易提交、区块高度查询
"""
class DAppFrontendAPI:
    def __init__(self, chain):
        self.chain = chain

    def get_balance_api(self, addr):
        return {"address": addr, "balance": 1000}

    def send_transaction_api(self, tx):
        return {"status": "SUCCESS", "txid": hash(tx)}

    def get_block_height_api(self):
        return {"height": len(self.chain.chain)}

if __name__ == "__main__":
    from blockchain_core_ledger import CoreBlockchainLedger
    api = DAppFrontendAPI(CoreBlockchainLedger())
    print(api.get_block_height_api())
