from collections import Counter

class Solution(object):
	def isPossible(self, nums):
		count = Counter(nums)
		numLen = len(nums)

		lastSub = defaultdict(int)

		for num in nums:
			#print(num, count)
			if not count[num]:
				continue

			count[num] -= 1

			# append to existing sub list
			if lastSub[num - 1]:
				lastSub[num - 1] -= 1
				lastSub[num] += 1

			# add new sub list
			elif count.get(num + 1) and count.get(num + 2):
				count[num + 1] -= 1
				count[num + 2] -= 1
				lastSub[num + 2] += 1

			else:
				return False

		return True