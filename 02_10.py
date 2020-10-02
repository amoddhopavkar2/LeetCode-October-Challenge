# Combination Sum

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		self.result = []
		candidates.sort()
		self.combinations_helper([], candidates, target)
		return self.result

	def combinations_helper(self, temp, candidates, target):
		for item in candidates:
			if item > target:
				break

			temp.append(item)
			if item == target:
				self.result.append(temp.copy())
				temp.pop()
			
			else:
				index = candidates.index(item)
				self.combinations_helper(temp, candidates[index:], target-item)
				temp.pop()