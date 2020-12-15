# Construct a binary tree with a single node
# Harsha vardhan reddy
# 121910313001

class TreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def printhead(self):
        print(self.data)

treenode = TreeNode(35)
treenode.printhead()