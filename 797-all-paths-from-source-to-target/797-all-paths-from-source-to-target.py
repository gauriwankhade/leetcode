class Solution(object):
	def allPathsSourceTarget(self, graph):
		visited = defaultdict(int)
		result = set()

		def backtrack(curr, path):
			if curr == len(graph) - 1:
				result.add(tuple(path))
				return
			# if not graph[curr]:
			# 	return

			for neighbour in graph[curr]:
				if not visited[neighbour]:
					visited[neighbour] = True
					backtrack(neighbour, path + [neighbour])
					visited[neighbour] = False

			return result


		return backtrack(0, [0])
