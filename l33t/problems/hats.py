#!/usr/bin/env python


dp = []
res = []

dp.append(1);
dp.append(0)

for i in range(2, 13):
    dp.append((i - 1) * (dp[i-1] + dp[i-2]))

res.append(1)
res.append(1)

for i in range(2, 13):
    res.append(i * res[i-1])

t = int(input())

for tt in range(0, t):
    n = int(input())
    print(str(dp[n]) + "/" + str(res[n]))
