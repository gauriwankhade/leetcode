class Solution(object):
	def generateParenthesis(self, n):
		string = '()' * n
		visited = defaultdict(bool)
		result = set()
		count = {1: '(', 0: ')'}

		def backtrack(curr, comb):
			if max(comb.count('('), comb.count(')')) > len(string)/2:
				return
			if comb.count('(') >= comb.count(')'):
				if len(comb) >= len(string):
					result.add(comb)
					return

				backtrack(curr, comb + count[curr])
				backtrack(1 - curr, comb + count[1 - curr])
			
				
						

		backtrack(0, "")

		return result