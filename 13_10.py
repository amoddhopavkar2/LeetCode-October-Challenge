# Sort Linked List

class Solution:
	def sortList(self, head: ListNode) -> ListNode:
		if not head:
			return None

		lst = []
		while head:
			lst.append(head.val)
			head = head.next

		lst.sort()
		nxt = None
		while lst:
			val = lst.pop()
			node = ListNode(val)
			node.next = nxt
			nxt = node
		return node
