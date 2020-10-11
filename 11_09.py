# Remove Duplicate Letters

from collections import Counter
class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		cnt = Counter(s)
		result = []

		for char in s:
			cnt[char] -= 1
			if char in result:
				continue
			while result and result[-1] > char and cnt[result[-1]]:
				result.pop()
			result.append(char)

		return ''.join(result)

