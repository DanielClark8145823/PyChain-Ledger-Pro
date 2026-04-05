"""
ERC721标准NFT合约 - 非同质化数字资产
功能：NFT铸造、所有权转移、资产查询
"""
class ERC721NFTAsset:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.nft_owners = {}
        self.nft_metadata = {}
        self.token_id = 1

    def mint_nft(self, owner, metadata):
        self.nft_owners[self.token_id] = owner
        self.nft_metadata[self.token_id] = metadata
        self.token_id += 1
        return self.token_id - 1

    def transfer_nft(self, from_owner, to_owner, token_id):
        if self.nft_owners.get(token_id) == from_owner:
            self.nft_owners[token_id] = to_owner
            return True
        return False

    def get_owner(self, token_id):
        return self.nft_owners.get(token_id, "NOT_EXIST")

if __name__ == "__main__":
    nft = ERC721NFTAsset("ArtNFT", "ART")
    tid = nft.mint_nft("CREATOR01", {"name": "Sunset", "type": "image"})
    nft.transfer_nft("CREATOR01", "BUYER01", tid)
    print("NFT所有者:", nft.get_owner(tid))
