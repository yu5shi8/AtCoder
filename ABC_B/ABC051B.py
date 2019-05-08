# -*- coding: utf-8 -*-
# B - Sum of Three Integers
# https://atcoder.jp/contests/abc051/tasks/abc051_b

k, s = map(int, input().split())
count = 0

for x in range(k+1):
    for y in range(k+1):
        if 0 <= s-x-y <= k:
            count += 1

print(count)

# 22:53 - 23:15
