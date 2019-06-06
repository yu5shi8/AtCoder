# -*- coding: utf-8 -*-
# A - 動物園
# https://atcoder.jp/contests/abc024/tasks/abc024_a

a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

member = s + t
ans = 0

if member >= k:
    ans = (a-c)*s + (b-c)*t
else:
    ans = a*s + b*t

print(ans)

# 9:24 - 9:28

