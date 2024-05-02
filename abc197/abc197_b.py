h,w,y,x = map(int,input().split())
s = [list(input()) for _ in range(h)]
count = 1
pm_b = [1,-1]
x -= 1
y -= 1

for pm in pm_b:
    for ud in range(1,h):
        if 0 <= y - ud*pm < h:
            if s[y-ud*pm][x] == '#':
                break
            else:
                count += 1

    for rl in range(1,w):
        if 0 <= x - rl*pm < w:
            if s[y][x-rl*pm] == '#':
                break
            else:
                count += 1

print(count)