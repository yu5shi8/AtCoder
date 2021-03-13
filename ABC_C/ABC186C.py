# -*- coding: utf-8 -*-
# C - Unlucky 7
# https://atcoder.jp/contests/abc186/tasks/abc186_c

N = int(input())
ans = 0

for i in range(1, N+1):
    t = True
    e = True
    num = str(i)
    if '7' in num:
        t = False
    num = str(oct(i))
    if '7' in num:
        e = False
    if t == True and e == True:
        ans += 1

print(ans)

# 14:00 - 14:24（AC）
