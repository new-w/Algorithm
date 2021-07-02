def solution(participant, completion):
    answer = ''
    d1 = {}
    d2 = {}
    
    # dictionary initialize
    for person in participant:
        d1[person] = d1.get(person, 0) + 1
    
    for temp in completion:
        d2[temp] = d2.get(temp, 0) + 1

    comm = list(set(participant) & set(completion))
    signal = 0

    # compare the number of keys
    for x in comm:
        if d1[x] !=d2[x]:
            answer = x
            signal = 1
    if signal == 0:
        comm = list(set(participant) - set(completion))
        answer = comm[0]

    return answer