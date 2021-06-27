def solution(people, limit):
    answer = 0
    cur = 0
    end = len(people)-1

    people.sort(reverse=True)
    
    while True:
        # the biggest one
        if  cur > end:
            break
        answer+=1
        temp = limit - people[cur]

        cur+=1
        if cur == len(people):
            break

        # extra
        if temp - people[end] >=0:
            end-=1
    
    return answer