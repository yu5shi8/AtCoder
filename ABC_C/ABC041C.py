# -*- coding: utf-8 -*-
# C - 背の順
# https://atcoder.jp/contests/abc041/tasks/abc041_c

N = int(input())
i = [i for i in range(1, N+1)]
a = list(map(int, input().split()))
ans = []

for j in range(N):
    ans.append([a[j], i[j]])

ans.sort(reverse=True)

for k in ans:
    print(k[1])

# 16:58 - 17:08（AC）
