"""
去中心化拍卖合约 - NFT/资产拍卖
功能：创建拍卖、出价、结束拍卖、最高出价
"""
class DecentralizedAuction:
    def __init__(self):
        self.auctions = {}

    def create_auction(self, aid, asset, start_price):
        self.auctions[aid] = {"asset": asset, "price": start_price, "bidder": None}

    def place_bid(self, aid, bidder, price):
        if self.auctions[aid]["price"] < price:
            self.auctions[aid]["price"] = price
            self.auctions[aid]["bidder"] = bidder

    def get_winner(self, aid):
        return self.auctions.get(aid, {}).get("bidder")

if __name__ == "__main__":
    auc = DecentralizedAuction()
    auc.create_auction("A01", "NFT_ART", 100)
    auc.place_bid("A01", "USER05", 150)
    print("获胜者:", auc.get_winner("A01"))
