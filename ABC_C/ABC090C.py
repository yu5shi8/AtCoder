# -*- coding: utf-8 -*-
# C - Flip,Flip, and Flip......
# https://atcoder.jp/contests/abc090/tasks/arc091_a

n, m = map(int, input().split())
ans = 0

if n == 1 and m == 1:
    ans = 1
elif n == 1 and m >= 3:
    ans = m - 2
elif n >= 3 and m == 1:
    ans = n - 2
elif n >= 3 and m >= 3:
    ans = (n - 2) * (m - 2)
else:
    ans = 0

print(ans)

# [1] 16:14 -（解説・解答を閲覧）17:25
# [2] 17:35 - 17:42（AC）
