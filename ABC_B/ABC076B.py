# -*- coding: utf-8 -*-
# B - Addition and Multiplication
# https://atcoder.jp/contests/abc076/tasks/abc076_b

n = int(input())
num = 1
k = int(input())

for i in range(n):
    if num*2 < num+k:
        num *= 2
    else:
        num += k

print(num)

# 22:23 - 22:37
