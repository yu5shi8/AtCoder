# -*- coding: utf-8 -*-
# B - 嘘つきの高橋くん
# https://atcoder.jp/contests/abc021/tasks/abc021_b

n = int(input())
a, b = map(int, input().split())
k = int(input())
p = sorted(list(map(int, input().split())) + [a] + [b])

for i in range(1, len(p)):
    if p[i - 1] == p[i]:
        print('NO')
        exit()

print('YES')

# 8:38 - 8:48（AC）
