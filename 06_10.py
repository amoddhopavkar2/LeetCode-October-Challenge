# Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
		if not root:
			root = TreeNode(val = val)
		elif root.val > val:
			root.left = self.insertIntoBST(root.left, val)
		else:
			root.right = self.insertIntoBST(root.right, val)
		return root
