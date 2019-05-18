# -*- coding: utf-8 -*-
# C - Synthetic Kadomatsu
# https://atcoder.jp/contests/abc119/tasks/abc119_c

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
inf = 10 ** 9

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else inf
    non_marge = dfs(cur+1, a, b, c)
    marge_a = dfs(cur+1, a+L[cur], b, c) + 10
    marge_b = dfs(cur+1, a, b+L[cur], c) + 10
    marge_c = dfs(cur+1, a, b, c+L[cur]) + 10
    return min(non_marge, marge_a, marge_b, marge_c)

print(dfs(0, 0, 0, 0))

# 23:13 -（解説を閲覧）23:43
# 穴埋め 0:30 - 0:40
# 0:40 - 0:45

# 参考URL
# https://reud.net/2019/02/26/atcoder-beginner-contest-119-c-synthetic-kadomatsu-%E6%84%9F%E6%83%B3/ß