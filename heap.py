
from math import inf

'''
Priority queue methods.
'''
def insert(q, x) :
	'''
	Insert x into q.
	'''
	pass

def _max(q) :
	'''
	Return element of q with largest key.
	'''
	pass

def extract_max(q) :
	'''
	Return element of q with largest key, and remove it from q.
	'''
	pass

def increase_key(q, x, k) :
	'''
	Increase the value of element x's key to the new value k
	'''
	pass

'''
Max heap access methods. (A heap is an implementation of a priority queue.)
These take a list and visualize it as a binary tree.
'''
def root(heap) :
	'''
	Return the highest node in the heap (the max).
	'''
	return heap[0]

def parent(i) :
	'''
	Return the theoretical index of the parent of a heap's ith element.
	'''
	return (i - 1) // 2

def left(i) :
	'''
	Return the theoretical index of the left child of a heap's ith element.
	'''
	return 2 * i + 1

def right(i) :
	'''
	Return the theoretical index of the right child of a heap's ith element.
	'''
	return 2 * i + 2

'''
Max heap operations.
'''

mh_ex = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
ex_idx = 1
# max_heapify(mh_ex, ex_idx) == ][16, 14, 10, 4, 7, 9, 3, 2, 8, 1]
def max_heapify(heap, i) :
	'''
	Correct the position of heap[i], assuming it is no lower than it
	should be (i.e., this function only moves heap elements down).
	Also known as: 
	'''
	l, r = left(i), right(i)
	largest = max(i,l,r, 
		key = lambda idx : heap[idx] if idx in range(len(heap)) else -inf)
	if i != largest :
		heap[i], heap[largest] = heap[largest], heap[i]
		max_heapify(heap, largest)
 
def min_heapify(heap, i) :
	pass

bmh_ex = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# build_max_heap(bmh_ex) == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
def build_max_heap(lst) :
	'''
	Turn an unordered list into a max heap.
	Also known as: heapify
	'''
	heap = lst[:]
	for i in range(len(heap) // 2, -1, -1) :
		max_heapify(heap, i)
	return heap


'''
Heap utility methods.
'''
hs_ex = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
def max_heapsort(lst) :
	'''
	Sorts a list using a heap.
	'''
	heap = build_max_heap(lst)
	sort = []
	while heap :
		heap[0], heap[-1] = heap[-1], heap[0]
		next_max = heap.pop()
		max_heapify(heap, 0)
		sort = [next_max] + sort
	return sort
