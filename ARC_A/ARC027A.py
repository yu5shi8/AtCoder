# -*- coding: utf-8 -*-
# A - 門限
# https://atcoder.jp/contests/arc027/tasks/arc027_1

h, m = map(int, input().split())

limit = 18 * 60
check = h * 60 + m
ans = limit - check

print(ans)

# 17:18 - 17:22（AC）
