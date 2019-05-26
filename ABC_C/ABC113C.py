# -*- coding: utf-8 -*-
# C - ID
# https://atcoder.jp/contests/abc113/tasks/abc113_c

n, m = map(int, input().split())
py = [[i] + list(map(int, input().split())) for i in range(m)]
py.sort(key=lambda x:(x[1], x[2]))

city = py[0][1]
num = 0

for i in py:
    if i[1] == city:
        num += 1
    else:
        num = 1
        city = i[1]
    i.append(num)

py.sort()

for i in py:
    print('{:06}{:06}'.format(i[1], i[3]))

# 17:29 - 18:23
#（解答を閲覧）23:25 - 23:47
#（再挑戦）23:51 - 24:05（RE）- 24:07（RE） - 24:09（AC）
