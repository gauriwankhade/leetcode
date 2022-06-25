class Solution(object):
	def allPathsSourceTarget(self, graph):
		# visited = defaultdict(int)
		result = []

		def backtrack(curr, path):
			if curr == len(graph) - 1:
				result.append(list(path))
				return
			
			for neighbour in graph[curr]:
				path.append(neighbour)
				backtrack(neighbour, path)
				path.pop()

			return result

		return backtrack(0, [0])
