# Minimum Number of Arrows to Burst Balloons

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		points.sort()
		previous = float("-inf")
		result = 0

		for left, right in points:
			if left <= previous:
				if right < previous:
					previous = right
			else:
				previous = right
				result += 1
		return result

