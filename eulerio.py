def get_online_textfile(url, parse_as = 'lines') :
	'''
	Get the content of a text file from online.
	'''
	import requests
	txt = requests.get(url)
	if parse_as == 'lines' :
		return [line.decode() for line in txt.iter_lines()]
	elif parse_as == 'matrix' :
		return [[int(num) for num in line.decode().split(',')] 
			for line in txt.iter_lines()]

def get_oeis(search) :
	'''
	Get an OEIS search result.
	'''
	import requests
	import json
	oeis = requests.get("https://oeis.org/search", 
		params={"fmt": "json", "q": search}).json()
	return oeis