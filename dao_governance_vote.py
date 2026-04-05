"""
DAO去中心化自治组织 - 链上投票
功能：提案创建、投票、结果统计
"""
class DAOGovernanceVote:
    def __init__(self):
        self.proposals = {}

    def create_proposal(self, pid, content):
        self.proposals[pid] = {"content": content, "agree": 0, "against": 0}

    def vote(self, pid, choice):
        if pid in self.proposals:
            if choice == 1:
                self.proposals[pid]["agree"] += 1
            else:
                self.proposals[pid]["against"] += 1

    def get_result(self, pid):
        return self.proposals.get(pid, "NOT_EXIST")

if __name__ == "__main__":
    dao = DAOGovernanceVote()
    dao.create_proposal("P01", "UPGRADE_VM")
    dao.vote("P01", 1)
    dao.vote("P01", 1)
    print("投票结果:", dao.get_result("P01"))
