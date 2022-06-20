from collections import defaultdict

class Solution(object):
	def groupAnagrams(self, strs):
		ans = collections.defaultdict(list)
		alpha = 'abcdefghijklmnopqrstuvwxyz'

		for item in strs:
			chars = [0] * 26
			for char in item:
				chars[alpha.find(char)] += 1

			ans[tuple(chars)].append(item)

		return ans.values()