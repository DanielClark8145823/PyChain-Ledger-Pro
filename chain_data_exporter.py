"""
区块链数据导出工具 - 数据备份/分析
功能：导出JSON、统计信息、高度查询
"""
import json

class ChainDataExporter:
    @staticmethod
    def export_chain(chain, filename="chain_backup.json"):
        with open(filename, "w") as f:
            json.dump(chain, f, indent=2)
        return "EXPORT_SUCCESS"

    @staticmethod
    def get_stats(chain):
        return {
            "blocks": len(chain),
            "last_height": len(chain)-1
        }

if __name__ == "__main__":
    from blockchain_core_ledger import CoreBlockchainLedger
    print(ChainDataExporter.get_stats(CoreBlockchainLedger().chain))
