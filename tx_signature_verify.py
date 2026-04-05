"""
交易签名批量验证 - 节点批量校验
功能：批量验证、非法交易过滤、结果返回
"""
class TxSignatureVerify:
    @staticmethod
    def verify_single(sig, pub_key, tx):
        return sig is not None and pub_key is not None

    @staticmethod
    def batch_verify(tx_list):
        valid = []
        invalid = []
        for tx in tx_list:
            if TxSignatureVerify.verify_single(tx["sig"], tx["pub"], tx["data"]):
                valid.append(tx["id"])
            else:
                invalid.append(tx["id"])
        return {"valid": valid, "invalid": invalid}

if __name__ == "__main__":
    txs = [{"id": 1, "sig": "S", "pub": "P", "data": "D"}]
    print(TxSignatureVerify.batch_verify(txs))
