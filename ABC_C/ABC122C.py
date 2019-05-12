# -*- coding: utf-8 -*-
# C - GeT AC
# https://atcoder.jp/contests/abc122/tasks/abc122_c

n, q = map(int, input().split())
s = input()

t = [0] * (n+1)
for i in range(n):
    t[i+1] = t[i] + (1 if s[i:i+2] == 'AC' else 0)

for i in range(q):
    l, r = map(int, input().split())
    print(t[r-1]-t[l-1])

'''
n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    left = lr[i][0] - 1
    right = lr[i][1]
    count = s[left:right].count('AC')
    print(count)
'''
# 12:32 - 12:52（TLE）
# （解説を閲覧）- 13:38
# （再挑戦）14:14 - 14:22
