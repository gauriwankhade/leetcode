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
			if sum(Map.values()) - Map[s[last]] > k:
				Map[s[last]] -= 1
				last += 1
				limit = k

			maxCount = max(sum(Map.values()), maxCount)

			index += 1


		if sum(Map.values()) - Map[s[last]] < k:
			count = sum(Map.values()) + k
			if count > length:
				count = length

		
		return max(count, maxCount)
