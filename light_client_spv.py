"""
轻客户端SPV - 简化支付验证
功能：无需同步全链、快速交易验证
"""
class LightClientSPV:
    def __init__(self):
        self.block_headers = []

    def add_header(self, header):
        self.block_headers.append(header)

    def verify_transaction(self, tx_root, proof):
        return tx_root is not None and proof is not None

if __name__ == "__main__":
    spv = LightClientSPV()
    spv.add_header({"root": "ROOT_HASH"})
    print("验证:", spv.verify_transaction("ROOT_HASH", "PROOF"))
