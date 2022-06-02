class Solution(object):
	def characterReplacement(self, s, k):
		maxCount = 0
		length = len(s)
		index  = count = 1
		limit = k
		last = 0

		Map = defaultdict(int)
		Map[s[0]] += 1

		while(index < length ):
			Map[s[index]] += 1
			count = sum(Map.values())

			if count - Map[s[last]] > k:
				Map[s[last]] -= 1
				last += 1
				count -= 1

			maxCount = max(count, maxCount)
			index += 1


		if count - Map[s[last]] < k:
			count +=  k
			if count > length:
				count = length


		return max(count, maxCount)
