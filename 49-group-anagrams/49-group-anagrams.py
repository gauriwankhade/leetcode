from collections import defaultdict

class Solution(object):
	def groupAnagrams(self, strs):
		strMap = defaultdict(list)

		for item in strs:
			key = "".join(sorted(item))
			strMap[key].append(item)

		return strMap.values()
