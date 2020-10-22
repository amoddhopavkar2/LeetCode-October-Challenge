# Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)

            if l > 0 and r > 0:
                return min(l, r) + 1

            elif l > 0:
                return l + 1

            else:
                return r + 1
        return 0
