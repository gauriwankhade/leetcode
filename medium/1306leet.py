
class Solution(object):
	def canReach(self, arr, start):
		if not arr:
			return
		limit = len(arr)
		visited = {}
		self.ans = False

		def recursion(curr):
			if curr >= limit or curr < 0 or visited.get(curr):
				return
			print(curr, arr[curr])
			visited[curr] = True
			if arr[curr] == 0:
				self.ans = True
				return 
			recursion(curr + arr[curr])
			recursion(curr - arr[curr])

			return self.ans

		return recursion(start)



s = Solution()
arr = [3,0,2,1,2]
start = 2
print(s.canReach(arr, start))