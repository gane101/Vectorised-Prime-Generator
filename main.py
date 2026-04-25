import math
from line_profiler import profile

n = 12

sm = 1
num = 6

# A hastable of numbers in the form, n:(n/p,p), where p is the first prime dividing n.
table = {
	1 : (1,1),
	2 : (1,2)
}

@profile
def run(val):
	global sm,num

	primes = [2]

	# Finding the primes
	for n in range(2,val):
		factors = []
		flag = True
		for i in primes:
			if n%i == 0:
				table[n] = (int(n/i),i)
				flag = False
				break
		if flag:
			table[n] = (1,n)
			primes.append(n)
			continue

		low = n

		while low != 1:
			factors.append(table[low][1])
			low = table[low][0]

		factors = set(factors)
		nums = [1]*(n+1)
		nums[0] = 0

		for f in factors:
			nums[f::f] = [0]*(int(n/f))

		ratio = sum(nums)/n
		if ratio < sm:
			sm = ratio
			num = n
			print(num,sm)

run(1_000_000)



