# Number of Longest Increasing Subsequence

class Solution:
	def findNumberOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0

		count = [1] * len(nums)
		dp = [1] * len(nums)
		max_length = 0

		for i in range(len(nums)):
			for j in range(i):
				if nums[j] < nums[i]:
					if dp[i] < dp[j] + 1:
						dp[i] = dp[j] + 1
						count[i] = count[j]
					elif dp[i] == dp[j] + 1:
						count[i] += count[j]
			max_length = max(max_length, dp[i])

		return sum(count for length, count in zip(dp, count) if length == max_length)