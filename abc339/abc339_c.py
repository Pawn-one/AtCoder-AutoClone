N = int(input())
A = list(map(int,input().split()))
min = 0
pass_sum = 0
for i in A:
    pass_sum += i
    if pass_sum < min:
        min = pass_sum
print(pass_sum - min)
