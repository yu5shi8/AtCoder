# -*- coding: utf-8 -*-
# B - ∵∴∵
# https://atcoder.jp/contests/abc058/tasks/abc058_b

o = list(input())
e = list(input())
psw = ['0']*(len(o)+len(e))

for i in range(len(o)):
    j = i * 2
    psw[j] = o[i]
for i in range(len(e)):
    j = i * 2 + 1
    psw[j] = e[i]

print(*psw, sep='')

# 14:09 - 14:24
