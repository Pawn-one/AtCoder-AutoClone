n,s,d = map(int,input().split())

damage = False
for i in range(n):
    x,y = map(int,input().split())
    if x < s and y > d:
        damage = True
if damage == True:
    print('Yes')
else:
    print('No')