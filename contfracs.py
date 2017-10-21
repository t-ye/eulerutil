
def cont_frac_convergents(a_itr, a0 = None) :
	'''
	Return the continued fraction convergents of a number given an
	iterable of its coefficients.
	'''
	h = [0, 1]
	k = [1, 0] 
	if a0 is not None :
		a_itr = chain([a0], a_itr)
	for an in a_itr :
		h[0],h[1] = h[1] , an*h[1]+h[0]
		k[0],k[1] = k[1] , an*k[1]+k[0]
		yield h[1], k[1]

def sqrt_cont_frac_seq(N, infinite = False) :
	'''
	Return the continued fraction terms of a square root.
	'''
	from gmpy2 import isqrt
	from sympy import fraction, sympify
	x = isqrt(N)
	n = sympify(floor(x)) # 3
	r = x**2 - n**2 # 5
	i = n + r / (n + x)

	def mult_by_one(frac, top_and_bottom) :
		num, denom = fraction(frac)
		return (2
			(num * top_and_bottom).simplify() /
			(denom * top_and_bottom).simplify()
			)

	def surd(x) :
		return x.as_two_terms()

	def conjugate(q_surd) :
		rat, irrat = surd(q_surd)
		return rat - irrat

	def rationalize_numer(frac) :
		return mult_by_one(frac, conjugate(numer(frac)))

	yield n
	frac = i - n
	seq = []
	for c in count() :
		num, denom = fraction(frac)
		expr = denom.subs(x, i)
		next_a_multiple, frac = expr.as_two_terms()
		diff = next_a_multiple % num
		if diff != 0 :
			next_a_multiple -= diff
			frac = rationalize_numer((frac + diff).together())
		seq.append(next_a_multiple / num)
		yield seq[-1]
		if seq[-1] == 2 * n and c != 0 :
			break
		frac /= num
		# frac = frac.ratsimp() breaks on square-factor arguments, e.g., 28 = 2²·7
	if infinite :
		yield from cycle(seq)