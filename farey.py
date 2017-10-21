def rank(p, q, n) :
	'''
	Compute the ordinal of p/q in the Farey sequence with denominators
	no greater than n.
	From "Computer ORder Statistics in the Farey Sequence" by C. & M.
	Pastrascu
	'''
	import numpy as np
	T = np.fromfunction(lambda i : p * i // q, (n+1,), dtype=int)
	for q in range(1, n+1) :
		for mq in range(2*q, n+1, q) :
			T[mq] -= T[q]
	return T.sum()

def fracs_between(p1, q1, p2, q2, n) :
	return rank(p2, q2, n) - rank(p1, q1, n) - 1

def length(n, approx = False) :
	'''
	Return the length of a Farey sequence with maximum denominator n,
	excluding 0 / n.
	'''
	from util import totient_sieve
	return totient_sum(n) - 1