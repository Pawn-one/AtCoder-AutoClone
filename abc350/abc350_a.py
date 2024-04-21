S = input()
abc = S[:3]
n = int(S[3:])
if abc == 'ABC' and n <= 349 and n != 316 and n >= 1:
    print('Yes')
else:
    print('No')
