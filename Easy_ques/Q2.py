# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

n = 5
i = 5
for i in range(1, i+1):
    for n in range(1, n+1):
        print(n, end=" ")
        n = n-1
    print("")
    i = i-1
