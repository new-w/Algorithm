N, M = map(int, input("input row & column: ").split())

card_list = []
min_list = []
for i in range(0, N):
    card_list.append(list(map(int, input().split())))
    min_list.append(min(card_list[i]))

print(min_list)