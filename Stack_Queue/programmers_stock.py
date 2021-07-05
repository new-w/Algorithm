from collections import deque

def solution(prices):
    answer = []

    q = deque(prices)
    mem = 0

    for k in range(len(prices)-1):
        count = 0
        
        for i in range(len(q)-1):
           

            print(prices[k], prices[k + i + 1])
            count+=1
            if prices[k] > prices[k + i + 1]:
                mem = i
                break

        q.popleft()
        if mem == 0:
            answer.append(i+1)
        else:
            answer.append(count)
            
    answer.append(0)      

    return answer

ans = solution([0, 8, 1, 2, 7, 3, 5, 2])
print("result: ", ans)