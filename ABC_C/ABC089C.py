# -*- coding: utf-8 -*-
# C - March
# https://atcoder.jp/contests/abc089/tasks/abc089_c

N = int(input())
S = [input() for _ in range(N)]
L = ['M', 'A', 'R', 'C', 'H']
dict_S = {}

for i in range(N):
    moji = S[i][0]
    if moji in L:
        if moji not in dict_S:
            dict_S[moji] = 1
        else:
            dict_S[moji] += 1

keys = len(dict_S.keys())
values = list(dict_S.values())

if keys < 3 or keys == None:
    print(0)
else:
    x = 0
    for i in range(keys):
        for j in range(i+1, keys):
            for k in range(j+1, keys):
                x += values[i] * values[j] * values[k]
    print(x)

# 13:25 - 14:04（WA）- 14:13（解説を閲覧）- 14:25（AC）
