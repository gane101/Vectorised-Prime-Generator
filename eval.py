import time
import numpy as np
from line_profiler import profile
import math

chosen = 2310
target = 1_000_000
primes = [2]

for i in range(2,chosen):
	flag = True

	for p in primes:
		if p*p > chosen:
			break
		if i%p == 0:
			flag = False
			break
	if flag:
		primes.append(i)

factors = []
nums = [1]*(chosen+1)
nums[0] = 0

for p in primes:
	if chosen%p == 0:
		factors.append(p)
		nums[p::p] = [0]*(int(chosen/p))

rmdr = []
for i in range(chosen):
	if nums[i]==1:
		rmdr.append(i)
rmdr = np.array(rmdr)

n = int(target/chosen) + 1
temp = rmdr.copy()

@profile
def run():
	global temp,primes
	for i in range(1,n):


		temp += chosen

		part = [p for p in primes if p*p < temp[-1]]

		to_del = []
		for p in part:
			temp2 = temp % p
			if 0 in temp2:
				to_del += list(np.where(temp2==0)[0])
		temp2 = temp.copy().tolist()
		to_del = list(set(to_del))
		to_del.sort()
		if len(to_del) != 0:
			for j in range(1,len(to_del)+1):
				del temp2[to_del[-j]]
		primes += temp2

		
		# for v in temp:
		# 	flag = True

		# 	for p in part:
		# 		if v%p==0:
		# 			flag = False
		# 			break
		# 	if flag:
		# 		primes.append(int(v))


start = time.time()
run()
end = time.time()
print(end-start)

# print(primes)

# first = [1,2,3,4,5,6,7,8,9]

# a = np.array(first)
# b = a % 4

# print(b)

# i = np.where(b==0)[0]

# print(i)

# for j in range(1,len(i)+1):
	# del first[i[-j]]

# print(a)











