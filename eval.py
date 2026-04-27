import time
import numpy as np
from line_profiler import profile
import math
import sys

# 2,6,30,210,2310,30030,510510,9699690,223092870

chosen = int(sys.argv[1])
target = int(sys.argv[2])

options = [2,6,30,210,2310,30030,510510,9699690,223092870]

# All primes upto the chosen number

start = time.time()
primes = [2,3,5,7,11,13,17,19,23]
for i in range(23,chosen):
	flag = True

	for p in primes:
		if i%p == 0:
			flag = False
			break
		if p*p > i:
			break
	if flag:
		primes.append(i)
end = time.time()
print(end-start)
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

for i in range(len(options)):
	if options[i] == chosen:
		part = [primes[i+1]]
		ind = i+2
		# print(part,ind)
		break

@profile
def run():
	global temp,primes,part,ind

	# ind = 1
	# part = [2,3,5,7,11,13,17,19,23]
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
			# temp2 = np.delete(temp2, np.where(temp2 % p==0)[0])
			# np.delete(temp2, np.where(temp2 % p==0)[0])
			# if len(temp) == 0:
				# break


		primes += list(temp2)
		# primes = list(set(primes))

# Running the program and calculating the time.

start = time.time()
run()
end = time.time()
print(end-start)

print(len(primes))

# print(primes)

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

# nums = [1]*(target+1)
# primes = []
# start = time.time()
# for i in range(2,target):
# 	if nums[i] == 1:
# 		nums[i::i] = [0]*(int(target/i))
# 		primes.append(i)
# end = time.time()
# print(end-start)

# print(primes)






