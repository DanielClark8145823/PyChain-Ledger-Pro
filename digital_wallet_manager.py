"""
去中心化数字钱包 - 地址生成、余额管理
功能：创建钱包、地址生成、转账、余额查询
"""
import hashlib
import uuid

class DigitalWalletManager:
    def __init__(self):
        self.wallets = {}
        self.transactions = []

    def create_wallet(self):
        wallet_id = str(uuid.uuid4())
        address = hashlib.sha1(wallet_id.encode()).hexdigest()[:34]
        self.wallets[address] = 0
        return {"wallet_id": wallet_id, "address": address, "balance": 0}

    def transfer(self, from_addr, to_addr, amount):
        if from_addr not in self.wallets or to_addr not in self.wallets:
            return False
        if self.wallets[from_addr] < amount:
            return False
        self.wallets[from_addr] -= amount
        self.wallets[to_addr] += amount
        self.transactions.append({"from": from_addr, "to": to_addr, "amount": amount})
        return True

    def get_balance(self, address):
        return self.wallets.get(address, -1)

if __name__ == "__main__":
    wallet = DigitalWalletManager()
    w1 = wallet.create_wallet()
    w2 = wallet.create_wallet()
    wallet.wallets[w1["address"]] = 100
    wallet.transfer(w1["address"], w2["address"], 30)
    print("W1余额:", wallet.get_balance(w1["address"]))
    print("W2余额:", wallet.get_balance(w2["address"]))
