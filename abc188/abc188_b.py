N = int(input())
sum_ab = 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(N):
    sum_ab += a[i]*b[i]

if sum_ab == 0:
    print('Yes')
else:
    print('No')