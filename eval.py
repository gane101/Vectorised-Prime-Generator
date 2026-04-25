import time
import numpy as np
from line_profiler import profile
import math
import sys

# chosen = 9699690
# chosen = 510510
# chosen = 30030
chosen = int(sys.argv[1])
target = int(sys.argv[2])
# target = 100_000_000

# All primes upto the chosen number

primes = [2]
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

check = 223
# print(len(rmdr))
# print(sorted(set(rmdr%check)))
# print(len(sorted(set(rmdr%check))) == check)

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
		while primes[ind] * primes[ind] <= temp[-1]:
			part.append(primes[ind])
			ind += 1

		to_del = [] # Numbers to be deleted
		temp2 = temp.copy()
		for p in part:
			# Checking the remainder of all the numbers at once after dividing by p
			temp3 = temp2 % p
			# if 0 in temp3:
			temp2 = np.delete(temp2, np.where(temp3==0)[0])

		primes += list(temp2)
		# primes = list(set(primes))

# Running the program and calculating the time.

# print("Start")
start = time.time()
run()
end = time.time()
print(end-start)

print(len(primes))

# print(primes[:100])

# start = time.time()
# primes = [2]

# for i in range(2,target):
# 	flag = True
# 	for p in primes:
# 		if i%p == 0:
# 			flag = False
# 			break
# 		if p*p > i:
# 			break
# 	if flag:
# 		primes.append(i)

# end = time.time()
# print(end-start)



# start = time.time()
# primes = []
# nums = [1]*(target+1)

# nums[0] = 0
# nums[1] = 0
# nums[2] = 1

# for i in range(2,target):
# 	if nums[i] == 1:
# 		nums[i::i] = [0]*(int(target/i))
# 		primes.append(i)

# end = time.time()
# print(end-start)







