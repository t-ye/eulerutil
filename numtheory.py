from functools import lru_cache

@lru_cache(maxsize = None)
def _sum_pos_int(n) :
	'''
	Return the sum of the positive integers up to and including n.
	'''
	return n * (n + 1) // 2

def totient_sum(n) :
	'''
	Sum totients from 1 to n inclusive.
	'''
	# Consider all 2-tuples to be tested for coprimality as (a, b), with
	# 1 < a < b <= N. When plotted on the Cartesian plane, they form a
	# lattice triangle with N * (N - 1) // 2 points.
	# Denote the count of (a, b) such that (a, b) = 1 as the totient
	# summatory. (This excludes (1,1). Add this on later if desired.)
	# Observe that (a, b) = k implies (a/k, b/k) = 1. Graphically, (a/k,
	# b/k) is magnified by k to yield a lattice point that should not be
	# included in the totient summatory. By excluding all of these
	# magnifications we can obtain our desired answer.
	# To do this, note that for all 2 <= k <= N, 1 < a < b <= N // k, 
	# (a, b) = 1, (ka, kb) uniquely corresponds to all to-be-excluded
	# magnifications. Thus we can find the totient summatory for all 
	# N // k instead of N. This yields a recursive algorithm.
	return (_sum_pos_int(n - 1) # The area of the lattice triangle
		- sum(totient_sum_recur(n // k) for k in irange(2, n)) + 1) 
		# The "demagnification" of n

@lru_cache(maxsize = None)
def totient_sum_recur(n) :
	if n == 1 :
		return 0
	if n == 2 :
		return 1
	return sum_pos_int(n - 1) - sum(
		totient_sum_recur(n // k) for k in irange(2, n))

def totient_sieve2(N) :
	'''
	Compute totients from 1 to N.
	'''
	import numpy as np
	from math import log
	from sympy import Rational
	sieve = np.arange(N+1, dtype=Rational)
	for p in wheel_range(N+1, size = min(6, ceil(log(N, 10)))) :
		if sieve[p] == p :
			sieve[p::p] *= (1 - 1/p)
	return sieve.astype(np.int64)
	

def divisor_sum_sieve(N) :
	'''
	Generate an array of the aliquot sums of 0 to N inclusive.
	'''
	sieve = np.zeros(N+1, dtype=int)
	for i in irange(1,N//2) :
		sieve[2*i::i] += i
	return sieve