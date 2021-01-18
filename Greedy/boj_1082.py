def convert(num):
    sum=0
    for i in range(len(num)):
        sum = sum + (num[i]) * (10 ** (len(num)-i-1))
    return sum

N = int(input())
value_list = list(map(int, input().split()))
money = int(input())
cur_money = money

money_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_result=0
# 자릿수를 크게 만드는 방법 -> 최대한 많은 개수의 숫자를 구입 -> 최대 개수의 숫자로 이루어진 값들의 크기를 비교하여 최종 선택

# 최대한 많은 개수의 숫자를 구입
num_list = []
if N!=1:
    if (money//value_list[1]!=0):
        num_list.append(money_list[1])
        cur_money-=value_list[1]
        base = (money-value_list[1]) // value_list[0]
        if base!=0:
            for k in range(base):
                num_list.append(money_list[0])
                cur_money-=value_list[0]
        
        # 각 자리의 수를 최대 값으로 변경
        

    else:
        final_result=0

else:
    final_result=0

final_result = convert(num_list)
print(final_result, cur_money)