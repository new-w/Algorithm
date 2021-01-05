#N = int(input("input N: "))
for N in range(0, 24):
    if N<3:
        K=0
        if N==0:
            K=0
            N=1
    elif (N>=3) and (N<13):
        K=1
    elif (N>=13) and (N<23):
        K=2
    elif (N>=23):
        K=3

    h = K * 60 * 60
    m = N * 60 * 15
    s = N * 60 * 15
    common = N * 15 * 15

    result = h + m + s - common
    print(N, ":", result)