#   Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        container = []
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            container.append((node.val, node))
            traverse(node.right)
        
        traverse(root)
        target = sorted(container)
        for i in range(len(container)):
            currNode, targetNode = container[i][1], target[i][1]
            if currNode != targetNode:
                currNode.val, targetNode.val = targetNode.val, currNode.val
                break
        