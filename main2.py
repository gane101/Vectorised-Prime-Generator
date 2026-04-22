import matplotlib.pyplot as plt
import numpy as np
import time

primes = [2]

start = time.time()

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

end = time.time()

print(end-start)

func = np.array(func)
inc = func.copy()
inc = func[-11:-1] - inc[-10:]

print(func[-10:])
print(inc)

print(len(func))
print(primes[-1])

plt.plot(func)
plt.grid()
plt.show()
