"""DP with memorization"""
def fibonnaci_no_memorization(n):
	if n == 0:
		return False
	elif n == 1:
		return  0
	elif n == 2:
		return 1
	else:
		return fibonnaci_no_memorization(n-1) + fibonnaci_no_memorization(n-2)
print(fibonnaci_no_memorization(9))