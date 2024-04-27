from collections import deque
N = int(input())
A = list(map(int,input().split()))

bolls = deque(A.copy())
ans = deque()

while 0 != len(bolls):
    if len(ans) != 0 and ans[-1] == bolls[0]:
        num = bolls.popleft()
        ans.pop()
        bolls.appendleft(num+1)

    else:
        ans.append(bolls.popleft())

print(len(ans))
