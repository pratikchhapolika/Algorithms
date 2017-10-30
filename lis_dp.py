def lis(l):
    dp = [1] * len(l)
    u = [-1] * len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] >= l[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                u[i] = j

    maximum = 0
    index = 0
    for i, v in enumerate(dp):
        if v > maximum:
            maximum = v
            index = i


    
    lnds = [l[index]]
    while index > 0:
        lnds.append(l[u[index]])
        index = u[index]

    print lnds[::-1]

    return max(dp)

print lis([3, 45, 23, 9, 99, 99])
