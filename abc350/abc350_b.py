N,Q = map(int,input().split())
T = list(map(int,input().split()))
teeth = [True] * N
for num in T:
    if teeth[num-1] == True:
        teeth[num-1] = False
    else:
        teeth[num-1] = True
print(teeth.count(True))