import time
import numpy as np
from line_profiler import profile
import math

chosen = 30030
target = 10_000_000
primes = [2]

# All primes upto the chosen number

for i in range(2,chosen):
	flag = True

	for p in primes:
		if i%p == 0:
			flag = False
			break
		if p*p > chosen:
			break
	if flag:
		primes.append(i)

# Make a vector of all the co-primes of the chosen number

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

	ind = 1
	part = [2]
	for i in range(1,n):

		temp += chosen

		# Checks if the subset of primes we are checking contains all primes less than sqrt of the largest number in current batch
		# Because checking all the primes is expensive. And making this array with list comprehension each time is also expensive.
		while primes[ind] * primes[ind] < temp[-1]:
			part.append(primes[ind])
			ind += 1

		to_del = [] # Numbers to be deleted
		for p in part:
			# Checking the remainder of all the numbers at once after dividing by p
			temp2 = temp % p
			if 0 in temp2:
				to_del += list(np.where(temp2==0)[0]) # Adding the numbers which are divisible by p in this list

		# Deleting the numbers at the indices from to_del and adding the remaining to the list of primes.
		temp2 = temp.copy().tolist()
		to_del = list(set(to_del))
		to_del.sort()
		if len(to_del) != 0:
			for j in range(1,len(to_del)+1):
				del temp2[to_del[-j]]
		primes += temp2

# Running the program and calculating the time.

start = time.time()
run()
end = time.time()
print(end-start)










