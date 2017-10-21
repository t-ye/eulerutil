def series_coeffs(expr) :
	'''
	Return the coefficients for the Taylor series of an expression.
	'''
	from sympy import series
	series_gen = series(expr, n = None)
	var = expr.free_symbols.pop() # assumed univariateP
	last_degree, next_degree = 0, None
	for term in series_gen :
		next_degree = Poly(term, var).degree()
		yield from repeat(0, next_degree - last_degree - 1)
		yield term.as_coeff_mul()[0] # get constant of term
		last_degree = next_degree

def series_coeffs_test(expr, times) :
	a=series_coeffs(expr);repeat_func(next, times, a)

#x=Dummy('x', real=True, positive=True,nonzero=True)
#e_gen_func = 2 + x*(1 / (1 - x**3) + x**2 / (1 - x**3) + diff(1/(1-x**3))/x*2/3)
#e_gen_func = (x**6-x**4-3*x**3+2*x**2+x+2)/((x-1)**2*(x**2+x+1)**2)

