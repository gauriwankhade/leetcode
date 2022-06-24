class Solution(object):
	def generateParenthesis(self, n):
		string = '()' * n
		result = set()
		paren = ['(', ')']
		count = {0: 0, 1: 0}

		def backtrack(curr, comb):
			if max(count[0], count[1]) > len(string)/2:
				return
			if count[0] >= count[1]:
				if len(comb) >= len(string):
					result.add(comb)
					return
				count[curr] += 1
				backtrack(curr, comb + paren[curr])
				count[curr] -= 1
				count[1 - curr] += 1
				backtrack(1 - curr, comb + paren[1 - curr])		
				count[1 - curr] -= 1				

		backtrack(0, "")

		return result
