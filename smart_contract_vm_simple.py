"""
简易智能合约虚拟机 - 链上代码执行环境
功能：合约部署、函数调用、状态存储
"""
class SimpleSmartContractVM:
    def __init__(self):
        self.contracts = {}
        self.storage = {}

    def deploy_contract(self, contract_name, code):
        self.contracts[contract_name] = code
        self.storage[contract_name] = {}
        return f"CONTRACT_{contract_name}_DEPLOYED"

    def execute_contract(self, contract_name, func, params):
        if contract_name not in self.contracts:
            return "CONTRACT_NOT_FOUND"
        try:
            if func == "set":
                key, val = params
                self.storage[contract_name][key] = val
                return "SET_SUCCESS"
            elif func == "get":
                key = params[0]
                return self.storage[contract_name].get(key, "NULL")
        except:
            return "EXECUTE_FAILED"

if __name__ == "__main__":
    vm = SimpleSmartContractVM()
    vm.deploy_contract("TokenContract", "TOKEN_MANAGE")
    print(vm.execute_contract("TokenContract", "set", ["total", 1000000]))
    print(vm.execute_contract("TokenContract", "get", ["total"]))
