"""
区块链预言机 - 链下数据上链
功能：数据请求、数据提交、数据验证
"""
class OracleMachineChainlink:
    def __init__(self):
        self.requests = {}
        self.data = {}

    def request_data(self, req_id, query):
        self.requests[req_id] = query

    def submit_data(self, req_id, result):
        self.data[req_id] = result

    def get_onchain_data(self, req_id):
        return self.data.get(req_id, "NO_DATA")

if __name__ == "__main__":
    oracle = OracleMachineChainlink()
    oracle.request_data("REQ01", "BTC_PRICE")
    oracle.submit_data("REQ01", 60000)
    print("链上价格:", oracle.get_onchain_data("REQ01"))
