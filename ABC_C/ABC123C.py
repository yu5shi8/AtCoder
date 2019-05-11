# -*- coding: utf-8 -*-
# C - Five Transportations
# https://atcoder.jp/contests/abc123/tasks/abc123_c

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
l = [a, b, c, d, e]
ans = 5
min_take = min(l)

if min(l) >= n:
    ans = 5
else:
    if n % min_take != 0:
        group = n // min_take
    else:
        group = n // min_take - 1
    ans += group

print(ans)

# 19:26 - 20:17
