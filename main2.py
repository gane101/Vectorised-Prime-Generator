import matplotlib.pyplot as plt
import numpy as np
import time

primes = [2]

for i in range(2,500_000):
	flag = True
	
	for p in primes:
		if i%p == 0:
			flag = False
			break

	if flag:
		primes.append(i)

res = 1

func = []

for p in primes:
	res *= (1-1/p)
	func.append(res)

func = np.array(func)

plt.plot(func)
plt.grid()
plt.show()
