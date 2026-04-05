"""
ERC20标准代币合约 - 同质化代币实现
功能：发行、转账、授权、余额、总量查询
"""
class ERC20StandardToken:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}
        self.allowance = {}

    def mint(self, address, amount):
        self.balances[address] = self.balances.get(address, 0) + amount
        self.total_supply += amount

    def transfer(self, from_addr, to_addr, amount):
        if self.balances.get(from_addr, 0) < amount:
            return False
        self.balances[from_addr] -= amount
        self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
        return True

    def balance_of(self, address):
        return self.balances.get(address, 0)

if __name__ == "__main__":
    token = ERC20StandardToken("MyChainToken", "MCT", 1000000)
    token.mint("USER001", 5000)
    token.transfer("USER001", "USER002", 1000)
    print("USER001余额:", token.balance_of("USER001"))
