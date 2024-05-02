N = int(input())
j = {}
for i in range(N):
    s,t = map(str,input().split())
    j[s] = int(t)
print(sorted(j.items(),key=lambda x:x[1])[-2][0])
