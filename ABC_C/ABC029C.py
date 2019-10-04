# -*- coding: utf-8 -*-
# C - Brute-force Attack
# https://atcoder.jp/contests/abc029/tasks/abc029_c

N = int(input())
L = ['a', 'b', 'c']
st = ['a', 'b', 'c']

if N == 1:
    print(*L, sep='\n')
    exit()

while N > 1:
    ans = []
    for i in L:
        for j in st:
            ans.append(i + j)
    N -= 1
    st = ans

print(*ans, sep='\n')

# 14:58 - 15:41（解説を閲覧 / AC）
