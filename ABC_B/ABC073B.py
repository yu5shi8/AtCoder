# -*- coding: utf-8 -*-
# B - Theater
# https://atcoder.jp/contests/abc073/tasks/abc073_b

n = int(input())
num = 0

for i in range(n):
    l, r = map(int, input().split())
    num += (r-l) + 1

print(num)


# 13:07 - 13:12
