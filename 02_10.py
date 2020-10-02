# Combination Sum

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		self.result = []
		candidates.sort()
		self.find_combinations([], candidates, target)
		return self.result

	def find_combinations(self, temp, candidates, target):
		for item in candidates:
			if item > target:
				break

			temp.append(item)
			if item == target:
				self.result.append(temp.copy())
				temp.pop()
				break
			else:
				index = candidates.index(item)
				self.find_combinations(temp, candidates[index:], target-item)
				temp.pop()
