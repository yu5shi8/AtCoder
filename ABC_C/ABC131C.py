# -*- coding: utf-8 -*-
# C - Anti-Division
# https://atcoder.jp/contests/abc131/tasks/abc131_c

import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

a, b, c, d = map(int, input().split())
a -= 1
cd = lcm(c, d)

upper = b - b//c - b//d + b//cd
lower = a - a//c - a//d + a//cd
ans = upper - lower

print(ans)

# 21:29 - 22:23（RE）- 22:25（RE）- 22:26（WA）
#（解説・解答を閲覧）- 23:36
