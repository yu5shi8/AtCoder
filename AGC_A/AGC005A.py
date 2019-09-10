# -*- coding: utf-8 -*-
# A - STring
# https://atcoder.jp/contests/agc005/tasks/agc005_a

X = input()
s = cnt = 0

for i in range(len(X)):
    if X[i] == 'S':
        s += 1
    elif s != 0:
        cnt += 2
        s -= 1

ans = len(X) - cnt
print(ans)

# [1] 10:38 - 10:48（TLE）- 10:53（TLE）-（解答を閲覧）11:10
# [2] 13:37 - 13:47（AC）
