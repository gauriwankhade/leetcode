class Solution(object):
	def generateParenthesis(self, n):
		result = set()

		def backtrack(curr, comb, openCount, closedCount, n):
			if max(openCount, closedCount) > n:
				return
			if openCount >= closedCount:
				if openCount + closedCount >= 2 * n:
					result.add(comb)
					return

				backtrack(0, comb + '(', openCount + 1, closedCount, n)
				backtrack(1, comb + ')', openCount, closedCount + 1, n)			

		backtrack(0, "", 0, 0, n)

		return result

