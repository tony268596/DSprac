"""
這邊insert方法好笨
有比較好的insert法再去找找

先建立binary tree，然後用DFS去遍歷他
bonus:preorder, inorder, postorder
"""

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# dfs跟preorder是一樣的
def dfstraverse(root:TreeNode):
    if not root:
        return
    
    print(f"{root.data}", end = "\t")
    dfstraverse(root.left)
    dfstraverse(root.right)

def inorder(root:TreeNode):
    if not root:
        return
    
    inorder(root.left)
    print(root.data, end = "\t")
    inorder(root.right)

def postorder(root:TreeNode):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = "\t")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print("DFS")
dfstraverse(root)
print("\n")

print("In")
inorder(root)
print("\n")

print("Post")
postorder(root)