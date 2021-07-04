from collections import deque

def solution(progresses, speeds):
    answer = []
    
    p = deque(progresses)
    s = deque(speeds)
    
    while len(p)!=0:
        count = 0
        day = (100 - p[0]) // s[0]
        if day == 0:
            day=1
        if p[0] + (day * s[0]) <100:
            day+=1
            
        p.popleft()
        s.popleft()
        count+=1

        for num in range(len(p)):
            p[num] = p[num] + (s[num] * day)

        for i in range(len(p)):
            if p[i] >= 100:
                count+=1
            else:
                break
            
        for j in range(count-1):
            p.popleft()
            s.popleft()
        
        answer.append(count)
    
    return answer