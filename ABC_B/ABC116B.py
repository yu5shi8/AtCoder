# -*- coding: utf-8 -*-
# B - Collatz Problem
# https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
a = [s]
i = 0

while a.count(a[i]) != 2:
    if a[i] % 2 == 0:
        a.append(a[i]//2)
    else:
        a.append(3*a[i] + 1)
    i += 1

ans = len(a)
print(ans)

# 8:37 - 9:04
