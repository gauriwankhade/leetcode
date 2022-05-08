
class Solution(object):
    def findClosestElements(self, arr, k, x):
        limit = len(arr)

        lastSum = sum([abs(i - x) for i in arr[0: k]])
        counter = 0
        startIndex = 0
        endIndex = k - 1

        while(counter + k < limit):
            newSum = lastSum - abs(arr[counter] - x) + abs(arr[counter + k] - x)
            if newSum < lastSum:
                startIndex = counter + 1
                endIndex = counter + k
                lastSum = newSum
            counter += 1

        return arr[startIndex: endIndex + 1]

            






s = Solution()
arr = [1, 2, 3, 8, 9]
k = 3
x = - 1
print(arr, f'x: {x}, k: {k}')
print(s.findClosestElements(arr, k, x))