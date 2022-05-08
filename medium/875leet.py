import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        result = 0
        high = max(piles)
        low = 1
        count = 0

        while(high >= low):
        	mid = int((high + low) / 2)
        	count = 0
        	for i in piles:
        		if i <= mid:
        			count += 1
        		else :
        			count += math.ceil(i / float(mid))

        	if count <= h:
        		high = mid - 1
        	elif count > h:
        		low = mid + 1


        return low


# driver's code
s = Solution()
piles = [[312884470], [30,11,23,4,20], [30,11,23,4,20], [3,6,7,11], [1, 2, 3, 4, 5], [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]]
h = [968709470, 5, 6, 8, 5, 823855818]

for i in range(len(h)):
	print(i+1,': h: ',h[i], s.minEatingSpeed(piles[i], h[i]))




