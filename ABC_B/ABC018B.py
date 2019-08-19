# -*- coding: utf-8 -*-
# B - 文字列の反転
# https://atcoder.jp/contests/abc018/tasks/abc018_2

s = list(input())
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    l = lr[i][0] - 1
    r = lr[i][1]
    new_s = s[l:r]
    new_s.reverse()
    s[l:r] = new_s

print(''.join(s))

# 16:45 - 17:01（AC）
