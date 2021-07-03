def solution(phone_book):
    answer = True
    
    phone_book.sort() 
    #phone_book.sort(key=lambda x : len(x)) -> 이걸 넣으면 2중 for문을 사용해야만 풀 수 있게됨,,

    for i in range(len(phone_book)-1):
        
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    
    return answer