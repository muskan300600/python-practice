def sum_rec(n):
	if n<=1:
		return n
	return n+sum_rec(n-1)
    

print(sum_rec(3))
