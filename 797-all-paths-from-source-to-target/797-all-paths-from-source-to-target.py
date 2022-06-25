class Solution(object):
	def allPathsSourceTarget(self, graph):
		result = []

		def backtrack(curr, path):
			if curr == len(graph) - 1:
				result.append(path[0: ])
				return
			
			for neighbour in graph[curr]:
				path.append(neighbour)
				backtrack(neighbour, path)
				path.pop()

			return result

		return backtrack(0, [0])
