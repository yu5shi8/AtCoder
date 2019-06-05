# -*- coding: utf-8 -*-
# A - 25個の文字列
# https://atcoder.jp/contests/abc025/tasks/abc025_a

s = input()
n = int(input())
name = []

for i in s:
    for j in s:
        name.append(i+j)

print(name[n-1])

# 16:44 - 16:48
