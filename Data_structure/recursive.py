#iterative
def factorial_iterative(n):
    result=1
    for i in range(1, n+1):
        result *=i
    return result

#recursive
def factorial_recursive(n):
    if n==0:
        return 1
    return factorial_recursive(n-1) * n


print(factorial_iterative(7))
print(factorial_recursive(7))