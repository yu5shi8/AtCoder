# -*- coding: utf-8 -*-
# B - 回転
# https://atcoder.jp/contests/abc036/tasks/abc036_b

n = int(input())
s = [input() for _ in range(n)]
ans = []

for i in range(n):
    array = ''
    for j in range(n-1, -1, -1):
        array += s[j][i]
        if len(array) == n:
            ans.append(array)

print(*ans, sep='\n')

# 22:46 - 23:05
