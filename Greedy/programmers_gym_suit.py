def solution(n, lost, reserve):
    answer=0
    stu = []
    for i in range(1, n+1):
        stu.append(i)
    
    # standard case
    s1 = set(lost) & set(reserve)
    s1 = list(s1)
    for i in range(0, len(s1)):
        reserve.remove(s1[i])
        lost.remove(s1[i])
    
    s2 = [x for x in stu if x not in lost]
    s2 = [x for x in s2 if x not in reserve]
    num_s = len(s2) + len(reserve)
    
    # lent
    num_l = 0
    for i in range(0, len(lost)):
        if lost[i]+1 in reserve:
            num_l +=1
            reserve.remove(lost[i]+1)
        elif lost[i]-1 in reserve:
            num_l +=1
            reserve.remove(lost[i]-1)
    answer = num_s + num_l
    
    return answer