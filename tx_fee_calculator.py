"""
交易手续费计算器 - 动态费率
功能：按数据大小计算手续费、优先打包排序
"""
class TxFeeCalculator:
    def __init__(self, base_fee=1):
        self.base_fee = base_fee

    def calculate_fee(self, tx_size, gas_price=1):
        return self.base_fee * tx_size * gas_price

    def sort_by_fee(self, tx_list):
        return sorted(tx_list, key=lambda x: x["fee"], reverse=True)

if __name__ == "__main__":
    fee = TxFeeCalculator()
    print("手续费:", fee.calculate_fee(20))
