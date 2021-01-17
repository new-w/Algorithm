N = int(input())
value_list = list(map(int, input().split()))
money = int(input())

money_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0

# 자릿수를 크게 만드는 방법 -> 최대한 많은 개수의 숫자를 구입 -> 최대 개수의 숫자로 이루어진 값들의 크기를 비교하여 최종 선택

# 최대한 많은 개수의 숫자를 구입
share_list = []
for i in range(0, N):
    share_list.append(money // value_list[N-1-i])

for i in range(0, share_list[0]+1):
    

print(share_list)