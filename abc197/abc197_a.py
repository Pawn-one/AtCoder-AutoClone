from collections import deque
s = input()
s = deque(s)
f = s.popleft()
s.append(f)
print(''.join(s))