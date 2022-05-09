
class Solution(object):
	def canReorderDoubled(self, arr):
		Map = {}
		arr = sorted(arr)
		for key in arr:
			if Map.get(key):
				Map[key] += 1
			else:
				Map[key] = 1

		
		for i in arr:
			if Map.get(i):
				Map[i] -= 1
				if i % 2 == 0 and Map.get(i / 2):
					Map[i / 2] -= 1
				elif Map.get(i * 2):
					Map[i * 2] -= 1
				else:
					return False

		return True

s = Solution()
arr = [-62,86,96,-18,43,-24,-76,13,-31,-26,-88,-13,96,-44,9,-20,-42,100,-44,-24,-36,28,-32,58,-72,20,48,-36,-45,14,24,-64,-90,-44,-16,86,-33,48,26,29,-84,10,46,50,-66,-8,-38,92,-19,43,48,-38,-22,18,-32,-48,-64,-10,-22,-48]
print(s.canReorderDoubled(arr))


