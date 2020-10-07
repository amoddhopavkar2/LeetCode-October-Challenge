# Rotate Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head or not k:
			return head

		n, tail, current = 0, head, head
		while current and current.next:
			current = current.next
			n += 1
		tail = current
		n += 1

		k = k % n
		if not k:
			return head

		n = n - k - 1
		current = head
		for _ in range(n):
			current = current.next

		new_head = current.next
		current.next = None
		tail.next = head

		return new_head
