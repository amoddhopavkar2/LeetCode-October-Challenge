# Remove Covered Intervals

class Solution:
	# Sort according to the start in ascending order.
	# In-case the start is same, then sort according to the end in descending order.
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))

		count, ending = 0, 0
		for start, end in intervals:
			if end > ending:
				count += 1
				ending = end
		return count
