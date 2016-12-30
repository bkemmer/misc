import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def enqueue(self,cur,qNode,qData):
        if(cur!=None):
            qNode.append(cur)
            qData.append(cur.data)

    def levelOrder(self,root):
        qNode = []
        qData = []

        cur = root
        self.enqueue(cur,qNode,qData)
        while(len(qNode)>0):
            cur = qNode.pop(0)
            self.enqueue(cur.left,qNode,qData)
            self.enqueue(cur.right,qNode,qData)

        for q in qData:
            print(q, end=' ')
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
