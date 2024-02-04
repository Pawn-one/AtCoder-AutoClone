S = input()
count = {}
for s in S:
    if s in count:
         count[s] += 1
    else:
         count[s] = 1

max_s = None
max_count = 0
for key, value in count.items():
    if max_count == value and ord(key) < ord(max_s):
        max_s = key
    elif max_count < value:
        max_count = value
        max_s = key

print(max_s)
          