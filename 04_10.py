# Remove Covered Intervals

class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		# Sort the start in ascending order.
		# In-case the start is same, then sort according to the end in descending order.
		intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))

		count = 0
		ending = 0
		for start, end in intervals:
			if end > ending:
				count += 1
				ending = end
		
		return count
