N = int(input())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

for row in range(N):
    if A[row] != B[row]:
        for i in range(N):
            if A[row][i] != B[row][i]:
                print(row+1,i+1)
                exit()


