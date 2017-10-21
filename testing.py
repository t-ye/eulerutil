from inspect import isgeneratorfunction

def stopwatch(func, *args, return_result = True, num_trials = 1) :
	'''
	Time a function.
	'''
	from time import time
	t = time()
	result = func(*args)

	if isgeneratorfunction(func) :
		if return_result :
			result = list(result)
		else :
			for x in result :
				pass 
	if return_result :
		return result, str(time() - t) + 's'
	else :
		return str(time() - t) + 's'

def igen(*gen, cnt = None) :
	'''
	Iterate over a generator with prompt for each element.
	'''
	gen = zip(*gen) if len(gen) > 1 else gen[0] 
	if cnt is None :
		for x in gen :
			if input(str(x) + ' -- ENTER to continue') != '' :
				break
	else :
		for _ in range(cnt) :
			if input(next(gen) + ' -- ENTER to continue') != '' :
				break