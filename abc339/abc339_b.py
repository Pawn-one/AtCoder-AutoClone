def fun(s,x,y):
    if s == 'n':
        y += -1
    elif s == 'e':
        x += 1
    elif s == 's':
        y += 1
    elif s == 'w':
        x += -1
    return x,y

def check(x,y):
    if x < 0:
        x += w
    elif x >= w:
        x -= w
    if y < 0:
        y += h
    elif y >= h:
        y -= h
    return x,y

h,w,n = map(int,input().split())
box = [['.']*w for _ in range(h)]
x = 0
y = 0
d = ['n','e','s','w']
j = 0
for i in range(n):
    if box[y][x] == '.':
        box[y][x] = '#'
        j += 1
        if j >= 4:
            j = 0
        x,y = fun(d[j],x,y)
        x,y = check(x,y)
        
    elif box[y][x] == '#':
        box[y][x] = '.'
        j -= 1
        if j < 0:
            j = 3
        x,y = fun(d[j],x,y)
        x,y = check(x,y)
for s in box:
    print(''.join(s))

