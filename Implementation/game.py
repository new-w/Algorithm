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
    if num == 4:
        break
    if map_list[A + steps[D-1][0]][B + steps[D-1][1]] == 0:
        D-=1
        A += steps[D-1][0]
        B += steps[D-1][1]
        sum+=1
        num=0
    else:
        D-=1
        num+=1
print(sum)