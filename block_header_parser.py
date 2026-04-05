"""
区块头解析器 - 快速解析区块元数据
功能：哈希解析、时间戳、难度、前区块哈希
"""
class BlockHeaderParser:
    @staticmethod
    def parse(header):
        return {
            "height": header.get("index"),
            "hash": header.get("hash"),
            "prev_hash": header.get("previous_hash"),
            "time": header.get("timestamp")
        }

if __name__ == "__main__":
    header = {"index": 10, "hash": "ABC", "previous_hash": "DEF", "timestamp": 123456}
    print(BlockHeaderParser.parse(header))
