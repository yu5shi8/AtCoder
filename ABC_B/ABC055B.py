# -*- coding: utf-8 -*-
# B - Training Camp
# https://atcoder.jp/contests/abc055/tasks/abc055_b

n = int(input()) + 1
mod = 10**9 + 7
power = 1

for i in range(1, n):
    power *= i
    power %= mod

print(power)

# 解説・解答を参照
# 17:26 - 18:12
