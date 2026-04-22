import math
from line_profiler import profile

n = 12

sm = 1
num = 6

table = {
	1 : (1,1),
	2 : (1,2),
	# 3 : (1,3),
	# 4 : (2,2),
	# 5 : (1,5),
	# 6 : (3,2),
	# 7 : (1,7),
	# 8 : (4,2),
	# 9 : (3,3),
	# 10 : (5,2),
	# 11 : (1,11),
	# 12 : (6,2)
}


@profile
def run(val):
	global sm,num

	primes = [2]

	# for i in range(2,val):
	# 	flag = True

	# 	for p in primes:
	# 		if i%p == 0:
	# 			flag = False
	# 			break

		# if flag:
			# primes.append(i)

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
			# for i in range(int(n/f)+1):
				# nums[i*f] = False

		# ratio = nums.count(True)/n
		ratio = sum(nums)/n
		# print(ratio)
		if ratio < sm:
			sm = ratio
			num = n
			print(num,sm)

run(100_000)

# print(num,sm)


# n = 20


# print(table)


# print(ls)



