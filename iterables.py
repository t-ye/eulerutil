
'''
Inclusive range.
'''
def irange(start_stop, stop, step=1):
	return range(start_stop + int(stop is None), *((stop+1,step) if stop is not None else ()))
	
'''
One-based inclusive range.
'''
def range1(stop):
	return range(1, stop+1)


def prod(itr) :
	'''
	Take the product of all elements of an iterable.
	'''
	p = 1
	for el in itr:
		p *= el
	return p

def merge_gen(gen1, gen2) :
	'''
	Merge two distinct ordered generators so that the new generator is
	distinct, ordered, and contains each element of its constituents.
	'''
	n1, n2 = next(gen1), next(gen2)
	while True :
		if n1 == n2 :
			nxt = n1
			n1 = next(gen1)
			n2 = next(gen2)
		elif n1 < n2 :
			nxt = n1
			n1 = next(gen1)
		elif n2 < n1 :
			nxt = n2
			n2 = next(gen2)
		yield nxt

def invert_gen(exclude) :
	'''
	Inverts an ordered integral generator so that the values not in the
	generator are generated, in order.
	'''
	(last, nxt) = next(exclude), next(exclude)
	while True :
		yield from range(last+1, nxt)
		last = nxt
		nxt = next(exclude)

def identical(iterator):
	'''
	Check if all elements of an iterator are identical.
	'''
	iterator = iter(iterator)
	try:
			first = next(iterator)
	except StopIteration :
			return True
	return all(first == rest for rest in iterator)



def consume(iterator, n):
	import collections
	''''Advance the iterator n-steps ahead. If n is none, consume
	entirely.
	Recipe from Python documentation.
	'''
	# Use functions that consume iterators at C speed.
	if n is None:
			# feed the entire iterator into a zero-length deque
			collections.deque(iterator, maxlen=0)
	else:
			# advance to the empty slice starting at position n
			next(islice(iterator, n, n), None)

