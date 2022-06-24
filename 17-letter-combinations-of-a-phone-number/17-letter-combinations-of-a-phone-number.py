class Solution(object):
    def letterCombinations(self, digits):
		if not digits:
			return 

		hashmap = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}

		lastComb = hashmap[digits[0]]

		for item in digits[1: ]:
			newComb = []
			for digit in hashmap[item]:
				for comb in lastComb:
					newComb.append(comb + digit)

			lastComb = newComb

		return lastComb

