def factorial_iterative(n):
    result=1
    i=1
    for i in range(n+1):
        result = result * i

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_iterative(7))
print(factorial_recursive(7))