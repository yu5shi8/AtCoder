# -*- coding: utf-8 -*-
# C - ID
# https://atcoder.jp/contests/abc113/tasks/abc113_c

n, m = map(int, input().split())
py = [[i] + list(map(int, input().split())) for i in range(m)]
py.sort(key=lambda x:(x[1],x[2]))

city = py[0][1]
num = 0

for i in py:
    if i[1] == city:
        num += 1
    else:
        num = 1
        city = i[1]
    i.append(num)

py.sort(key=lambda x:[x[0]])

for i in py:
    print('{:06}{:06}'.format(i[1], i[3]))

# 15:42 - 15:54

