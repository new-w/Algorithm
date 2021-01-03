N, M, K = input("input N, M, K: ").split()
N = int(N)
M = int(M)
K = int(K)

num_list = input("input values  ").split()
num_list = list(map(int, num_list))

# find maximum value
max1 = max(num_list)
num_list.remove(max1)

# find second maximum value
max2 = max(num_list)

a = M // (K+1)
b = M % (K+1)
sum=0
for j in range(0, a):
    for i in range(0, K):
        sum+=max1
    sum+=max2
for l in range(0, b):
    sum+=max1

print("sum: ", sum)