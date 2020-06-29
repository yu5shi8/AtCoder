# -*- coding: utf-8 -*-
# A - We Love Golf
# https://atcoder.jp/contests/abc165/tasks/abc165_a

K = int(input())
A, B = map(int, input().split())

for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        exit()

print('NG')

# 21:44 - 21:46（AC）
