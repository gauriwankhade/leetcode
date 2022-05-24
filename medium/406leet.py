


# class Solution(object):
# 	def reconstructQueue(self, people):
# 		people = sorted([tuple(item) for item in people], reverse=True) 
# 		newArr = []
# 		count = 0
# 		peopleMap = {}

# 		for p in people:
# 			if not peopleMap.get(p[0]):
# 				peopleMap[p[0]] = [p[1]]
# 			else:
# 				peopleMap[p[0]].append(p[1])
		

# 		counter = 0
# 		while(counter < len(people)):
# 			if not newArr:
# 				newArr.append((people[counter][0], peopleMap[people[counter][0]].pop()))
				
# 			else:
# 				item = (people[counter][0], peopleMap[people[counter][0]].pop())
# 				count = 0
# 				while (count < item[1]):
# 					if item[1] == count:
# 						break
# 					if newArr[count][0] >= item[0]:
# 						count += 1
# 				print(item, count, newArr)
# 				newArr = newArr[0: count] + [item] + newArr[count: ]

# 			counter += 1

# 		return newArr



# s = Solution()
# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2],(2,0)]
# print(s.reconstructQueue(people))






# class Solution(object):
# 	def reconstructQueue(self, people):
# 		people = sorted([tuple(item) for item in people], reverse=True) 
# 		newArr = []
# 		count = 0
# 		peopleMap = {}

# 		for p in people:
# 			if not peopleMap.get(p[0]):
# 				peopleMap[p[0]] = [p[1]]
# 			else:
# 				peopleMap[p[0]].append(p[1])

# 		counter = 1
# 		newArr.append((people[0][0], peopleMap[people[0][0]].pop()))

# 		while(counter < len(people)):
# 			print(counter, people[counter], peopleMap)
# 			item = (people[counter][0], peopleMap[people[counter][0]].pop())
# 			count = 0
# 			while (count < item[1]):
# 				if item[1] == count:
# 					break
# 				if newArr[count][0] >= item[0]:
# 					count += 1
			
# 			newArr = newArr[0: count] + [item] + newArr[count: ]

# 			counter += 1

# 		return newArr




# class Solution(object):
# 	def reconstructQueue(self, people):
# 		people = sorted([tuple(item) for item in people], reverse=True) 
# 		newArr = [0] * len(people)
# 		count = 0
# 		peopleMap = {}

# 		for p in people:
# 			if not peopleMap.get(p[0]):
# 				peopleMap[p[0]] = [p[1]]
# 			else:
# 				peopleMap[p[0]].append(p[1])

# 		counter = 1
# 		newArr[0] = (people[0][0], peopleMap[people[0][0]].pop())

# 		while(counter < len(people)):
			
# 			item = (people[counter][0], peopleMap[people[counter][0]].pop())
# 			count = item[1]
			
# 			newArr[count] = item

# 			counter += 1

# 		return newArr




class Solution(object):
	def reconstructQueue(self, people): 
		people.sort(key = lambda x:x[1])
		people.sort(reverse=True, key = lambda x:x[0])
		
		newArr = []
		for item in people:
			newArr.insert(item[1], item) 
			

		return newArr
 


s = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(s.reconstructQueue(people))


