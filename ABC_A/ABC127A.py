# -*- coding: utf-8 -*-
# A - Ferris Wheel
# https://atcoder.jp/contests/abc127/tasks/abc127_a

a, b = map(int, input().split())
ans = 0

if a >= 13:
    ans = b
elif 6 <= a <= 12:
    ans = b // 2
else:
    ans = 0

print(ans)

# 21:00 - 21:02
