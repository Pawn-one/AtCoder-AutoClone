H = int(input())
t = 0
i = 0
while t <= H:
    t += 2**i
    i += 1
print(i)
