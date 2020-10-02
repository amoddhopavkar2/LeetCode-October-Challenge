# Number of Recent Calls

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class RecentCounter:

    def __init__(self):
        self.result = []

    def ping(self, t: int) -> int:
        self.result.append(t)
        
        while self.result[0] < t - 3000:
            self.result.pop(0)
            
        return len(self.result)
        