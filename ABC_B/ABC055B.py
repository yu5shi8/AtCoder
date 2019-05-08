# -*- coding: utf-8 -*-
# B - Training Camp
# https://atcoder.jp/contests/abc055/tasks/abc055_b

n = int(input())+1
num = 10**9+7
power = 1

for i in range(1, n):
    power = power * i

ans = power % num
print(ans)

# 16:53 - 17:24（TLE）
