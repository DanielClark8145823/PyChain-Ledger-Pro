"""
节点验证器资格检查 - 作恶惩罚
功能：验证节点状态、作恶标记、惩罚机制
"""
class NodeValidatorCheck:
    def __init__(self):
        self.validators = {}
        self.blacklist = []

    def register_validator(self, addr, stake):
        self.validators[addr] = {"stake": stake, "score": 100}

    def punish_evil(self, addr):
        if addr in self.validators:
            self.validators[addr]["score"] -= 50
            if self.validators[addr]["score"] <= 0:
                self.blacklist.append(addr)

    def is_qualified(self, addr):
        return addr not in self.blacklist

if __name__ == "__main__":
    check = NodeValidatorCheck()
    check.register_validator("V01", 5000)
    check.punish_evil("V01")
    print("是否合格:", check.is_qualified("V01"))
