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
			path = 0
			if visited[node]:
				continue
			queue = [node]
			while(queue):
				elem = queue.pop()
				if not visited[elem]:
					queue = queue + graph[elem]
					visited[elem] = True
					path += 1
			if path > 0:
				count += 1

		return count + n - len(visited) 
					