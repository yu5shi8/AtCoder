# -*- coding: utf-8 -*-
# B - Maximum Difference
# https://atcoder.jp/contests/abc102/tasks/abc102_b

n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
min_a = min(a)
ans = max_a - min_a
print(ans)

# 15:28 - 15:36
