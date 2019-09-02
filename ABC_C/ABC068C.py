# -*- coding: utf-8 -*-
# C - Cat Snuke and a Voyage
# https://atcoder.jp/contests/abc068/tasks/arc079_a

N, M = map(int, input().split())
A = set()
B = set()

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        A.add(b)
    elif b == N:
        B.add(a)

if A & B:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

# 10:10 - 10:35（TLE）- 10:43（TLE）- 10:51（TLE）-10:58（TLE）-10:59（TLE）-（解説・解答を閲覧）11:09（AC）
