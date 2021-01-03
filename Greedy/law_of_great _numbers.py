N, M, K = input("input N, M, K : ").split()
N = int(N)
M = int(M)
K = int(K)

num_list = input("input values : ").split()
num_list = list(map(int, num_list))

# find maximum value

# find second maximum valueK


sum = 0
for j in range(0, M):
    for i in range(0, K):
        sum+=max(num_list)
    M = M - K
