s = 0
f = 0

i = 1
j = 1
while f < 4000000:
    f = i + j
    i = j 
    j = f
    if f % 2 == 0:
        s += f

print(f'sum of even Fibonacci numbers is {s}')