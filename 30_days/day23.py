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

    def getHeight(self,root):
        right_height = 0
        left_height = 0
        if root==None:
            return -1
        right_height = self.getHeight(root.right)
        left_height = self.getHeight(root.left)

        return max(right_height,left_height) + 1

    def enqueue(self,cur,queue):
        if cur.left != None: queue.append(cur.left.data)
        if cur.right != None: queue.append(cur.right.data)

    def levelOrder(self,root):
        queue = []
        queue.append(root.data)
        height = self.getHeight(root)
        cur = root
        for i in range(height-3):
            self.enqueue(cur,queue)
            self.enqueue(cur.left,queue)
            self.enqueue(cur.right,queue)
        for q in queue:
            print(q, end=' ')
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
