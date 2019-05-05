# -*- coding: utf-8 -*-
# B - Two Switches
# https://atcoder.jp/contests/abc070/tasks/abc070_b

a, b, c, d = map(int, input().split())
ans = min(b, d) - max(a, c)

if ans < 0:
    ans = 0

print(ans)

# 13:48 - 14:14
