# -*- coding: utf-8 -*-
# C - Scc Puzzle
# https://atcoder.jp/contests/abc055/tasks/arc069_a

N, M = map(int, input().split())

if N >= M // 2:
    ans = M // 2
else:
    ans = N
    M -= N * 2
    if M >= 4:
        ans += M // 4

print(ans)

# 14:06 - 14:24（AC）
