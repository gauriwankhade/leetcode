class Solution(object):
	def countComponents(self, n, edges):
		graph = defaultdict(list)
		visited = defaultdict(bool)
		result = []

		for edge in edges:
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])

		count = 0
		for node in graph.keys():
			if visited[node]:
				continue
			stack = [node]
			path = 0
			while(stack):
				elem = stack.pop()
				if not visited[elem]:
					stack = stack + graph[elem]
					visited[elem] = True
					path += 1
			if path > 0:
				count += 1

		return count + n - len(visited) 
					
	