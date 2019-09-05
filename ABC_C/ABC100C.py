# -*- coding: utf-8 -*-
# C - *3 or /2
# https://atcoder.jp/contests/abc100/tasks/abc100_c

N = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    while i % 2 == 0:
        i //= 2
        count += 1

print(count)

# 8:43 - 9:14（TLE）- 9:30（解説を閲覧）- 9:37（AC）
