s = 0

for i in range(1, 1001):
	if i % 3 == 0 or i % 5 == 0:
		s += i

print(f'sum of multiples of 3 and 5 within 1000 is {s}')