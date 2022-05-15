

class Solution(object):
	def removeKdigits(self, num, k):
		length = len(num) - 1
		stack = [0]
		counter = 0
		string = [p for p in num]
		num = [int(n) for n in num]
		index = 1

		while(counter != k):
			print(index, stack)
			if index > length:
				string[stack[-1]] = -1
				counter += 1
				print('pop - ', stack[-1], counter)
				stack.pop()
			elif num[stack[-1]] <= num[index]:
				stack.append(index)
				index += 1
			else:
				string[stack[-1]] = -1
				counter += 1
				print('pop - ', stack[-1], counter)
				stack.pop()
				if not stack:
					stack.append(index)
					index += 1

		result = ''
		for item in string:
			if item!= -1:
				result += item
		
		if not result:
			result = 0
		return int(result)

s = Solution()
num = "43214321"
k = 4
print([l for l in range(len(num))])
print([int(b) for b in num])
print(s.removeKdigits(num, k))

