Q = int(input())
box = []
for i in range(Q):
    k,n = map(int,input().split())
    if k == 1:
       box.append(n) 
    elif k == 2:
        print(box[-n])

