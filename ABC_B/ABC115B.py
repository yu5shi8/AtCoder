# -*- coding: utf-8 -*-
# B - Christmas Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_b

n = int(input())
p = [int(input()) for _ in range(n)]

ans = (sum(p) - max(p)) + (max(p) // 2)

print(ans)

# 10:19 - 10:23
