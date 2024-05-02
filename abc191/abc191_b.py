N,X = map(int,input().split())

a = list(map(int,input().split()))
box = []
for i in range(N):
    if a[i] != X:
        box.append(a[i])
print(*box)