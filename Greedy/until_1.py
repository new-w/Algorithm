N, K = map(int, input("input N & K: ").split())

sum = 0
while 1:
    extra = N % K
    if(extra != 0):
        sum+=extra
        N -=extra
    N = N // K
    sum+=1
    if(N == 1):
        break

print(sum)