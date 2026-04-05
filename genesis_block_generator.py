"""
创世区块自定义生成器 - 链初始化工具
功能：自定义创世节点、初始分配、初始参数
"""
import hashlib
import time

class GenesisBlockGenerator:
    @staticmethod
    def create(allocations, chain_params):
        genesis = {
            "index": 0,
            "time": time.time(),
            "allocations": allocations,
            "params": chain_params,
            "hash": hashlib.sha256(str(time.time()).encode()).hexdigest()
        }
        return genesis

if __name__ == "__main__":
    gene = GenesisBlockGenerator.create({"NODE01": 10000}, {"version": 1})
    print(gene)
