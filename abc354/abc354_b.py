N = int(input())
S = []
C = []
for i in range(N):
    s,c = map(str,input().split())
    S.append(s)
    C.append(int(c))
S.sort()
print(S[sum(C)%N])