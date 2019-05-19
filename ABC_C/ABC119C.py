# -*- coding: utf-8 -*-
# C - Synthetic Kadomatsu
# https://atcoder.jp/contests/abc119/tasks/abc119_c

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
inf = 10**9

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else inf
    no_merge = dfs(cur+1, a, b, c)
    merge_a = dfs(cur+1, a+L[cur], b, c) + 10
    merge_b = dfs(cur+1, a, b+L[cur], c) + 10
    merge_c = dfs(cur+1, a, b, c+L[cur]) + 10
    return min(no_merge, merge_a, merge_b, merge_c)

print(dfs(0, 0, 0, 0))

# 10:34 - 10:55
