n = 2
def check_prime(n):
	if n == 1:
		return False
	count = 0
	for i in range(2,n):
		if n%i == 0:
			count += 1
	if count  == 0:
		return True
	else:
		return False

print(check_prime(n))
