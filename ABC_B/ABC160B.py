# -*- coding: utf-8 -*-
# B - Golden Coins
# https://atcoder.jp/contests/abc160/tasks/abc160_b

X = int(input())

fh = 0
f  = 0

while X > 0:
    if X // 500 > 0:
        num = X // 500
        fh += num
        X -= num * 500
    elif X // 5 > 0:
        num = X // 5
        f += num
        X -= num * 5
    else:
        break

ans = 1000 * fh + 5 * f

print(ans)

# 23:13 - 23:25（AC）
