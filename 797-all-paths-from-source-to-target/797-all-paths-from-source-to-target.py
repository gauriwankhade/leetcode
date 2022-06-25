class Solution(object):
	def allPathsSourceTarget(self, graph):
		# visited = defaultdict(int)
		result = []

		def backtrack(curr, path):
			if curr == len(graph) - 1:
				result.append(path)
				return
			
			for neighbour in graph[curr]:
				backtrack(neighbour, path + [neighbour])

			return result

		return backtrack(0, [0])
