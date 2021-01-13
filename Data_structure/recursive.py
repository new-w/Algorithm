def recursive_function(num):
    print(num, ":", "번째 재귀함수 호출")
    num+=1
    if num == 101:
        return
    recursive_function(num)

recursive_function(1)