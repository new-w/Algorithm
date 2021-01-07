ans = input("input location: ")
row = int(ans[1])
col = ans[0]

#ord(col)
move = []
for i in range(0, 6):
    move.append([row, col])


print(ord(move[0][1]))