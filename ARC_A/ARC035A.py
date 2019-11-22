# -*- coding: utf-8 -*-
# A - 高橋くんと回文
# https://atcoder.jp/contests/arc035/tasks/arc035_a

s = input()
n = len(s) // 2

l = s[:n]
r = s[n:][::-1]

for i in range(n):
    if l[i] == r[i] or l[i] == '*' or r[i] == '*':
        continue
    else:
        print('NO')
        exit()

print('YES')

# 17:06 - 17:16（AC）
