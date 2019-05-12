# -*- coding: utf-8 -*-
# C - Five Transportations
# https://atcoder.jp/contests/abc123/tasks/abc123_c

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
trafic = [a, b, c, d, e]
ans = 5

if min(trafic) >= n:
    print(ans)
    exit()
else:
    if n % min(trafic) == 0:
        group = n//min(trafic) - 1
    else:
        group = n//min(trafic)

print(ans+group)

# 10:38 - 10:52
