# Rotate Array
# Do not return anything, modify nums in-place instead.

class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		n = len(nums)
		k = k % n

		nums[:] = nums[n-k:] + nums[:n-k]