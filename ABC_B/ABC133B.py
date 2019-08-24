# -*- coding: utf-8 -*-
# B - Good Distance
# https://atcoder.jp/contests/abc133/tasks/abc133_b

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(i+1, n):
        num = 0
        for k in range(d):
            num += (x[i][k] - x[j][k]) ** 2
        check = pow(num, 0.5)
        if check.is_integer():
            count += 1

print(count)

# [1] 20:02 -（解説・解答を閲覧）- （math使わなくてもいけるみたい）
# [2] 17:03 - 17:23（AC）
