N, M = map(int, input("input N and M: ").split())
A, B, D = map(int, input("input initial state A, B and Direct D: ").split())

# 2-dimension array
map_list = []
for i in range(N):
    map_list.append(list(map(int, input().split())))

sum=0
num=0
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    # set direction
    D-=1
    if D == -1:
        D = 3
    if map_list[A+(steps[D][0])][B+(steps[D][1])] == 0:
        # check location
        map_list[A+(steps[D][0])][B+(steps[D][1])] = 2
        # move
        A += steps[D][0]
        B += steps[D][1]
        # count
        sum+=1
        #initialize
        num=0
    else:
        num+=1
        if (num==4) and (map_list[A+(steps[D-2][0])][B+(steps[D-2][1])] == 1):
            break
        elif (num==4) and (map_list[A+(steps[D-2][0])][B+(steps[D-2][1])] != 1):
            # move back
            A += steps[D-2][0]
            B += steps[D-2][1]
            num=0

print(sum)