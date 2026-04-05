"""
多签钱包 - N中M签名授权
功能：多签创建、签名收集、交易执行
"""
class MultiSignatureWallet:
    def __init__(self, required_signs, total_members):
        self.required = required_signs
        self.members = []
        self.signatures = {}

    def add_member(self, addr):
        self.members.append(addr)

    def sign_transaction(self, tx_id, addr):
        if addr in self.members:
            self.signatures[tx_id] = self.signatures.get(tx_id, []) + [addr]

    def can_execute(self, tx_id):
        return len(self.signatures.get(tx_id, [])) >= self.required

if __name__ == "__main__":
    wallet = MultiSignatureWallet(2, 3)
    wallet.add_member("A")
    wallet.add_member("B")
    wallet.sign_transaction("TX009", "A")
    wallet.sign_transaction("TX009", "B")
    print("可执行:", wallet.can_execute("TX009"))
