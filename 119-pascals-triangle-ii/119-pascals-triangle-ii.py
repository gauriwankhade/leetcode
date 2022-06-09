class Solution(object):
	def getRow(self, rowIndex):
		dp = [[0 for col in range(rowIndex + 1)] for row in range(rowIndex + 1)]

		for col in dp:
			col[0] = 1

		for i in range(1, len(dp)):
			for j in range(1, len(dp)):
				dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

		return dp[-1]
