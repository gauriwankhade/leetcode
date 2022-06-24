class Solution(object):
    def letterCombinations(self, digits):
		

		hashmap = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
		result = []

		def backtrack(curr, comb):
			if curr >= len(digits):
				result.append(comb)
				return

			for digit in hashmap[digits[curr]]:
				backtrack(curr + 1, comb + digit)

			return result

		return backtrack(0, "")
		
