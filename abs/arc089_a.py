N = int(input())
Box = [None]*(N+1)
Box[0] = [0,0,0]
for i in range(1,N+1):
    t,x,y = map(int,input().split())
    Box[i] = [t,x,y]

def check_rout(Box,N):
    for i in range(1,N+1):
        Number_of_moves = Box[i][0]-Box[i-1][0]
        difference_in_x = abs(Box[i][1]-Box[i-1][1])
        difference_in_y = abs(Box[i][2]-Box[i-1][2])
        if Number_of_moves < difference_in_x+difference_in_y:
            return 0
        elif (Number_of_moves - (difference_in_x+difference_in_y)) % 2 == 1:
            return 0
    return 1

if check_rout(Box,N) == 1:
    print('Yes')
else:
    print('No')
    
                

    
        

