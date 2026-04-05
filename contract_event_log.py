"""
智能合约事件日志 - 链上事件监听
功能：事件触发、日志存储、事件查询
"""
class ContractEventLog:
    def __init__(self):
        self.events = []

    def emit_event(self, contract, event_name, data):
        self.events.append({
            "contract": contract,
            "event": event_name,
            "data": data
        })

    def query_events(self, contract, event_name):
        return [e for e in self.events if e["contract"] == contract and e["event"] == event_name]

if __name__ == "__main__":
    log = ContractEventLog()
    log.emit_event("Token", "Transfer", {"from": "A", "to": "B"})
    print(log.query_events("Token", "Transfer"))
