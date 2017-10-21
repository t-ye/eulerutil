from math import inf

def psieve2():
	'''
	Simple implementation of postponed prime sieve.
	'''
	D = {}
	yield 2
	for q in it.count(3, 2) :
		p = D.pop(q, None)
		if p is None:
			D[q*q] = q
			yield q
		else :
			x = q + 2*p
			while x in D:
				x += 2*p
			D[x] = p

def psieve():
	'''
	Generate primes with a postponed sieve.
	'''
	import itertools as it
	D = {}
	yield from (2,3,5)
	MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )
	for q in it.accumulate(it.chain([7], it.cycle([4,2,4,2,4,6,2,6]))) :
		p = D.pop(q, None)
		if p is None :
			D[q*q] = q
			yield q
		else:
			x = q + 2*p
			while x in D or (x%30) not in MODULOS:
					x += 2*p
			D[x] = p

_diffs_cache = {}
def wheel_range(stop = inf, size = 6) :
	'''
	Generate prime candidates by wheel factorization.
	'''
	from itertools import cycle, islice, takewhile
	from numpy import diff, concatenate, fromiter, int64
	primes = psieve()
	base = fromiter(islice(primes, size), dtype=int64)
	circum = prod(base)
	diffs = _diffs_cache.get(size)
	if diffs is None :
		diffs = diff(
			concatenate((
				[1],
				fromiter(
					takewhile(lambda p:p<circum, primes), dtype=int64
					),
				[circum + 1]
				))
			)
		_diffs_cache[size] = diffs
	yield from base
	nxt = 1
	for diff in cycle(diffs) :
		nxt += diff
		if nxt >= stop :
			raise StopIteration
		yield nxt