# I do plan to comment this. Right after I retrace my train of thought.
from math import log
d = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def todec(n,b):
	nn = list("x"*len(n))
	for i in range(0,len(n)):
		nn[i] = str((''.join(d)).find(n[i]))
	r = 0
	for i in range(0,len(n)):
		r += int(nn[-i-1])*(b**i)
	return r
def fromdec(n,b):
	L = int(log(float(int(n)),float(b)))
	r = list("x"*(L+1))
	for i in range(L+1):
		r[i] = d[int(n)/(b**(-(i-L)))]
		if r[i] == '0':
			continue
		n = int(n) % (b**(-(i-L)))
	return ''.join(r)
inbase = int(raw_input('Input base: '))
outbase = int(raw_input('Output base: '))
number = raw_input('Input number: ')
print number,"in base",inbase,"is",fromdec(todec(number,inbase),outbase),"in base", outbase
# from os import system
# system('pause')
