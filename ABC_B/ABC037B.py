# -*- coding: utf-8 -*-
# B - 編集
# https://atcoder.jp/contests/abc037/tasks/abc037_b

n, q = map(int, input().split())
lrt = [list(map(int, input().split())) for _ in range(q)]
a = [0] * n

for i in range(q):
    start = lrt[i][0] - 1
    end = lrt[i][1]
    num = lrt[i][2]
    for j in range(start, end):
        a[j] = num

print(*a, sep='\n')

# 6:26 - 6:38
