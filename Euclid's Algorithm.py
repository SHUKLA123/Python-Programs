# gcd of any number 

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)
print(gcd(10,20))

# Output : 10

# But python has simple way of finding gcd is using math module :

# Alternative way : It is fast as well as always used in Competitive programming.

from math import gcd
print(gcd(10,20))

# Output : 10

