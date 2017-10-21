def dijkstra_path_sum(matrix, moves, start_nodes, end_nodes,
	contains_node=None) :
	'''
	Dijkstra's shortest path algorithm based on path sums in a matrix.
	(80, 81, 82)
	matrix: the graph to traverse
	moves: the functions that can be applied to a node to transform it
	into another
	start_nodes: a desired path can start at any of these nodes
	end_nodes: a desired path can end at any of these nodes
	'''
	import numpy as np
	import heapq

	if contains_node == None :
		contains_node = lambda node : \
			0 <= node[0] < len(matrix) and 0 <= node[1] < len(matrix[0])

	heap = [(matrix[start_node], start_node) for start_node in
		start_nodes]
	heapq.heapify(heap)

	visited = np.zeros(matrix.shape, dtype=bool)
	for start_node in start_nodes :
		visited[start_node] = True

	def adj_nodes(node) :
		return filter(contains_node, (move(node) for move in moves))

	while heap[0][1] not in end_nodes :
		weight, node = heapq.heappop(heap)
		for adj_node in adj_nodes(node) :
			if not visited[adj_node] :
				heapq.heappush(heap, (weight+graph[adj_node], adj_node))
			visited[adj_node] = True

	return heap
	