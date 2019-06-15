# -*- coding: utf-8 -*-
# B - 文字数カウント
# https://atcoder.jp/contests/abc028/tasks/abc028_b

s = list(input())
l = ['A', 'B', 'C', 'D', 'E', 'F']
ans = [0] * 6

for i in range(6):
    ans[i] = s.count(l[i])

print(*ans, sep=' ')

# 18:15 - 18:29
