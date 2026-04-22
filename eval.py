import time
import numpy as np
from line_profiler import profile
import math

chosen = 510510
target = 10_000_000
primes = [2]

for i in range(2,chosen):
	flag = True

	for p in primes:
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
	global temp
	for i in range(1,n):

		temp += chosen

		part = [p for p in primes if p*p < temp[-1]]

		for v in temp:
			flag = True

			for p in part:
				if v%p==0:
					flag = False
					break
			if flag:
				primes.append(int(v))


start = time.time()
run()
end = time.time()
print(end-start)
# print(primes)

