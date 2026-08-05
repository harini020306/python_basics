class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if root is None:
        return None

    
    root.left, root.right = root.right, root.left

    
    invertTree(root.left)
    invertTree(root.right)

    return root



def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (Preorder):")
preorder(root)

invertTree(root)

print("\nInverted Tree (Preorder):")
preorder(root)