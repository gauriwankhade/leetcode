from collections import defaultdict

class Solution(object):
	def characterReplacement(self, s, k):
		maxCount = last = 0
		length = len(s)
		index  = count = 1

		Map = defaultdict(int)
		Map[s[0]] += 1

		while(index < length):
			Map[s[index]] += 1
			count += 1

			if count - Map[s[last]] > k:
				Map[s[last]] -= 1
				last += 1
				count -= 1

			maxCount = max(count, maxCount)
			index += 1

		# handle edge case - last count didnt used up k
		if count - Map[s[last]] < k:
			count +=  k

		return min(max(count, maxCount), length)

	