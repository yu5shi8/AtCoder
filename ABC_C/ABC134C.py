# -*- coding: utf-8 -*-
# C - Exception Handling
# https://atcoder.jp/contests/abc134/tasks/abc134_c

n = int(input())
a = [int(input()) for _ in range(n)] + [0]

sorted_a = sorted(a)
a_first = sorted_a[-1]
a_second = sorted_a[-2]

for i in range(n):
    if a[i] == a_first:
        print(a_second)
    else:
        print(a_first)

# 10:30 - 10:35（TLE）- 11:20（TLE）-（解説を閲覧）- 11:23（AC）
