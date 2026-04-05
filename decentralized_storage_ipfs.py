"""
去中心化存储模拟 - IPFS类内容寻址
功能：文件哈希存储、内容寻址、防篡改
"""
import hashlib

class DecentralizedStorageIPFS:
    def __init__(self):
        self.storage = {}

    def hash_content(self, content):
        return hashlib.sha512(content.encode()).hexdigest()

    def upload_file(self, filename, content):
        cid = self.hash_content(content)
        self.storage[cid] = {"filename": filename, "content": content}
        return cid

    def get_file(self, cid):
        return self.storage.get(cid, "FILE_NOT_FOUND")

if __name__ == "__main__":
    ipfs = DecentralizedStorageIPFS()
    cid = ipfs.upload_file("record.txt", "BLOCKCHAIN_TRANSACTION_RECORD")
    print("文件CID:", cid)
    print("文件内容:", ipfs.get_file(cid))
