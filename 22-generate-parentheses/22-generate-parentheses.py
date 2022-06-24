class Solution(object):
	def generateParenthesis(self, n):
		string = '()' * n
		result = set()
		count = {1: '(', 0: ')'}

		def backtrack(curr, comb, openCount, closedCount):
			if max(openCount, closedCount) > len(string)/2:
				return
			if openCount >= closedCount:
				if len(comb) >= len(string):
					result.add(comb)
					return

				backtrack(0, comb + count[0], openCount, closedCount + 1)
				backtrack(1, comb + count[1], openCount + 1, closedCount)			

		backtrack(0, "", 0, 0)

		return result
