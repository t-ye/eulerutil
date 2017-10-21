'''
Turn an iterable of digits into a number, assuming it provides the
most significant digits first1.
'''
digits_to_num = lambda digits : reduce(lambda x,y: 10*x+y, digits)

def digits(num) :
	'''
	Yield the decimal digits of an number in read order.
	'''
	num = abs(num)
	def digits_recur(num) :
		yield from (num,) if num<10 else chain(digits_recur(num//10),
			(num%10,))
	yield from digits_recur(num)


def digit_bag(num) :
	'''
	Return a multiset of the digits of a number as a dict.
	'''
	return frozendict(Counter(digits(num)))

def digit_sum(num, base = 10) :
	'''
	Return the sum of the digits of a number in any base.
	'''
	total = 0
	while num > 0 :
		total += num % base
		num //= base
	return total
