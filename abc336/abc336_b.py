N = int(input())
bin_n = bin(N)
bin_n = bin_n[::-1]
count = 0
for symbol in bin_n:
    if symbol == '0':
        count += 1
    else:
        break
print(count)

