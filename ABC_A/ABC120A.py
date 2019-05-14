# -*- coding: utf-8 -*-
# A - Favorite Sound
# https://atcoder.jp/contests/abc120/tasks/abc120_a

a, b, c = map(int, input().split())
ans = b // a

if ans >= c:
    print(c)
else:
    print(ans)

# 21:38 - 21:43
