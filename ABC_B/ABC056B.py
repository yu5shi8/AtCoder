# -*- coding: utf-8 -*-
# B - NarrowRectanglesEasy
# https://atcoder.jp/contests/abc056/tasks/abc056_b

w, a, b = map(int, input().split())
ans = max(a, b) - (min(a, b)+w)

if ans <= 0:
    print(0)
else:
    print(ans)

# 16:37 - 16:51
