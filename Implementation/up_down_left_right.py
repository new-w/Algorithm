size = int(input("input size: "))
direction_list = input("input direction: ").split()

x = 1
y = 1
for direction in direction_list:
    if direction == 'U':
        if y-1 > 0:
            y-=1
    elif direction == 'D':
        if y+1 <= size:
            y+=1
    elif direction == 'L':
        if x-1 > 0:
            x-=1
    else:
        if x+1 <= size:
            x+=1

print("location is -> ", y, x)