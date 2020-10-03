# K-diff Pairs in an Array

class Solution:
	def findPairs(self, nums: List[int], k: int) -> int:
		if k < 0:
			return 0
		pairs, seen = set(), set()
		for n in nums:
			if (n - k) in seen:
				pairs.add((n-k, n))
			if (n + k) in seen:
				pairs.add((n, n+k))
			seen.add(n)
		return len(pairs)
	
