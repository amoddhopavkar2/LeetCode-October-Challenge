# Number of Recent Calls

class RecentCounter:

	def __init__(self):
		self.d = []

	def ping(self, t: int) -> int:
		self.d.append(t)

		while self.d[0] < t - 3000:
			self.d.pop(0)

		return len(self.d)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)