from math import inf

def bary_coords(P, *xy) :
	'''
	Return a set of weights for each xy-coordinate such that their
	weighted sum yields P.
	'''
	from sympy.abc import lamda
	import numpy as np
	A = np.vstack((np.ones((1,len(xy)), dtype = int), 
		np.stack(xy, axis = 1)))
	b = np.vstack((1, *P))
	return np.linalg.solve(A, b)

def prim_pythag_triple_gen(max_sum = inf) :
	'''
	Generate all primitive Pythagorean triples.

	Not memory-efficient. Consider deletion of prior elements in chunks.
	'''
	import numpy as np
	from itertools import count
	ROOT = np.array([3,4,5], dtype=int)
	transforms = np.array([
		[
			[1, -2, 2],
			[2, -1, 2],
			[2, -2, 3]
		],
		[
			[1, 2, 2],
			[2, 1, 2],
			[2, 2, 3]
		],
		[
			[-1, 2, 2],
			[-2, 1, 2],
			[-2, 2, 3]
		]
		], dtype=int)
	nodes = []
	nodes.append(ROOT)
	limit = lambda arr : sum(arr) <= max_sum
	for node in nodes :
		yield node
		nodes.extend(filter(limit, iter(transforms @ node)))