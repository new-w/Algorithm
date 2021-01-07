ans = input("input location: ")
row = int(ans[1])
col = ord(ans[0])               # change to ASCII code value

#ord(col)
move = []
for i in range(0, 8):
    move.append([col, row])


for i in range(0, 2):
    move[i][0] +=2
    if i==0:
        move[i][1]+=1
    else:
        move[i][1]-=1
for i in range(2, 4):
    move[i][0] -=2
    if i==2:
        move[i][1]+=1
    else:
        move[i][1]-=1
for i in range(4, 6):
    move[i][0] +=1
    if i==4:
        move[i][1]+=2
    else:
        move[i][1]-=2
for i in range(6, 8):
    move[i][0] -=1
    if i==6:
        move[i][1]+=2
    else:
        move[i][1]-=2

sum=0
for i in range(0, 8):
    if (move[i][0]>=97 and move[i][0] <=104):
        if(move[i][1]>=1 and move[i][1]<=8):
            sum+=1

print(sum)