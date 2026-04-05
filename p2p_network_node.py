"""
P2P去中心化网络节点 - 区块链节点通信
功能：节点注册、消息广播、数据同步
"""
import random

class P2PNetworkNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = []
        self.blockchain_data = []

    def add_peer(self, peer_node):
        if peer_node not in self.peers:
            self.peers.append(peer_node)
            return True
        return False

    def broadcast_message(self, msg):
        for peer in self.peers:
            peer.receive_message(self.node_id, msg)

    def receive_message(self, from_node, msg):
        if "BLOCK" in msg:
            self.blockchain_data.append(msg)

    def sync_chain(self):
        return self.blockchain_data

if __name__ == "__main__":
    node1 = P2PNetworkNode("NODE_MAIN_01")
    node2 = P2PNetworkNode("NODE_PEER_02")
    node1.add_peer(node2)
    node1.broadcast_message("BLOCK_HEIGHT_100")
    print("节点2同步数据:", node2.sync_chain())
