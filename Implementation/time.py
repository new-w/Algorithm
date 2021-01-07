for N in range(0, 24):
    if (N>=0) and (N<3):
        K=0
        C=0
    elif (N>=3) and (N<13):
        K=1
        C=1575
    elif (N>=13) and (N<23):
        K=2
        C=3150
    elif (N>=23):
        K=3
        C=4725

    h = K * 60 * 60
    m = (N+1) * 60 * 15
    s = (N+1) * 60 * 15
    common = ((N+1) * 15 * 15) + C

    result = (h + m + s) - common
    print(N, ":", result)