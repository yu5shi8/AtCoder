# -*- coding: utf-8 -*-
# B - Exponential
# https://atcoder.jp/contests/abc097/tasks/abc097_b

x = int(input())
ans = []

for b in range(1, x+1):
    for p in range(2, 100):
        num = pow(b, p)
        if num <= x:
            ans.append(num)
        else:
            break

print(max(ans))

# 14:41 - 14:52
