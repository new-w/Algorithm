money = int(input("input money: "))
change = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    temp_change = money // coin
    change = change + temp_change
    money = money % coin

print("chage: ", change)