"""
Web3 RPC客户端 - 链节点远程调用
功能：远程查询、交易发送、合约调用模拟
"""
class Web3RPCClient:
    def __init__(self, node_url):
        self.node_url = node_url

    def rpc_call(self, method, params):
        return {"jsonrpc": "2.0", "id": 1, "result": {"method": method, "params": params}}

    def get_chain_id(self):
        return self.rpc_call("eth_chainId", [])

if __name__ == "__main__":
    rpc = Web3RPCClient("http://localhost:8545")
    print(rpc.get_chain_id())
