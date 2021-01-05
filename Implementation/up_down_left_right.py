size = int(input("input size: "))
direction_list = input("input direction: ").split()

print(direction_list)

list_size = len(direction_list)

x = 1
y = 1
for i in range(list_size):
    if direction_list[i] == 'U':
        print("Up")
        if y-1 > 0:
            y-=1
    elif direction_list[i] == 'D':
        print("Down")
        if y+1 <= size:
            y+=1
    elif direction_list[i] == 'L':
        print("left")
        if x-1 > 0:
            x-=1
    else:
        print("right")
        if x+1 <= size:
            x+=1

print("location is -> ", y, x)